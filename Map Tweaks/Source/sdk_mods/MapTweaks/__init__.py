from typing import Any #type:ignore
from mods_base import hook, build_mod, keybind, get_pc,BoolOption #type:ignore
from unrealsdk.hooks import Type, Block #type:ignore
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct #type:ignore
from .maps import Map

@hook("WillowGame.WillowGameInfo:PreCommitMapChange", Type.POST)
def FinalizedMapChange(obj:UObject, args:WrappedStruct, ret:Any, func:BoundFunction) -> Any:
    map_name = args.NextMapName
    #print(map_name)
    map_class = Map.registry.get(map_name)
    if map_class:
        map_class().on_map_loaded()


build_mod()