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
current_obj = None

struct = unrealsdk.make_struct
wclass = unrealsdk.find_class


def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)


def patch():

 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Assault_Rifle_Bullets").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Combat_Shotgun_Shells").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Grenade_Protean").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Patrol_SMG_Clip").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Repeater_Pistol_Clip").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Revolver_Pistol_Rounds").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Rocket_Launcher").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Sniper_Rifle_Cartridges").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_currency.A_Item.Bobblehead").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_currency.A_Item.Currency").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_currency.A_Item.Currency_big").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_currency.A_Item.SkagPearl").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_1").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_2").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_3").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_4").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_5").bAutomaticallyPickup = True


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
    hooks=[on_startgame],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/AutoPickupSDK.json"),
)

logging.info(f"Auto-Pickup SDK Loaded: {__version__}, {__version_info__}")
