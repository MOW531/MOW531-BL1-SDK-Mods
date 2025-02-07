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

TEXT_MOD_FOLDER = "./Mods/BadTextModLoader/TextMods/"

setcommands = []
rsetcommands = []
bPatched = False
bPatched_volatile = False
Count = 0
current_obj = None

def patch():
    for x in setcommands:
        exec(x)

def patch_volatile():
    for x in rsetcommands:
        exec(x)



def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)

def remove_first_word(s): 
    # Split the string into words 
    words = s.split() 
    # Join the words back together, excluding the first one 
    return ' '.join(words[1:]) 

def process_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            commandtype = line.strip().split()
            if line.strip():
                if commandtype[0] == "set":
                    command = remove_first_word(line.strip())
                    setcommands.append(command)
                elif commandtype[0] == "rset":
                    command = remove_first_word(line.strip())
                    rsetcommands.append(command)

def prep():
    for filename in os.listdir(TEXT_MOD_FOLDER):
        filepath = os.path.join(TEXT_MOD_FOLDER, filename)
        if os.path.isfile(filepath):
            process_file(filepath)




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
        if bPatched_volatile != True:
            bPatched_volatile = True
            patch_volatile()
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
    global bPatched
    if bPatched is False:
        bPatched = True
        prep()
        patch()






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
    settings_file=Path(f"{SETTINGS_DIR}/BadTextModLoader.json"),
)

logging.info(f"Bad Text Mod Loader Loaded: {__version__}, {__version_info__}")
