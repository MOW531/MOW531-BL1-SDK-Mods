import unrealsdk #type: ignore
from unrealsdk import logging #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

WeaponChanged = True
currentweapon = None
EquippedWeapons = []

def GetEquippedWeapons():
    global EquippedWeapons
    EquippedWeapons.clear()
    for items in get_pc().pawn.Children:
        if str(items.Class) == "Class'WillowGame.WillowWeapon'":
            if items.quickselectslot > 0:
                EquippedWeapons.append(int(items.quickselectslot))
    EquippedWeapons.sort()

@hook(
    hook_func="WillowGame.WillowPlayerController:NextWeapon",
    hook_type=Type.PRE,
)
def NextWeapon(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global EquippedWeapons
    global currentweapon
    global WeaponChanged
    if get_pc().pawn.weapon != None:
        GetEquippedWeapons()
        if WeaponChanged == True:
            WeaponChanged = False
            currentweapon = int(EquippedWeapons.index(int(get_pc().pawn.weapon.quickselectslot))) + 1
        currentweapon = currentweapon + 1
        if currentweapon > len(EquippedWeapons):
            currentweapon = 1
        get_pc().pawn.invmanager.EquipWeaponFromSlot(EquippedWeapons[currentweapon - 1])
    return Block

@hook(
    hook_func="WillowGame.WillowPlayerController:PrevWeapon",
    hook_type=Type.PRE,
)
def PrevWeapon(

    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global EquippedWeapons
    global currentweapon
    global WeaponChanged
    if get_pc().pawn.weapon != None:
        GetEquippedWeapons()
        if WeaponChanged == True:
            WeaponChanged = False
            currentweapon = int(EquippedWeapons.index(int(get_pc().pawn.weapon.quickselectslot))) + 1
        currentweapon = currentweapon - 1
        if currentweapon < 1:
            currentweapon = len(EquippedWeapons)
        get_pc().pawn.invmanager.EquipWeaponFromSlot(EquippedWeapons[currentweapon - 1])

    return Block

@hook(
    hook_func="WillowGame.WillowInventoryManager:ChangedWeapon",
    hook_type=Type.PRE,
)
def ChangedWeapon(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
   # print("ChangedWeapon")
    global WeaponChanged
    WeaponChanged = True


# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    keybinds=[],
    hooks=[NextWeapon, PrevWeapon, ChangedWeapon],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/ScrollWheelFix.json"),
)

logging.info(f"Scroll Wheel Fix Loaded: {__version__}, {__version_info__}")