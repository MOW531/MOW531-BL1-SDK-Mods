import unrealsdk #type: ignore
from unrealsdk import logging #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

WeaponChanged = True

def NextWeapon(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    global currentweapon
    global WeaponChanged
    if WeaponChanged == True:
        WeaponChanged = False
        currentweapon = get_pc().pawn.weapon.quickselectslot
    MaxWeapons = get_pc().pawn.invmanager.GetWeaponReadyMax()
    currentweapon = currentweapon + 1
    if currentweapon > MaxWeapons:
        currentweapon = 1
   # print(currentweapon)
    get_pc().pawn.invmanager.EquipWeaponFromSlot(currentweapon)
    return Block

remove_hook("WillowGame.WillowPlayerController:NextWeapon", Type.PRE, "NextWeapon")
add_hook("WillowGame.WillowPlayerController:NextWeapon", Type.PRE, "NextWeapon", NextWeapon)

def PrevWeapon(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    global currentweapon
    global WeaponChanged
    if WeaponChanged == True:
        WeaponChanged = False
        currentweapon = get_pc().pawn.weapon.quickselectslot
    MaxWeapons = get_pc().pawn.invmanager.GetWeaponReadyMax()
    currentweapon = currentweapon - 1
    if currentweapon < 1:
        currentweapon = MaxWeapons
   # print(currentweapon)
    get_pc().pawn.invmanager.EquipWeaponFromSlot(currentweapon)

    return Block

remove_hook("WillowGame.WillowPlayerController:PrevWeapon", Type.PRE, "PrevWeapon")
add_hook("WillowGame.WillowPlayerController:PrevWeapon", Type.PRE, "PrevWeapon", PrevWeapon)

def ChangedWeapon(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
   # print("ChangedWeapon")
    global WeaponChanged
    WeaponChanged = True

remove_hook("WillowGame.WillowInventoryManager:ChangedWeapon", Type.PRE, "ChangedWeapon")
add_hook("WillowGame.WillowInventoryManager:ChangedWeapon", Type.PRE, "ChangedWeapon", ChangedWeapon)



# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    keybinds=[],
    hooks=[],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/ScrollWheelFix.json"),
)

logging.info(f"Scroll Wheel Fix Loaded: {__version__}, {__version_info__}")