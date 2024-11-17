import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command
from mods_base.options import BaseOption, SliderOption

WorldFOV = SliderOption("World FOV", 70, 0, 160, 1, True)


@hook(
    hook_func="WillowGame.WillowPlayerController:AdjustFOV",
    hook_type=Type.POST,
)
def SetFOV(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    for controllers in unrealsdk.find_all("WillowPlayerController"):
        if controllers.DesiredFOVBaseValue < WorldFOV.value or controllers.DesiredFOVBaseValue > WorldFOV.value + 15:
            controllers.DesiredFOVBaseValue = WorldFOV.value
        if controllers.DesiredFOV < WorldFOV.value or controllers.DesiredFOV > WorldFOV.value + 15:
            controllers.DesiredFOV = WorldFOV.value
        if controllers.DefaultFOV < WorldFOV.value or controllers.DefaultFOV > WorldFOV.value + 15:
            controllers.DefaultFOV = WorldFOV.value
        if controllers.pawn != None:
            Vehicle = (str(controllers.pawn.objectarchetype).find("Vehicle"))
            if Vehicle != -1:
                Cheetah_Paw = (str(controllers.pawn.objectarchetype).find("DLC3_Cheetah_Paw"))
                if Cheetah_Paw > -1:
                    controllers.Pawn.AfterburnerMaxFOV = (WorldFOV.value + 10)
                else:
                    controllers.Pawn.AfterburnerMaxFOV = (WorldFOV.value + 20)
        if controllers.CharacterClass != None:
            controllers.CharacterClass.FOV = WorldFOV.value