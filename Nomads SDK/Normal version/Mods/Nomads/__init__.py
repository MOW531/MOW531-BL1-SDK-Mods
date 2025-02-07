import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc 
from mods_base.options import BaseOption, BoolOption
from mods_base import SETTINGS_DIR
from mods_base import build_mod
from unrealsdk import logging
import os

bPatched = False
bPatched_volatile = False
Count = 0
current_obj = None

struct = unrealsdk.make_struct
wclass = unrealsdk.find_class


def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    #unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)



def patch_volatile():


# Enemies

    # Normal Nomad
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList.append(obj("PopulationDefinition","Char_Nomad.nomad.nomad_pop").ActorArchetypeList[0])
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].Probability.BaseValueScaleConstant = 0.5
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].Probability.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.WeightingPlayerCount.Enemy_Upgrade_PerPlayer")
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].MaxActiveAtOneTime.BaseValueConstant = 2.0

    # Heavy Nomad
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList.append(obj("PopulationDefinition","Char_Nomad_Heavy.nomad.nomad_Heavy_pop").ActorArchetypeList[0])
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].Probability.BaseValueScaleConstant = 0.5
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].Probability.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.WeightingPlayerCount.Enemy_Upgrade_PerPlayer")
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].MaxActiveAtOneTime.BaseValueConstant = 2.0

    # Taskmaster Nomad
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList.append(obj("PopulationDefinition","Char_Nomad_Taskmaster.nomad.nomad_Taskmaster_pop").ActorArchetypeList[0])
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].Probability.BaseValueScaleConstant = 0.5
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].Probability.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.WeightingPlayerCount.Enemy_Upgrade_PerPlayer")
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].MaxActiveAtOneTime.BaseValueConstant = 2.0

    # Super Nomad
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList.append(obj("PopulationDefinition","Char_Nomad_Super.nomad.Nomad_Super_pop").ActorArchetypeList[0])
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].Probability.BaseValueScaleConstant = 0.08
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].Probability.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.WeightingPlayerCount.Enemy_MajorUpgrade_PerPlayer")
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_Mixture").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].MaxActiveAtOneTime.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.WeightingPlayerCount.Bosses_PerPlayers")

 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_BadassBandits").ActorArchetypeList.append(obj("PopulationDefinition","Char_Nomad_Super.nomad.Nomad_Super_pop").ActorArchetypeList[0])
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_BadassBandits").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].MaxActiveAtOneTime.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.WeightingPlayerCount.Bosses_PerPlayers")
 obj("PopulationDefinition","gd_population_enemies.Bandits.BanditSquad_BadassBandits").ActorArchetypeList[len(current_obj.ActorArchetypeList) - 1].MaxActiveAtOneTime.BaseValueConstant = 0

@hook(
    hook_func="Engine.WorldInfo:CommitMapChange",
    hook_type=Type.POST,
)
def on_commit_map_change(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched_volatile
    bPatched_volatile = False

@hook(
    hook_func="Engine.WorldInfo:PostBeginPlay",
    hook_type=Type.POST,
)
def on_level_loaded(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched_volatile
    global Count
    if Count >= 2:
        Count = 0
        if bPatched_volatile is False:
            patch_volatile()
            bPatched_volatile = True
    else:
        Count = Count + 1

@hook(
    hook_func="Engine.WorldInfo:IsMenuLevel",
    hook_type=Type.PRE,
)
def on_startgame(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    patch_volatile()






# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    keybinds=[],
    hooks=[on_level_loaded, on_commit_map_change, on_startgame],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/NomadsSDK.json"),
)

logging.info(f"Nomads SDK Loaded: {__version__}, {__version_info__}")
