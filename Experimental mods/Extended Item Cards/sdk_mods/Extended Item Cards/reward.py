import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem


flash_path = "reward.card1"
flash_element_main = "rls.text"
flash_element_main_text = "Reload Time"
flash_element_main_text_eridian = "Recharge Delay"
flash_element_number = "reloadspeed.text"
flash_element_arrow4 = "arrow4.gotoAndStop"
flash_element_techicon = "chemical.gotoAndStop"

def Reward_NormalView(obj):
    SelectedItem = obj.CardContents.Inv
    if SelectedItem is not None:
        
        obj.SingleArgInvokeS(flash_path + "." + flash_element_techicon, GetElementIconForItem(SelectedItem))

        if "WillowWeapon" in str(SelectedItem.Class):

            if SelectedItem.DefinitionData.ManufacturerDefinition == unrealsdk.find_object("ManufacturerDefinition","gd_manufacturers.Manufacturers.Eridian"):
                obj.SetVariableString(flash_path + "." + flash_element_main, flash_element_main_text_eridian)
            else:
                obj.SetVariableString(flash_path + "." + flash_element_main, flash_element_main_text)

            obj.SetVariableString(flash_path + "." + flash_element_number, str(round(SelectedItem.ReloadTimeBaseValue, 1)))
            obj.SingleArgInvokeS(flash_path + "." + flash_element_arrow4, "Blank")

        else:
            
            obj.SetVariableString(flash_path + "." + flash_element_main, "")
            obj.SetVariableString(flash_path + "." + flash_element_number, "")
            obj.SingleArgInvokeS(flash_path + "." + flash_element_arrow4, "Blank")

    else:
        obj.SingleArgInvokeS(flash_path + "." + flash_element_techicon, "none")

        obj.SetVariableString(flash_path + "." + flash_element_main, "")
        obj.SetVariableString(flash_path + "." + flash_element_number, "")
        obj.SingleArgInvokeS(flash_path + "." + flash_element_arrow4, "Blank")




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