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

def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)


def patch():

    obj("ItemDefinition","gd_shields.A_Item.Item_Shield").UIStats[2].Attribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldOnIdleRegenerationDelay")

    obj("AttributePresentationDefinition","gd_AttributePresentation.Shields.AttrPresent_ShieldOnIdleRegenerationDelay").RoundingMode = 0

    # UI
        # KeepAlive

    obj("VendingMachineGFxDefinition","menus_vending.Definitions.VendingMachineDefinition").ObjectFlags |= 0x4000
    obj("QuestAcceptGFxMovie","menus_mission.FlashInstances.mission_interface_instance").ObjectFlags |= 0x4000
    obj("EchoQuestAcceptGFxMovie","menus_mission.FlashMovies.mission_interface_instance_echo").ObjectFlags |= 0x4000
    obj("BankGFxMovie","menus_bank.FlashInstances.bank_instance").ObjectFlags |= 0x4000


    obj("StatusMenuExGFxMovie","menus_ingame_redux.FlashInstances.status_menu_instance").MovieInfo = obj("GFxMovieInfo","menus_ingame_redux_MOD.FlashMovies.status_menu")
    obj("ItemPickupGFxMovie","inworld_ui.weapon_card.weapon_card_INST").MovieInfo = obj("GFxMovieInfo","inworld_ui_MOD.weapon_card.weapon_card")
    obj("BankGFxMovie","menus_bank.FlashInstances.bank_instance").MovieInfo = obj("GFxMovieInfo","menus_bank_MOD.FlashMovies.bank")
    obj("VendingMachineGFxDefinition","menus_vending.Definitions.VendingMachineDefinition").Movie = obj("VendingMachineGFxMovie","menus_vending_MOD.FlashInstances.vending_machine_1")
    obj("QuestAcceptGFxMovie","menus_mission.FlashInstances.mission_interface_instance").MovieInfo = obj("GFxMovieInfo","menus_mission_MOD.FlashMovies.mission_interface")
    obj("EchoQuestAcceptGFxMovie","menus_mission.FlashMovies.mission_interface_instance_echo").MovieInfo = obj("GFxMovieInfo","menus_mission_MOD.FlashMovies.mission_interface")
    obj("WillowHUDGFxMovie","GfxHUD.FlashInstances.hud_instance").MovieInfo = obj("GFxMovieInfo","GfxHUD_MOD.FlashMovie.HUD")



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
    settings_file=Path(f"{SETTINGS_DIR}/ShieldStatsSDK.json"),
)

logging.info(f"Shield Stats SDK Loaded: {__version__}, {__version_info__}")
