import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem, GetFunStats

pickup_flash_path = "inventory.card1"
flash_element_main = "rls.text"
flash_element_main_text = "Reload Time"
flash_element_main_text_eridian = "Recharge Delay"
flash_element_number = "reloadspeed.text"
flash_element_arrow3 = "arrow3.gotoAndStop"
flash_element_arrow4 = "arrow4.gotoAndStop"
flash_element_techicon = "chemicalmod.gotoAndStop"
flash_element_funstats = "funstatsmod.htmlText"

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

        # Set FunStats
        obj.SetVariableString(pickup_flash_path + "." + flash_element_funstats, GetFunStats(GroundItem))


    if GroundItem is not None and EquippedItem is not None:
            
            if "WillowEquipAbleItem" in str(GroundItem.Class) and "WillowEquipAbleItem" in str(EquippedItem.Class):
                if GroundItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield") and EquippedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                    EquippedItemNumber = EquippedItem.UIStatModifiers[2].ModifierTotal
                    GroundItemNumber = GroundItem.UIStatModifiers[2].ModifierTotal
                    if GroundItemNumber < EquippedItemNumber:
                        obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_arrow3,"Up")
                    if GroundItemNumber > EquippedItemNumber:
                        obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_arrow3,"Down")
                    if GroundItemNumber == EquippedItemNumber:
                        obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_arrow3,"Same")

            if "WillowWeapon" in str(GroundItem.Class):

                if str(GroundItem.DefinitionData.ManufacturerDefinition) in ["ManufacturerDefinition'gd_manufacturers.Manufacturers.Eridian'","ManufacturerDefinition'Eridian_Weapons_Overhaul.Shared.Manufacturers.Eridian'"]:
                    obj.SetVariableString(pickup_flash_path + "." + flash_element_main, flash_element_main_text_eridian)
                else:
                    obj.SetVariableString(pickup_flash_path + "." + flash_element_main, flash_element_main_text)

                obj.SetVariableString(pickup_flash_path + "." + flash_element_number, str(round(GroundItem.ReloadTimeBaseValue, 1)))

                if round(GroundItem.ReloadTimeBaseValue, 1) < round(EquippedItem.ReloadTimeBaseValue, 1):
                    
                    obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_arrow4,"Up")

                elif round(GroundItem.ReloadTimeBaseValue, 1) > round(EquippedItem.ReloadTimeBaseValue, 1):

                    obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_arrow4,"Down")

                elif round(GroundItem.ReloadTimeBaseValue, 1) == round(EquippedItem.ReloadTimeBaseValue, 1):


                    obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_arrow4,"Same")


    elif GroundItem is not None and EquippedItem is None and "WillowWeapon" in str(GroundItem.Class):

        if str(GroundItem.DefinitionData.ManufacturerDefinition) in ["ManufacturerDefinition'gd_manufacturers.Manufacturers.Eridian'","ManufacturerDefinition'Eridian_Weapons_Overhaul.Shared.Manufacturers.Eridian'"]:
            obj.SetVariableString(pickup_flash_path + "." + flash_element_main, flash_element_main_text_eridian)
        else:
            obj.SetVariableString(pickup_flash_path + "." + flash_element_main, flash_element_main_text)

        obj.SetVariableString(pickup_flash_path + "." + flash_element_number, str(round(GroundItem.ReloadTimeBaseValue, 1)))
        obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_arrow4,"Blank")
    else:
        obj.SetVariableString(pickup_flash_path + "." + flash_element_main, "")
        obj.SetVariableString(pickup_flash_path + "." + flash_element_number, "")
        obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_arrow4, "Blank")


def EquippedCardWhileComparing_Text():
    global EquippedCard_obj
    global PickupCard_obj
    CurrentWeapon = get_pc().pawn.weapon

    if PickupCard_obj is not None and EquippedCard_obj is not None and PickupCard_obj.MyHUDOwner.ItemComparison[0] is not None and PickupCard_obj.MyHUDOwner.ItemComparison[1] is not None and "WillowWeapon" not in str(PickupCard_obj.MyHUDOwner.ItemComparison[0].Class):
        EquippedCard_obj.SingleArgInvokeS(hud_flash_path + "." + flash_element_techicon, GetElementIconForItem(PickupCard_obj.MyHUDOwner.ItemComparison[1]))


    if PickupCard_obj is not None and EquippedCard_obj is not None and PickupCard_obj.MyHUDOwner.ItemComparison[0] is not None and "WillowWeapon" in str(PickupCard_obj.MyHUDOwner.ItemComparison[0].Class):
        if CurrentWeapon is not None:
            EquippedCard_obj.SingleArgInvokeS(hud_flash_path + "." + flash_element_techicon, GetElementIconForItem(CurrentWeapon))

            EquippedCard_obj.SetVariableString(hud_flash_path + "." + flash_element_number, str(round(CurrentWeapon.ReloadTimeBaseValue, 1)))        

        



def EquippedCardWhileNotComparing_Text():
    global EquippedCard_obj
    global PickupCard_obj
    global DesiredWeapon

    #print("Change Color")
    #EquippedCard_obj.SingleArgInvokeS("p1.shield.color.gotoAndStop","yellow")
    #EquippedCard_obj.SingleArgInvokeS("p1.ring.shield.color.gotoAndStop","yellow")


    if PickupCard_obj is None or PickupCard_obj is not None and PickupCard_obj.MyHUDOwner.ItemComparison[0] is None:
        if EquippedCard_obj is not None and DesiredWeapon is not None:
            EquippedCard_obj.SetVariableString(hud_flash_path + "." + flash_element_number, str(round(DesiredWeapon.ReloadTimeBaseValue, 1)))
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




@hook(
    hook_func="WillowGame.WillowHUDGFxMovie:extEnemyRingFadeInFinished",
    hook_type=Type.POST,
)
def ArmorCheck(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    Armored = 2
    pc = get_pc()
    if pc is not None:
        if pc.AutoAimStrategy.InstantaneousTarget is not None:

            if str(pc.AutoAimStrategy.InstantaneousTarget.Class.name) in "WillowVehicle_WheeledVehicle":
                obj.SingleArgInvokeS("p1.ring.health.bar.gotoAndStop","armored")

            elif pc.AutoAimStrategy.InstantaneousTarget.BodyClass.DefaultHitRegion.DefaultDamageSurfaceType == Armored:
                obj.SingleArgInvokeS("p1.ring.health.bar.gotoAndStop","armored")

        elif pc.AutoAimStrategy.LastInstantaneousTarget is not None:

            if str(pc.AutoAimStrategy.LastInstantaneousTarget.Class.name) in "WillowVehicle_WheeledVehicle":
                obj.SingleArgInvokeS("p1.ring.health.bar.gotoAndStop","armored")

            elif pc.AutoAimStrategy.LastInstantaneousTarget.BodyClass.DefaultHitRegion.DefaultDamageSurfaceType == Armored:
                obj.SingleArgInvokeS("p1.ring.health.bar.gotoAndStop","armored")

        elif str(pc.pawn.Class.name) in "WillowVehicle_WheeledVehicle" and pc.pawn.lockedpawn is not None:

            if str(pc.pawn.lockedpawn.Class.name) in "WillowVehicle_WheeledVehicle":
                obj.SingleArgInvokeS("p1.ring.health.bar.gotoAndStop","armored")

            elif pc.pawn.lockedpawn.BodyClass.DefaultHitRegion.DefaultDamageSurfaceType == Armored:
                obj.SingleArgInvokeS("p1.ring.health.bar.gotoAndStop","armored")