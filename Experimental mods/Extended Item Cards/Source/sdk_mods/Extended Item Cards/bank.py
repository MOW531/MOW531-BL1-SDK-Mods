import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem, GetFunStats, single_item, default_card, inv_default_cards, inv_compare_items

flash_path = "currentPage.card"
flash_element_techicon = "chemical.gotoAndStop"
flash_element_funstats = "funstats.htmlText"

IsComparing = False

ComparingItem = None

LeftCard = 0

# Non-comparing view
def bank_NormalView(obj):
    global IsComparing
    if IsComparing is False:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
        if SelectedItem is not None:

            # Set Element Icon
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(SelectedItem))

            # Set FunStats
            obj.SetVariableString(flash_path + "1." + flash_element_funstats, GetFunStats(SelectedItem))


            # Add reload info to the card
            if "WillowWeapon" in str(SelectedItem.Class):
                single_item(obj, SelectedItem, flash_path, flash_joiner="1.")

            # Make sure the reload text it cleared when not wanted
            else:
                default_card(obj, flash_path, flash_joiner="1.")

        # Make sure the reload text and element icon are cleared when not wanted
        else:
            default_card(obj, flash_path, flash_joiner="1.")
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")


# Compare view
def bank_CompareView(obj):
    global ComparingItem
    global IsComparing
    global LeftCard
    if IsComparing is True:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
        if SelectedItem is not None:

            # Set Element Icon
            if SelectedItem is not None and ComparingItem is not None:
                obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, GetElementIconForItem(SelectedItem))
                obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(ComparingItem))

            # Set FunStats
            obj.SetVariableString(flash_path + "1." + flash_element_funstats, GetFunStats(ComparingItem))
            obj.SetVariableString(flash_path + "2." + flash_element_funstats, GetFunStats(SelectedItem))

            inv_compare_items(obj, SelectedItem, ComparingItem, flash_path, LeftCard)


        else:

            obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, "none")
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")

            inv_default_cards(obj, flash_path)



@hook(
    hook_func="WillowGame.BankGFxMovie:extCard2Visible",
    hook_type=Type.POST,
)
def bankStartCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    bank_NormalView(obj)
    bank_CompareView(obj)


@hook(
    hook_func="WillowGame.BankGFxMovie:UpdateCardPanelWithCurrentActiveListEntry",
    hook_type=Type.POST,
)
def bankChangeSelectedItemMouse(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    bank_NormalView(obj)
    bank_CompareView(obj)


@hook(
    hook_func="WillowGame.BankGFxMovie:StartComparing",
    hook_type=Type.PRE,
)
def bankPrepCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global LeftCard
    global ComparingItem
    global IsComparing
    IsComparing = True
    SelectedItem = obj.ActiveTextList.GetHighlightedObject()
    if SelectedItem is not None:
        ComparingItem = SelectedItem

        if "WillowEquipAbleItem" in str(SelectedItem.Class):
            if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                LeftCard = SelectedItem.UIStatModifiers[2].ModifierTotal


@hook(
    hook_func="WillowGame.BankGFxMovie:LeaveCompare",
    hook_type=Type.PRE,
)
def bankStopCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global IsComparing
    IsComparing = False