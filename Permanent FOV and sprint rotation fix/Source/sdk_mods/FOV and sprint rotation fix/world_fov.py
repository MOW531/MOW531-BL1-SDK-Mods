import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command, ENGINE
from mods_base.options import BaseOption, SliderOption, BoolOption


def obj (definition:str, object:str):
    object_class = unrealsdk.find_class(definition)
    current_obj = ENGINE.DynamicLoadObject(object, object_class, False)
    current_obj.ObjectFlags |= 0x4000
    return current_obj

def lerp(v0: float, v1: float, t: float):
    return v0 + t * (v1 - v0)

def GetFOVScaled(EndFOV, StartFOV):
    return StartFOV * (EndFOV / 70)


def Set_FOV_from_slider(option:BaseOption, value:float):
    pc = get_pc()
    if pc is not None:
        pc.DesiredFOV = value
        pc.DesiredFOVBaseValue = value
        if pc.pawn is not None:
            if pc.pawn.Class == unrealsdk.find_class("WillowGame.WillowVehicle_WheeledVehicle"):
                if pc.pawn.objectarchetype == obj("WillowVehicle_WheeledVehicle","gd_lightrunner.VehicleArchetype.LightRunner_Rockets") or pc.pawn.objectarchetype == obj("WillowVehicle_WheeledVehicle","gd_lightrunner.VehicleArchetype.LightRunner_MG") or pc.pawn.objectarchetype == obj("WillowVehicle_WheeledVehicle","gd_DLC3_Stunt_Runner.VehicleArchetype.DLC3_Stunt_Runner_Rockets") or pc.pawn.objectarchetype == obj("WillowVehicle_WheeledVehicle","gd_DLC3_Lancer.VehicleArchetype.DLC3_lancer") or pc.pawn.objectarchetype == obj("WillowVehicle_WheeledVehicle","gd_saltracer.VehicleArchetype.SaltRacer"):
                    pc.pawn.AfterburnerMaxFOV = (value + 20)
                elif pc.pawn.objectarchetype == obj("WillowVehicle_WheeledVehicle","gd_DLC3_Cheetah_Paw.VehicleArchetype.DLC3_Cheetah_Paw"):
                    pc.pawn.AfterburnerMaxFOV = (value + 10)
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

def Set_EyeHeight_from_slider(option:BaseOption, value:float):
    for SkillEffectDefinition in obj("SkillDefinition","gd_skills_common.Basic.DoubleTime").SkillEffectDefinitions:
        if str(SkillEffectDefinition.AttributeToModify) in "AttributeDefinition'd_attributes.GameplayAttributes.EyeHeightModifier'":
            SkillEffectDefinition.BaseModifierValue.BaseValueConstant = value * 0.01
def Set_PainFOV_from_slider(option:BaseOption, value:float):
    get_pc().myhud.huddef.MaximumPainFOV = value


WorldFOV = SliderOption("World FOV", 70, 50, 140, 1, True, on_change=Set_FOV_from_slider)
SprintFOVModifier = SliderOption("Sprint FOV Modifier", 15, 0, 30, 1, True)
EyeHeight = SliderOption("Eye Height Modifier", -2, -5, 5, 1, True, on_change=Set_EyeHeight_from_slider)
bKeepFOVInAir = BoolOption("Keep FOV while in air", True)
PainFOV = SliderOption("Pain FOV Modifier", -1, -2, 2, 1, True, on_change=Set_PainFOV_from_slider)
bScaleADSFov = BoolOption("Scale ADS FOV", True)


