import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .inventory import InvStartCompare, InvChangeSelectedItemKey, InvChangeSelectedItemMouse, InvPrepCompare
from .hud import PickupcardCompare, WeaponChanged, extEquippedCardOpened, SetCurrentWeapon, HUDClearVars
from .vendor import VendorStartCompare, VendorChangeSelectedItemKey, VendorChangeSelectedItemMouse, VendorPrepCompare
from .bank import bankStartCompare, bankChangeSelectedItemMouse, bankPrepCompare, bankStopCompare
from .reward import DisplayRewardsPage
from .functions import FontSize, ShowParts, ShowElementText

bPatched = False

def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)


def patch():

    obj("ItemDefinition","gd_shields.A_Item.Item_Shield").ObjectFlags |= 0x4000
    obj("ItemDefinition","gd_shields.A_Item.Item_Shield").UIStats[2].Attribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldOnIdleRegenerationDelay")

    obj("AttributePresentationDefinition","gd_AttributePresentation.Shields.AttrPresent_ShieldOnIdleRegenerationDelay").ObjectFlags |= 0x4000
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

    #EWO
    try:
        obj("ItemDefinition","Eridian_Weapons_Overhaul_Shields.A_Item.Item_Eridian_Shield").ObjectFlags |= 0x4000
        obj("ItemDefinition","Eridian_Weapons_Overhaul_Shields.A_Item.Item_Eridian_Shield_Barrier").ObjectFlags |= 0x4000
        obj("ItemDefinition","Eridian_Weapons_Overhaul_Shields.A_Item.Item_Eridian_Shield_Fire").ObjectFlags |= 0x4000
        obj("ItemDefinition","Eridian_Weapons_Overhaul_Shields.A_Item.Item_Eridian_Shield_Flesh").ObjectFlags |= 0x4000
        obj("ItemDefinition","Eridian_Weapons_Overhaul_Shields.A_Item.Item_Eridian_Shield").UIStats[2].Attribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldOnIdleRegenerationDelay")
        obj("ItemDefinition","Eridian_Weapons_Overhaul_Shields.A_Item.Item_Eridian_Shield_Barrier").UIStats[2].Attribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldOnIdleRegenerationDelay")
        obj("ItemDefinition","Eridian_Weapons_Overhaul_Shields.A_Item.Item_Eridian_Shield_Fire").UIStats[2].Attribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldOnIdleRegenerationDelay")
        obj("ItemDefinition","Eridian_Weapons_Overhaul_Shields.A_Item.Item_Eridian_Shield_Flesh").UIStats[2].Attribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldOnIdleRegenerationDelay")

        obj("InteractiveObjectDefinition","gd_Forgotten_Eridian_Ruins_Assets.VendingMachine.InteractiveObject.InteractiveObj_VendingMachine_EridianWeapons").ObjectFlags |= 0x4000
        obj("InteractiveObjectDefinition","gd_Forgotten_Eridian_Ruins_Assets.VendingMachine.InteractiveObject.InteractiveObj_VendingMachine_EridianWeapons").DefaultBehaviorSet.OnUsedBy[0].MovieDefinition = obj("VendingMachineGFxDefinition","menus_vending_MOD.Definitions.VendingMachineDefinition2")
        
        obj("BehaviorCollectionDefinition","Eridian_Weapons_Overhaul_Grenades.BehaviorCollections.BC_Energy_Generic").ObjectFlags |= 0x4000
        obj("BehaviorCollectionDefinition","Eridian_Weapons_Overhaul_Grenades.BehaviorCollections.BC_Energy_Generic").Behaviors[1].InstanceData[0].Float = 21

        obj("BehaviorCollectionDefinition","Eridian_Weapons_Overhaul_Shields.Behaviors.BehaviorCol_ShieldIcon_Energy").ObjectFlags |= 0x4000
        obj("BehaviorCollectionDefinition","Eridian_Weapons_Overhaul_Shields.Behaviors.BehaviorCol_ShieldIcon_Energy").Behaviors[0].InstanceData[0].Float = 21
        
        print("EWO Detected!")
    except:
        print("EWO Not Detected!")

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

# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[FontSize, ShowParts, ShowElementText],
    keybinds=[],
    hooks=[on_startgame, InvChangeSelectedItemKey, InvChangeSelectedItemMouse, InvStartCompare, InvPrepCompare, HUDClearVars, PickupcardCompare, WeaponChanged, extEquippedCardOpened, SetCurrentWeapon, VendorStartCompare, VendorChangeSelectedItemKey, VendorChangeSelectedItemMouse, VendorPrepCompare, bankStartCompare, bankChangeSelectedItemMouse, bankPrepCompare, bankStopCompare, DisplayRewardsPage],
    commands=[],
    # Defaults to f"SETTINGS_DIR/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"SETTINGS_DIR/EIC.json"),
)

logging.info(f"Extended Item Cards Loaded: {__version__}, {__version_info__}")