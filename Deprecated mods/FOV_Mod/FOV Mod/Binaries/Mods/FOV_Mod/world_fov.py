import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command
from mods_base.options import BaseOption, SliderOption

def SetFOV(option:BaseOption, value:float):
    for controllers in unrealsdk.find_all("WillowPlayerController"):
        controllers.DesiredFOVBaseValue = value
        controllers.DesiredFOV = value
        controllers.DefaultFOV = value
        if controllers.pawn != None:
            Vehicle = (str(controllers.pawn.objectarchetype).find("Vehicle"))
            if Vehicle != -1:
                Cheetah_Paw = (str(controllers.pawn.objectarchetype).find("DLC3_Cheetah_Paw"))
                if Cheetah_Paw > -1:
                    controllers.Pawn.AfterburnerMaxFOV = (value + 10)
                else:
                    controllers.Pawn.AfterburnerMaxFOV = (value + 20)
        if controllers.CharacterClass != None:
            controllers.CharacterClass.FOV = value

WorldFOV = SliderOption("World FOV", 70, 0, 160, 1, True, on_change=SetFOV)


@hook(
    hook_func="WillowGame.WillowPlayerController:SpawningProcessComplete",
    hook_type=Type.POST,
)
def SpawningProcessComplete(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    for controllers in unrealsdk.find_all("WillowPlayerController"):
        controllers.DesiredFOVBaseValue = WorldFOV.value
        controllers.DesiredFOV = WorldFOV.value
        controllers.DefaultFOV = WorldFOV.value

@hook(
    hook_func="WillowGame.WillowVehicleBase:DriverEnter",
    hook_type=Type.POST,
)
def DriverEnter(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    for controllers in unrealsdk.find_all("WillowPlayerController"):
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
@hook(
    hook_func="WillowGame.WillowVehicleBase:DriverLeave",
    hook_type=Type.POST,
)
def DriverLeave(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    for controllers in unrealsdk.find_all("WillowPlayerController"):
        controllers.DesiredFOVBaseValue = WorldFOV.value
        controllers.DesiredFOV = WorldFOV.value
        controllers.DefaultFOV = WorldFOV.value


