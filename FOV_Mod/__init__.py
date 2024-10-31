from pathlib import Path
from mods_base import SETTINGS_DIR, build_mod
from unrealsdk import logging
from mods_base.options import BaseOption, SliderOption


from .hooks import on_player_loaded, on_player_leave_car, on_player_enter_car, on_player_weapon_action, fov_setting, revolver_pistol_fov_setting, repeater_pistol_setting, machine_pistol_setting, assault_shotgun_setting, combat_shotgun_setting, combat_rifle_setting, grenade_launcher_setting, rocket_launcher_setting, sniper_rifle_setting, sniper_rifle_semiauto_setting, support_machinegun_setting, patrol_smg_setting, alien_setting


# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]


build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[fov_setting, revolver_pistol_fov_setting, repeater_pistol_setting, machine_pistol_setting, assault_shotgun_setting, combat_shotgun_setting, combat_rifle_setting, grenade_launcher_setting, rocket_launcher_setting, sniper_rifle_setting, sniper_rifle_semiauto_setting, support_machinegun_setting, patrol_smg_setting, alien_setting],
    keybinds=[],
    hooks=[on_player_loaded, on_player_leave_car, on_player_enter_car, on_player_weapon_action],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/FOV.json"),
)

logging.info(f"FOV Mod Loaded: {__version__}, {__version_info__}")
