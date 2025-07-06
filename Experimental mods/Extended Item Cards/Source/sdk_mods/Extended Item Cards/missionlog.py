import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

bPlotIcon = BoolOption("Story mission indicator", True)

def FindPlotCriticalMissions(log):
    pc = get_pc()
    global PlotList
    CurrentPlaythrough = pc.GetCurrentPlaythrough()
    for mission in pc.MissionPlaythroughData[CurrentPlaythrough].MissionList:
        if mission.MissionDef.bPlotCritical is True:
            Icon = ""
            Idx = mission.Status
            if Idx == 0:
                Icon = "new_plot"
            elif Idx == 1:
                Icon = "inprogress_plot"
            elif Idx == 2:
                Icon = "turnin_plot"
            elif Idx == 3:
                Icon = "complete_plot"
            if Icon != "":
                log.MissionLogTextList.SetIconOverrideFor(mission.MissionDef,Icon)


@hook(
    hook_func="WillowGame.StatusMenuExGFxMovie:UpdateMissionDetails",
    hook_type=Type.POST,
)
def UpdateMissionDetails(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    if bPlotIcon.value is True:
        FindPlotCriticalMissions(obj)