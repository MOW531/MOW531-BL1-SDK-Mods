import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem

pickup_flash_path = "inventory.card1"
flash_element_techicon = "chemicalmod.gotoAndStop"
hud_flash_path = "p1.outerequip.equipcard"

PickupCard_obj = None

EquippedCard_obj = None

DesiredWeapon = None




def PickupCard_CompareView(obj, EquippedItem = None):
    GroundItem =  obj.MyHUDOwner.ItemComparison[0]
    
    if EquippedItem is None:
        EquippedItem = obj.MyHUDOwner.ItemComparison[1]

    if GroundItem is not None:
        obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_techicon, GetElementIconForItem(GroundItem))



def EquippedCardWhileComparing_Text():
    global EquippedCard_obj
    global PickupCard_obj
    CurrentWeapon = get_pc().pawn.weapon

    if PickupCard_obj is not None and EquippedCard_obj is not None and PickupCard_obj.MyHUDOwner.ItemComparison[0] is not None and PickupCard_obj.MyHUDOwner.ItemComparison[1] is not None and "WillowWeapon" not in str(PickupCard_obj.MyHUDOwner.ItemComparison[0].Class):
        EquippedCard_obj.SingleArgInvokeS(hud_flash_path + "." + flash_element_techicon, GetElementIconForItem(PickupCard_obj.MyHUDOwner.ItemComparison[1]))


    if PickupCard_obj is not None and EquippedCard_obj is not None and PickupCard_obj.MyHUDOwner.ItemComparison[0] is not None and "WillowWeapon" in str(PickupCard_obj.MyHUDOwner.ItemComparison[0].Class):
        if CurrentWeapon is not None:
            EquippedCard_obj.SingleArgInvokeS(hud_flash_path + "." + flash_element_techicon, GetElementIconForItem(CurrentWeapon))


        



def EquippedCardWhileNotComparing_Text():
    global EquippedCard_obj
    global PickupCard_obj
    global DesiredWeapon


    if PickupCard_obj is None or PickupCard_obj is not None and PickupCard_obj.MyHUDOwner.ItemComparison[0] is None:
        if EquippedCard_obj is not None and DesiredWeapon is not None:
            EquippedCard_obj.SingleArgInvokeS(hud_flash_path + "." + flash_element_techicon, GetElementIconForItem(DesiredWeapon))



@hook(
    hook_func="WillowGame.ItemPickupGFxMovie:UpdateCompareAgainstThing",
    hook_type=Type.POST,
)
def PickupcardCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global PickupCard_obj
    PickupCard_obj = obj
    PickupCard_CompareView(obj)
    EquippedCardWhileComparing_Text()


@hook(
    hook_func="WillowGame.WillowPawn:WeaponChanged",
    hook_type=Type.POST,
)
def WeaponChanged(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global PickupCard_obj
    if PickupCard_obj is not None:
        PickupCard_CompareView(PickupCard_obj, obj.Weapon)
        EquippedCardWhileComparing_Text()


@hook(
    hook_func="WillowGame.WillowHUDGFxMovie:extEquippedCardOpened",
    hook_type=Type.POST,
)
def extEquippedCardOpened(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global EquippedCard_obj
    EquippedCard_obj = obj
    EquippedCardWhileComparing_Text()
    EquippedCardWhileNotComparing_Text()

@hook(
    hook_func="Engine.InventoryManager:SetCurrentWeapon",
    hook_type=Type.POST,
)
def SetCurrentWeapon(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global DesiredWeapon
    DesiredWeapon = (__args.DesiredWeapon)


@hook(
    hook_func="Engine.WorldInfo:IsMenuLevel",
    hook_type=Type.PRE,
)
def HUDClearVars(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global PickupCard_obj
    global EquippedCard_obj
    global DesiredWeapon
    PickupCard_obj = None
    EquippedCard_obj = None
    DesiredWeapon = None