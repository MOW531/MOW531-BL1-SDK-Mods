import unrealsdk #type: ignore
from unrealsdk import logging #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

MissionList = []
ActiveMission = None

def GetMissionList():
    global MissionList
    MissionList.clear()
    for missions in unrealsdk.find_all("MissionTracker")[1].MissionList:
        MissionList.append(missions)

@keybind(identifier="Next Mission", key="F2", event_filter=EInputEvent.IE_Pressed)
def NextMission():
    global ActiveMission
    global MissionList
    if len(unrealsdk.find_all("MissionTracker")) > 1:
        GetMissionList()
        ActiveMission = MissionList.index(unrealsdk.find_all("MissionTracker")[1].ActiveMission)
        ActiveMission = ActiveMission + 1
        if ActiveMission > len(MissionList) - 1:
            ActiveMission = 0
        get_pc().SetActiveMission(MissionList[ActiveMission])
        unrealsdk.find_all("MissionTracker")[1].ActiveMission = MissionList[ActiveMission]


@keybind(identifier="Previous Mission", key="F1", event_filter=EInputEvent.IE_Pressed)
def PrevMission():
    global ActiveMission
    global MissionList
    if len(unrealsdk.find_all("MissionTracker")) > 1:
        GetMissionList()
        ActiveMission = MissionList.index(unrealsdk.find_all("MissionTracker")[1].ActiveMission)
        ActiveMission = ActiveMission - 1
        if ActiveMission < 0:
            ActiveMission = len(MissionList) - 1
        get_pc().SetActiveMission(MissionList[ActiveMission])
        unrealsdk.find_all("MissionTracker")[1].ActiveMission = MissionList[ActiveMission]



# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    keybinds=[NextMission, PrevMission],
    hooks=[],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/MissionSelector.json"),
)

logging.info(f"Mission Selector Loaded: {__version__}, {__version_info__}")