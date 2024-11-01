import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook,get_pc

@hook(
    hook_func="WillowGame.WillowPlayerController:SpawningProcessComplete",
    hook_type=Type.POST,
)
def on_player_loaded(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    unrealsdk.load_package("gd_skills_common.Basic.Reload")
    unrealsdk.find_object("SkillDefinition", "gd_skills_common.Basic.Reload").Behaviors.OnActivated = []