import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command
from mods_base.options import BaseOption, SliderOption, BoolOption

def obj (definition:str, object:str):
    unrealsdk.load_package(object)
    return unrealsdk.find_object(definition, object)

def reloadfix(option:BaseOption, value:bool):

    if value is True:
        obj("SkillDefinition", "gd_skills_common.Basic.Reload").Behaviors.OnActivated = []
    else:
        ReloadStruct = unrealsdk.make_struct("SkillPredictedEventReactionData",bPredictOnClient=True)
        ReloadStruct.Behaviors.append(unrealsdk.construct_object("PlayerBehavior_Reload",obj("SkillDefinition", "gd_skills_common.Basic.Reload")))
        obj("SkillDefinition", "gd_skills_common.Basic.Reload").Behaviors.OnActivated.append(ReloadStruct)

bReloadFix = BoolOption("Keyboard Reload Fix", True, on_change=reloadfix)



