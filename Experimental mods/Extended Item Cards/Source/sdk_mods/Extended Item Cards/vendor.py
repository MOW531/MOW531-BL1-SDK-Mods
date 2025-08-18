import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem, GetFunStats, single_item, default_card, inv_default_cards, inv_compare_items

flash_path = "topLevel_mc.card"
flash_element_techicon = "chemical.gotoAndStop"
flash_element_funstats = "funstats.htmlText"


ComparingItem = None
LeftCard = 0

# Non-comparing view
def Vendor_NormalView(obj):
    global LeftCard
    if obj.IsComparing() is False:
        
        if obj.bOnItemOfTheDay is True:
            SelectedItem = obj.ItemOfTheDayData.Item
        else:
            SelectedItem = obj.ActiveTextList.GetHighlightedObject()

        if SelectedItem is not None:
            
            #Set Element Icon
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(SelectedItem))

            # Set FunStats
            obj.SetVariableString(flash_path + "1." + flash_element_funstats, GetFunStats(SelectedItem))

            # Add reload info to card
            if "WillowWeapon" in str(SelectedItem.Class):
                single_item(obj, SelectedItem, flash_path, flash_joiner="1.")
                
            else:
                default_card(obj, flash_path, flash_joiner="1.")

        else:
            default_card(obj, flash_path, flash_joiner="1.")
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")

# Comparing view
def Vendor_CompareView(obj):
    global LeftCard
    global ComparingItem
    if obj.IsComparing() is True:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
        if SelectedItem is not None:
            
            # Set Element Icon
            obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, GetElementIconForItem(SelectedItem))
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(ComparingItem))

            # Set FunStats
            obj.SetVariableString(flash_path + "1." + flash_element_funstats, GetFunStats(ComparingItem))
            obj.SetVariableString(flash_path + "2." + flash_element_funstats, GetFunStats(SelectedItem))


            inv_compare_items(obj, SelectedItem, ComparingItem, flash_path, LeftCard)

        else:
            inv_default_cards(obj, flash_path)



@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:extCard2Visible",
    hook_type=Type.POST,
)
def VendorStartCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global LeftCard
    Vendor_NormalView(obj)
    Vendor_CompareView(obj)


@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:UpdateCardPanelWithItemOfTheDay",
    hook_type=Type.POST,
)
def VendorChangeSelectedItemKey(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    Vendor_NormalView(obj)
    Vendor_CompareView(obj)

@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:UpdateCardPanelWithCurrentActiveListEntry",
    hook_type=Type.POST,
)
def VendorChangeSelectedItemMouse(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    Vendor_NormalView(obj)
    Vendor_CompareView(obj)


@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:extCompare",
    hook_type=Type.PRE,
)
def VendorPrepCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global LeftCard
    global ComparingItem
    if obj.bOnItemOfTheDay is True:
        SelectedItem = obj.ItemOfTheDayData.Item
    else:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
    if SelectedItem is not None:

        ComparingItem = SelectedItem

        if "WillowEquipAbleItem" in str(SelectedItem.Class):
            if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                LeftCard = SelectedItem.UIStatModifiers[2].ModifierTotal
