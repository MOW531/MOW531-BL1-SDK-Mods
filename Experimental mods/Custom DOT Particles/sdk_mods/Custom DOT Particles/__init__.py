import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .statuseffects import UpdateDistributions


# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[],
    keybinds=[],
    hooks=[UpdateDistributions],
    commands=[],
    # Defaults to f"SETTINGS_DIR/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/CDP.json"),
)

logging.info(f"Custom DOT Particles Loaded: {__version__}, {__version_info__}")