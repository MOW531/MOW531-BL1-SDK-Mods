import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, SETTINGS_DIR, build_mod, ENGINE
from mods_base.options import BaseOption, BoolOption
from unrealsdk import logging, make_struct, find_class

def DisableCameraRotation(option:BaseOption, value:bool):
    InjuredDef = unrealsdk.find_object("object","gd_PlayerShared.injured.PlayerInjuredDefinition")
    if value is True:
        InjuredDef.InjuredRotationLimit.roll = 0
        InjuredDef.InjuredRotationLean.pitch = 0
        InjuredDef.InjuredRotationLean.yaw = 0

    else:
        InjuredDef.InjuredRotationLimit.roll = 3640
        InjuredDef.InjuredRotationLean.pitch = 91
        InjuredDef.InjuredRotationLean.yaw = 1820
    
    if get_pc() is not None and get_pc().pawn is not None:
        get_pc().pawn.SetupPlayerInjuredState()

bDisableCameraRotation = BoolOption("Disables Auto-Rotation", True, on_change=DisableCameraRotation)



@hook(
    hook_func="WillowGame.WillowPawn:injured.SwitchToSidearm",
    hook_type=Type.POST,
)
def injured(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    obj.AccelRate = 2048
    obj.GroundSpeed = 150

@hook(
    hook_func="WillowGame.WillowPawn:GoFromInjuredToHealthyClient",
    hook_type=Type.POST,
)
def GoFromInjuredToHealthyClient(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    obj.GroundSpeed = 440

@hook(
    hook_func="WillowGame.WillowPawn:GoFromInjuredToHealthy",
    hook_type=Type.POST,
)
def GoFromInjuredToHealthy(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    obj.GroundSpeed = 440


# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    keybinds=[],
    hooks=[injured, GoFromInjuredToHealthyClient, GoFromInjuredToHealthy],
    commands=[],
)