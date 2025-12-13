import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem

flash_path = "topLevel_mc.card"
flash_element_techicon = "chemical.gotoAndStop"


ComparingItem = None

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

        else:
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")

# Comparing view
def Vendor_CompareView(obj):
    global ComparingItem
    if obj.IsComparing() is True:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
        if SelectedItem is not None:
            
            # Set Element Icon
            obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, GetElementIconForItem(SelectedItem))
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(ComparingItem))





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
    global ComparingItem
    if obj.bOnItemOfTheDay is True:
        ComparingItem = obj.ItemOfTheDayData.Item
    else:
        ComparingItem = obj.ActiveTextList.GetHighlightedObject()