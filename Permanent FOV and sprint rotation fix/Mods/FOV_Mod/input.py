import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command
from mods_base.options import BaseOption, SliderOption, BoolOption


bPatched = False

bReloadFix = BoolOption("Keyboard Reload Fix", True)

current_obj = None

def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)

@hook(
    hook_func="Engine.WorldInfo:IsMenuLevel",
    hook_type=Type.PRE,
)
def reloadfix(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    if bReloadFix.value is True:
        obj("SkillDefinition", "gd_skills_common.Basic.Reload").Behaviors.OnActivated = []