import unrealsdk #type: ignore
from unrealsdk import logging #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

MissionList = []
ActiveMission = None
current_obj = None
ActiveMissionLevel = None
OldActiveMission = None
TextColor = "#FFFFFF"

bTextColor = BoolOption("Text Color", True)

def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)

def GetTextColor():
    global TextColor
    global ActiveMissionLevel
    playerlevel = get_pc().pawn.GetExpLevel()
    if ActiveMissionLevel >= playerlevel + 5:
        TextColor = "#ea0e0e"
    elif ActiveMissionLevel >= playerlevel + 3:
        TextColor = "#fc9c0c"
    elif ActiveMissionLevel >= playerlevel + 1:
        TextColor = "#fcca01"
    elif ActiveMissionLevel >= playerlevel + -2:
        TextColor = "#14b766"
    else:
        TextColor = "#a2a2a2"

def GetMissionList():
    global MissionList
    MissionList.clear()
    for missions in unrealsdk.find_all("MissionTracker")[1].MissionList:
        MissionList.append(missions)

def GetMissionLevel():
    global ActiveMissionLevel
    mission_region = unrealsdk.find_all("MissionTracker")[1].ActiveMission.GameStageRegion
    DLCID = unrealsdk.find_all("MissionTracker")[1].ActiveMission.DlcPackageId
    ActiveMissionLevel = int(1)
    # Playthrough 1/2
    # Base Game
    if get_pc().GetCurrentPlaythrough() < 2:
        if DLCID == 0:
            for acts in obj("GlobalsDefinition","gd_globals.General.Globals").RegionBalanceData[get_pc().GetCurrentPlaythrough()].BalanceDefinitions:
                for regions in acts.BalanceByRegion:
                    if regions.Region == mission_region:
                        for overrides in regions.MissionOverrides:
                            if get_pc().IsMissionInStatus(overrides.Mission, 4) is True:
                                ActiveMissionLevel = int(overrides.GameStage.BaseValueConstant)
                                GetTextColor()
                                return
                        ActiveMissionLevel = int(regions.DefaultGameStage.BaseValueConstant)
        # DLC 1
        elif DLCID == 1:
            for acts in obj("GlobalsDefinition","dlc1_PackageDefinition.CustomGlobals").RegionBalanceData[get_pc().GetCurrentPlaythrough()].BalanceDefinitions:
                for regions in acts.BalanceByRegion:
                    if regions.Region == mission_region:
                        for overrides in regions.MissionOverrides:
                            if get_pc().IsMissionInStatus(overrides.Mission, 4) is True:
                                ActiveMissionLevel = int(overrides.GameStage.BaseValueConstant)
                                GetTextColor()
                                return
                        ActiveMissionLevel = int(regions.DefaultGameStage.BaseValueConstant)
        # DLC 2
        elif DLCID == 2:
            for acts in obj("GlobalsDefinition","dlc2_packagedefinition.CustomGlobals").RegionBalanceData[get_pc().GetCurrentPlaythrough()].BalanceDefinitions:
                for regions in acts.BalanceByRegion:
                    if regions.Region == mission_region:
                        for overrides in regions.MissionOverrides:
                            if get_pc().IsMissionInStatus(overrides.Mission, 4) is True:
                                ActiveMissionLevel = int(overrides.GameStage.BaseValueConstant)
                                GetTextColor()
                                return
                        ActiveMissionLevel = int(regions.DefaultGameStage.BaseValueConstant)
        # DLC 3
        elif DLCID == 4:
            for acts in obj("GlobalsDefinition","dlc3_PackageDefinition.CustomGlobals").RegionBalanceData[get_pc().GetCurrentPlaythrough()].BalanceDefinitions:
                for regions in acts.BalanceByRegion:
                    if regions.Region == mission_region:
                        for overrides in regions.MissionOverrides:
                            if get_pc().IsMissionInStatus(overrides.Mission, 4) is True:
                                ActiveMissionLevel = int(overrides.GameStage.BaseValueConstant)
                                GetTextColor()
                                return
                        ActiveMissionLevel = int(regions.DefaultGameStage.BaseValueConstant)
        # DLC 4
        elif DLCID == 8:
            for acts in obj("GlobalsDefinition","dlc4_PackageDefinition.CustomGlobals").RegionBalanceData[get_pc().GetCurrentPlaythrough()].BalanceDefinitions:
                for regions in acts.BalanceByRegion:
                    if regions.Region == mission_region:
                        for overrides in regions.MissionOverrides:
                            if get_pc().IsMissionInStatus(overrides.Mission, 4) is True:
                                ActiveMissionLevel = int(overrides.GameStage.BaseValueConstant)
                                GetTextColor()
                                return
                        ActiveMissionLevel = int(regions.DefaultGameStage.BaseValueConstant)
    # Playthrough 3
    elif get_pc().GetCurrentPlaythrough() == 2:
        ActiveMissionLevel = obj("GlobalsDefinition","gd_globals.General.Globals").RegionBalanceData[2].BalanceDefinitions[1].BalanceByRegion[0].DefaultGameStage.BaseValueAttribute.ValueResolverChain[0].ConstantValue
    GetTextColor()


