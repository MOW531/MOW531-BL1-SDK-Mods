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
def INV_NormalView(obj):
    if obj.IsComparing() is False:
        SelectedItem = obj.GetCurrentHighlightedObject()
        if SelectedItem is not None:
            # Set Element Icon
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(SelectedItem))

        else:
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")

# Comparing view
def INV_CompareView(obj):
    global ComparingItem
    if obj.IsComparing() is True:
        SelectedItem = obj.GetCurrentHighlightedObject()
        if SelectedItem is not None:

            # Set Element Icon
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(ComparingItem))
            obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, GetElementIconForItem(SelectedItem))


        else:
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
    ComparingItem = obj.GetCurrentHighlightedObject() # obj.ActiveTextList.GetHighlightedObject()
