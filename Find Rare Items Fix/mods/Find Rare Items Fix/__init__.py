from pathlib import Path
from mods_base import SETTINGS_DIR, build_mod
from unrealsdk import logging
from mods_base.options import BaseOption, SliderOption


from .hooks import on_container_open, on_enemy_spawn


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
    hooks=[on_container_open, on_enemy_spawn],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/Find_Rare_Items_Fix.json"),
)

logging.info(f"Find Rare Items Fix Loaded: {__version__}, {__version_info__}")
