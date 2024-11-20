import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command
from mods_base.options import BaseOption, SliderOption

bPatched = False


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
def on_startgame_world(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched
    if bPatched is False:
        bPatched = True


def SetFOV(option:BaseOption, value:float):
    global bPatched
    if bPatched is True:

        for controllers in unrealsdk.find_all("WillowPlayerController"):
            controllers.DesiredFOVBaseValue = value
            controllers.DesiredFOV = value
            controllers.DefaultFOV = value
            obj("PlayerClassDefinition","gd_Roland.Character.CharacterClass_Roland").FOV = value
            obj("PlayerClassDefinition","gd_Brick.Character.CharacterClass_Brick").FOV = value
            obj("PlayerClassDefinition","gd_lilith.Character.CharacterClass_Lilith").FOV = value
            obj("PlayerClassDefinition","gd_mordecai.Character.CharacterClass_Mordecai").FOV = value
            obj("WillowVehicle_WheeledVehicle","gd_lightrunner.VehicleArchetype.LightRunner_Rockets").AfterburnerMaxFOV = (value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_lightrunner.VehicleArchetype.LightRunner_MG").AfterburnerMaxFOV = (value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_saltracer.VehicleArchetype.SaltRacer").AfterburnerMaxFOV = (value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_DLC3_Stunt_Runner.VehicleArchetype.DLC3_Stunt_Runner_Rockets").AfterburnerMaxFOV = (value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_DLC3_Lancer.VehicleArchetype.DLC3_lancer").AfterburnerMaxFOV = (value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_DLC3_Cheetah_Paw.VehicleArchetype.DLC3_Cheetah_Paw").AfterburnerMaxFOV = (value + 10)

WorldFOV = SliderOption("World FOV", 70, 0, 160, 1, True, on_change=SetFOV)


@hook(
    hook_func="WillowGame.WillowPlayerController:SpawningProcessComplete",
    hook_type=Type.POST,
)
def SpawningProcessComplete(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched
    if bPatched is True:

        for controllers in unrealsdk.find_all("WillowPlayerController"):
            controllers.DesiredFOVBaseValue = WorldFOV.value
            controllers.DesiredFOV = WorldFOV.value
            controllers.DefaultFOV = WorldFOV.value
            obj("PlayerClassDefinition","gd_Roland.Character.CharacterClass_Roland").FOV = WorldFOV.value
            obj("PlayerClassDefinition","gd_Brick.Character.CharacterClass_Brick").FOV = WorldFOV.value
            obj("PlayerClassDefinition","gd_lilith.Character.CharacterClass_Lilith").FOV = WorldFOV.value
            obj("PlayerClassDefinition","gd_mordecai.Character.CharacterClass_Mordecai").FOV = WorldFOV.value
            obj("WillowVehicle_WheeledVehicle","gd_lightrunner.VehicleArchetype.LightRunner_Rockets").AfterburnerMaxFOV = (WorldFOV.value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_lightrunner.VehicleArchetype.LightRunner_MG").AfterburnerMaxFOV = (WorldFOV.value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_saltracer.VehicleArchetype.SaltRacer").AfterburnerMaxFOV = (WorldFOV.value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_DLC3_Stunt_Runner.VehicleArchetype.DLC3_Stunt_Runner_Rockets").AfterburnerMaxFOV = (WorldFOV.value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_DLC3_Lancer.VehicleArchetype.DLC3_lancer").AfterburnerMaxFOV = (WorldFOV.value + 20)
            obj("WillowVehicle_WheeledVehicle","gd_DLC3_Cheetah_Paw.VehicleArchetype.DLC3_Cheetah_Paw").AfterburnerMaxFOV = (WorldFOV.value + 10)


@hook(
    hook_func="WillowGame.WillowVehicleBase:DriverEnter",
    hook_type=Type.POST,
)
def DriverEnter(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched
    if bPatched is True:

        obj("WillowVehicle_WheeledVehicle","gd_lightrunner.VehicleArchetype.LightRunner_Rockets").AfterburnerMaxFOV = (WorldFOV.value + 20)
        obj("WillowVehicle_WheeledVehicle","gd_lightrunner.VehicleArchetype.LightRunner_MG").AfterburnerMaxFOV = (WorldFOV.value + 20)
        obj("WillowVehicle_WheeledVehicle","gd_saltracer.VehicleArchetype.SaltRacer").AfterburnerMaxFOV = (WorldFOV.value + 20)
        obj("WillowVehicle_WheeledVehicle","gd_DLC3_Stunt_Runner.VehicleArchetype.DLC3_Stunt_Runner_Rockets").AfterburnerMaxFOV = (WorldFOV.value + 20)
        obj("WillowVehicle_WheeledVehicle","gd_DLC3_Lancer.VehicleArchetype.DLC3_lancer").AfterburnerMaxFOV = (WorldFOV.value + 20)
        obj("WillowVehicle_WheeledVehicle","gd_DLC3_Cheetah_Paw.VehicleArchetype.DLC3_Cheetah_Paw").AfterburnerMaxFOV = (WorldFOV.value + 10)

@hook(
    hook_func="WillowGame.WillowVehicleBase:DriverLeave",
    hook_type=Type.POST,
)
def DriverLeave(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched
    if bPatched is True:

        for controllers in unrealsdk.find_all("WillowPlayerController"):
            controllers.DesiredFOVBaseValue = WorldFOV.value
            controllers.DesiredFOV = WorldFOV.value
            controllers.DefaultFOV = WorldFOV.value
            obj("PlayerClassDefinition","gd_Roland.Character.CharacterClass_Roland").FOV = WorldFOV.value
            obj("PlayerClassDefinition","gd_Brick.Character.CharacterClass_Brick").FOV = WorldFOV.value
            obj("PlayerClassDefinition","gd_lilith.Character.CharacterClass_Lilith").FOV = WorldFOV.value
            obj("PlayerClassDefinition","gd_mordecai.Character.CharacterClass_Mordecai").FOV = WorldFOV.value