def notify():
    global OldActiveMission
    global TextColor
    global ActiveMission
    if OldActiveMission != unrealsdk.find_all("MissionTracker")[1].ActiveMission:
        if bTextColor.value is True:
            GetMissionLevel()
        else:
            TextColor = "#FFFFFF"
        get_pc().myHUD.GetHUDMovie().AddCriticalText(0, 'Mission selected: "<font color = \"' + TextColor + '\">' + MissionList[ActiveMission].MissionName + '</font>"', 1.5, get_pc().myHUD.WhiteColor, get_pc().myHUD.WPRI)
        unrealsdk.find_all("WillowUIScene")[0].PlaySound(unrealsdk.find_object("SoundCue","Interface.User_Interface.UI_SelectCue"))

@keybind(identifier="Next Mission", key="F2", event_filter=EInputEvent.IE_Pressed)
def NextMission():
    global OldActiveMission
    global ActiveMission
    global MissionList
    if len(unrealsdk.find_all("MissionTracker")) > 1:
        GetMissionList()
        OldActiveMission = unrealsdk.find_all("MissionTracker")[1].ActiveMission
        ActiveMission = MissionList.index(unrealsdk.find_all("MissionTracker")[1].ActiveMission)
        ActiveMission = ActiveMission + 1
        if ActiveMission > len(MissionList) - 1:
            ActiveMission = 0
        get_pc().SetActiveMission(MissionList[ActiveMission])
        unrealsdk.find_all("MissionTracker")[1].ActiveMission = MissionList[ActiveMission]
        notify()

@keybind(identifier="Previous Mission", key="F1", event_filter=EInputEvent.IE_Pressed)
def PrevMission():
    global OldActiveMission
    global ActiveMission
    global MissionList
    if len(unrealsdk.find_all("MissionTracker")) > 1:
        GetMissionList()
        OldActiveMission = unrealsdk.find_all("MissionTracker")[1].ActiveMission
        ActiveMission = MissionList.index(unrealsdk.find_all("MissionTracker")[1].ActiveMission)
        ActiveMission = ActiveMission - 1
        if ActiveMission < 0:
            ActiveMission = len(MissionList) - 1
        get_pc().SetActiveMission(MissionList[ActiveMission])
        unrealsdk.find_all("MissionTracker")[1].ActiveMission = MissionList[ActiveMission]
        notify()




# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[bTextColor],
    keybinds=[NextMission, PrevMission],
    hooks=[],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/MissionSelector.json"),
)

logging.info(f"Mission Selector Loaded: {__version__}, {__version_info__}")