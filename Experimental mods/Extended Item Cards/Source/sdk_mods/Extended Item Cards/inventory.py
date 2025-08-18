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
def INV_NormalView(obj):
    if obj.IsComparing() is False:
        SelectedItem = obj.GetCurrentHighlightedObject()
        if SelectedItem is not None:

            # Set Element Icon
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(SelectedItem))

            # Set FunStats
            obj.SetVariableString(flash_path + "1." + flash_element_funstats, GetFunStats(SelectedItem))

            #if "WillowEquipAbleItem" in str(SelectedItem.Class):
                #if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_tunercuffs.A_Item.Item_GrenadeModulator"):
                    #print(SelectedItem)
                    #obj.SetVariableString("topLevel_mc.card1.rof.text","Firerate")
                    #obj.SetVariableString("topLevel_mc.card1.firerate.text","RoF")



            # Add reload info to card
            if "WillowWeapon" in str(SelectedItem.Class):
                single_item(obj, SelectedItem, flash_path, flash_joiner="1.")

        # Clear reload info card
        else:
            default_card(obj, flash_path, flash_joiner="1.")
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")

# Comparing view
def INV_CompareView(obj):
    global LeftCard
    global ComparingItem
    if obj.IsComparing() is True:
        SelectedItem = obj.GetCurrentHighlightedObject()
        if SelectedItem is not None:

            # Set Element Icon
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(ComparingItem))
            obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, GetElementIconForItem(SelectedItem))

            # Set FunStats
            obj.SetVariableString(flash_path + "1." + flash_element_funstats, GetFunStats(ComparingItem))
            obj.SetVariableString(flash_path + "2." + flash_element_funstats, GetFunStats(SelectedItem))


            #Add shield delay arrow and compare
            inv_compare_items(obj, SelectedItem, ComparingItem, flash_path, LeftCard)

        else:
            inv_default_cards(obj, flash_path)
            obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, "none")



@hook(
    hook_func="WillowGame.StatusMenuExGFxMovie:extCard2Visible",
    hook_type=Type.POST,
)
def InvStartCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    INV_NormalView(obj)
    INV_CompareView(obj)


@hook(
    hook_func="WillowGame.StatusMenuExGFxMovie:UpdateCardPanelWithCurrentCell",
    hook_type=Type.POST,
)
def InvChangeSelectedItemKey(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    INV_NormalView(obj)
    INV_CompareView(obj)

@hook(
    hook_func="WillowGame.StatusMenuExGFxMovie:UpdateCardPanelWithCurrentActiveListEntry",
    hook_type=Type.POST,
)
def InvChangeSelectedItemMouse(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    INV_NormalView(obj)
    INV_CompareView(obj)


@hook(
    hook_func="WillowGame.StatusMenuExGFxMovie:extCompare",
    hook_type=Type.PRE,
)
def InvPrepCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global ComparingItem
    global LeftCard
    SelectedItem = obj.GetCurrentHighlightedObject() # obj.ActiveTextList.GetHighlightedObject()
    if SelectedItem is not None:

        ComparingItem = SelectedItem

        if "WillowEquipAbleItem" in str(SelectedItem.Class):
            if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                LeftCard = SelectedItem.UIStatModifiers[2].ModifierTotal
