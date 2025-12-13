import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, ENGINE
from mods_base.options import BaseOption, BoolOption
from mods_base import SETTINGS_DIR
from mods_base import build_mod
from unrealsdk import logging
import os

from .inventory import InvStartCompare, InvChangeSelectedItemKey, InvChangeSelectedItemMouse, InvPrepCompare
from .vendor import VendorStartCompare, VendorChangeSelectedItemKey, VendorChangeSelectedItemMouse, VendorPrepCompare
from .bank import bankStartCompare, bankChangeSelectedItemMouse, bankPrepCompare, bankStopCompare
from .hud import PickupcardCompare, WeaponChanged, extEquippedCardOpened, SetCurrentWeapon, HUDClearVars
from .reward import DisplayRewardsPage



bPatched = False


def obj (definition:str, object:str):
    object_class = unrealsdk.find_class(definition)
    return ENGINE.DynamicLoadObject(object, object_class, False)

# Gets applied when a game starts
def patch():
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

    #EWO
    try:
        obj("InteractiveObjectDefinition","gd_Forgotten_Eridian_Ruins_Assets.VendingMachine.InteractiveObject.InteractiveObj_VendingMachine_EridianWeapons").ObjectFlags |= 0x4000
        obj("InteractiveObjectDefinition","gd_Forgotten_Eridian_Ruins_Assets.VendingMachine.InteractiveObject.InteractiveObj_VendingMachine_EridianWeapons").DefaultBehaviorSet.OnUsedBy[0].MovieDefinition = obj("VendingMachineGFxDefinition","menus_vending_MOD.Definitions.VendingMachineDefinition2")
        print("EWO Detected!")    
    except:
        print("EWO not Detected!")
        
    #Jakobs Vendor Fix
    try:
        obj("InteractiveObjectDefinition","ugy_fjv_itemgrades.VendingMachine.dlc1_InteractiveObj_VendingMachine_Jakobs").ObjectFlags |= 0x4000
        obj("InteractiveObjectDefinition","ugy_fjv_itemgrades.VendingMachine.dlc1_InteractiveObj_VendingMachine_Jakobs").ExtraBehaviorSets[1].OnUsedBy[0].MovieDefinition = obj("VendingMachineGFxDefinition","menus_vending_MOD.Definitions.VendingMachineDefinition2")
        print("Jakobs Vendor Fix Detected!")
    except:
        print("Jakobs Vendor Fix Not Detected!")

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






__version__: str
__version_info__: tuple[int, ...]

build_mod(
    keybinds=[],
    hooks=[on_startgame, InvStartCompare, InvChangeSelectedItemKey, InvChangeSelectedItemMouse, InvPrepCompare, VendorStartCompare, VendorChangeSelectedItemKey, VendorChangeSelectedItemMouse, VendorPrepCompare, bankStartCompare, bankChangeSelectedItemMouse, bankPrepCompare, bankStopCompare, PickupcardCompare, WeaponChanged, extEquippedCardOpened, SetCurrentWeapon, HUDClearVars, DisplayRewardsPage],
    commands=[],
)

