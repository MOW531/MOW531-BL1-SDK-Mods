import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem


flash_path = "reward.card1"
flash_element_techicon = "chemical.gotoAndStop"

def Reward_NormalView(obj):
    SelectedItem = obj.CardContents.Inv
    if SelectedItem is not None:
        obj.SingleArgInvokeS(flash_path + "." + flash_element_techicon, GetElementIconForItem(SelectedItem))

    else:
        obj.SingleArgInvokeS(flash_path + "." + flash_element_techicon, "none")




@hook(
    hook_func="WillowGame.QuestAcceptGFxMovie:extSetUpRewardsPage",
    hook_type=Type.POST,
)
def DisplayRewardsPage(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    Reward_NormalView(obj)