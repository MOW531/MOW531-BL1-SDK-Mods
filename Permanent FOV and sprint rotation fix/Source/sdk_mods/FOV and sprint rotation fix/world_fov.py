import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command
from mods_base.options import BaseOption, SliderOption

def obj (definition:str, object:str):
    unrealsdk.load_package(object)
    unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    return unrealsdk.find_object(definition, object)


def Set_FOV():
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


def Set_FOV_from_slider(option:BaseOption, value:float):
    pc = get_pc()
    if pc is not None:
        pc.DesiredFOVBaseValue = value
        pc.DesiredFOV = value
        pc.DefaultFOV = value
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

WorldFOV = SliderOption("World FOV", 70, 50, 140, 1, True, on_change=Set_FOV_from_slider)


@hook(
    hook_func="WillowGame.WillowPlayerController:SpawningProcessComplete",
    hook_type=Type.POST,
)
def on_startgame(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    Set_FOV()