bIsSprinting = False


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
    pc = get_pc()
    if pc is not None:
        pc.DesiredFOV = WorldFOV.value
        pc.DesiredFOVBaseValue = WorldFOV.value
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
    hook_func="WillowGame.WillowPlayerController:BeginSprint",
    hook_type=Type.POST,
)
def BeginSprint(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bIsSprinting
    bIsSprinting = True
    if __obj.pawn.OnGround == 1:
        __obj.DesiredFOV = (WorldFOV.value + SprintFOVModifier.value)

@hook(
    hook_func="WillowGame.WillowPlayerController:EndSprint",
    hook_type=Type.POST,
)
def EndSprint(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bIsSprinting
    bIsSprinting = False
    __obj.DesiredFOV = WorldFOV.value

@hook(
    hook_func="WillowGame.WillowPlayerPawn:PlayLanded",
    hook_type=Type.POST,
)
def Landed(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bIsSprinting
    if __obj.controller == get_pc():
        if bIsSprinting is True:
            __obj.controller.DesiredFOV = (WorldFOV.value + SprintFOVModifier.value)

@hook(
    hook_func="Engine.Pawn:DoJump",
    hook_type=Type.POST,
)
def DoJump(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bIsSprinting
    if __obj.controller == get_pc():
        if bKeepFOVInAir.value is False and __obj.Physics == 2:
            if bIsSprinting is True:
                __obj.controller.DesiredFOV = WorldFOV.value

@hook(
    hook_func="Engine.Pawn:Falling",
    hook_type=Type.POST,
)
def Falling(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bIsSprinting
    if __obj.controller == get_pc():
        if bKeepFOVInAir.value is False:
            if bIsSprinting is True:
                __obj.controller.DesiredFOV = WorldFOV.value
@hook(
    hook_func="WillowGame.WillowPlayerPawn:BerserkBegin.Tick",
    hook_type=Type.POST,
)
def BerserkEnter(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    if __obj.controller == get_pc():
        __obj.controller.DesiredFOV = (WorldFOV.value + 20)

@hook(
    hook_func="WillowGame.WillowPlayerPawn:BerserkEnd.Tick",
    hook_type=Type.POST,
)
def BerserkExit(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    if __obj.controller == get_pc():
        __obj.controller.DesiredFOV = WorldFOV.value

@hook(
    hook_func="WillowGame.PlayerBehavior_ToggleBerserk:ApplyBehaviorToContext",
    hook_type=Type.PRE,
)
def ToggleBerserk(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    pawn = get_pc().pawn
    if pawn.IsBerserk() is False:
        if pawn.controller == __args.ContextObject:
            pawn.controller.DesiredFOV = (WorldFOV.value + 20)

    else:
        if pawn.controller == __args.ContextObject:
            pawn.controller.DesiredFOV = WorldFOV.value






@hook(
    hook_func="WillowGame.WillowWeapon:ClientStartZoom",
    hook_type=Type.PRE,
)
def ClientStartZoom(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:

    StartFOV = 70.0000000

    if((obj.bFadeOnZoomBegin and int(obj.ZoomState) != int(1)) and int(obj.ZoomState) != int(2)):
    

        if((obj.WorldInfo.TimeSeconds - obj.ZoomFadeTime) < obj.DefinitionData.WeaponTypeDefinition.ZoomTime):
        
            obj.ZoomFadeTime = obj.WorldInfo.TimeSeconds - (obj.DefinitionData.WeaponTypeDefinition.ZoomTime - (obj.WorldInfo.TimeSeconds - obj.ZoomFadeTime))
        
        else:
        
            obj.ZoomFadeTime = obj.WorldInfo.TimeSeconds
        
    obj.SetZoomState(1)
    obj.ZoomedRate = obj.DefinitionData.WeaponTypeDefinition.ZoomedRate

    if((obj.Instigator != None) and obj.Instigator.IsLocallyControlled()):
    
        pc = obj.Instigator.Controller

        if(pc != None):
        
            pc.CurrentWanderAccuracy = 0.0000000
            StartFOV = pc.DesiredFOVBaseValue


    if bScaleADSFov.value is True:
        obj.ZoomedEndFOV = GetFOVScaled(obj.ZoomedEndFOVBaseValue, StartFOV)
    else:
        obj.ZoomedEndFOV = obj.ZoomedEndFOVBaseValue
    obj.ZoomedFOV = lerp(obj.Instigator.Controller.FOVAngle, obj.ZoomedEndFOV, obj.GetZoomEffect())

    return Block