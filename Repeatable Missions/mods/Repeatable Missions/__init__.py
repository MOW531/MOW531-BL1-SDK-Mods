import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc 
from mods_base import SETTINGS_DIR
from mods_base import build_mod
from unrealsdk import logging


def RepeatMission(mission_package:str):
    pc = get_pc()
    unrealsdk.load_package(mission_package)
    mission = unrealsdk.find_object("MissionDefinition", mission_package)
    missionindex = pc.GetMissionIndexForMission(mission)
    MissionList = pc.MissionPlaythroughData[get_pc().GetCurrentPlaythrough()].MissionList
    if pc.IsMissionInStatus(mission, 4) == True:
        pc.SetMissionStatus(missionindex, 0)
        MissionList.pop(missionindex)

def RepeatCoDMissionChain():
    pc = get_pc()
    unrealsdk.load_package("Z0_Missions.Missions.M_CircleOfDeath01")
    unrealsdk.load_package("Z0_Missions.Missions.M_CircleOfDeath02")
    unrealsdk.load_package("Z0_Missions.Missions.M_CircleOfDeath03")
    mission_1 = unrealsdk.find_object("MissionDefinition", "Z0_Missions.Missions.M_CircleOfDeath01")
    mission_2 = unrealsdk.find_object("MissionDefinition", "Z0_Missions.Missions.M_CircleOfDeath02")
    mission_3 = unrealsdk.find_object("MissionDefinition", "Z0_Missions.Missions.M_CircleOfDeath03")
    MissionList = pc.MissionPlaythroughData[get_pc().GetCurrentPlaythrough()].MissionList
    if pc.IsMissionInStatus(mission_3, 4) == True:
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_3), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_3))
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_2), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_2))
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_1), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_1))


def RepeatCoSMissionChain():
    pc = get_pc()
    unrealsdk.load_package("Z1_Missions.Missions.M_SlaughterWave1")
    unrealsdk.load_package("Z1_Missions.Missions.M_SlaughterWave2")
    unrealsdk.load_package("Z1_Missions.Missions.M_SlaughterWave3")
    mission_1 = unrealsdk.find_object("MissionDefinition", "Z1_Missions.Missions.M_SlaughterWave1")
    mission_2 = unrealsdk.find_object("MissionDefinition", "Z1_Missions.Missions.M_SlaughterWave2")
    mission_3 = unrealsdk.find_object("MissionDefinition", "Z1_Missions.Missions.M_SlaughterWave3")
    MissionList = pc.MissionPlaythroughData[get_pc().GetCurrentPlaythrough()].MissionList
    if pc.IsMissionInStatus(mission_3, 4) == True:
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_3), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_3))
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_2), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_2))
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_1), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_1))

def RepeatDLCCoDMissionChain():
    pc = get_pc()
    unrealsdk.load_package("dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave1")
    unrealsdk.load_package("dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave2")
    unrealsdk.load_package("dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave3")
    unrealsdk.load_package("dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave4")
    unrealsdk.load_package("dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave5")
    mission_1 = unrealsdk.find_object("MissionDefinition", "dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave1")
    mission_2 = unrealsdk.find_object("MissionDefinition", "dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave2")
    mission_3 = unrealsdk.find_object("MissionDefinition", "dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave3")
    mission_4 = unrealsdk.find_object("MissionDefinition", "dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave4")
    mission_5 = unrealsdk.find_object("MissionDefinition", "dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave5")
    MissionList = pc.MissionPlaythroughData[get_pc().GetCurrentPlaythrough()].MissionList
    if pc.IsMissionInStatus(mission_5, 4) == True:
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_5), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_5))
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_4), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_4))
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_3), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_3))
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_2), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_2))
        pc.SetMissionStatus(pc.GetMissionIndexForMission(mission_1), 0)
        MissionList.pop(pc.GetMissionIndexForMission(mission_1))

def missions():
    RepeatCoSMissionChain()
    RepeatCoDMissionChain()
    RepeatDLCCoDMissionChain()
    RepeatMission("dlc3_SideMissions.SideMissions.M_dlc3_GetLoot03")

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
    missions()


@hook(
    hook_func="WillowGame.MissionTracker:GlobalCompleteMission",
    hook_type=Type.POST,
)
def on_mission_completion(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    missions()

# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    keybinds=[],
    hooks=[on_player_loaded, on_mission_completion],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/Repeatable_Missions.json"),
)

logging.info(f"Repeatable Missions Loaded: {__version__}, {__version_info__}")
