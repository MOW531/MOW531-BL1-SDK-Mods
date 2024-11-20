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

struct = unrealsdk.make_struct


def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)


def patch():
    a=1

def patch_volatile():

    # Itempools

        # Shops
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine").BalancedItems.append(current_obj.BalancedItems[9])
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_Weapons_flatChance").BalancedItems.append(current_obj.BalancedItems[9])
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_Weapons_flatChance").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

        # NineToes
    obj("ItemPoolDefinition","gd_itempools_custom.CustomWeapons.Weapons_NineToes").BalancedItems.append(current_obj.BalancedItems[0])
    obj("ItemPoolDefinition","gd_itempools_custom.CustomWeapons.Weapons_NineToes").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_customweapons.Weapons.CustomWeap_GrenadeLauncher_NineToes_BigToe")
    obj("InventoryBalanceDefinition","gd_customweapons.Weapons.CustomWeap_GrenadeLauncher_NineToes_BigToe").Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage = 1
    obj("InventoryBalanceDefinition","gd_customweapons.Weapons.CustomWeap_GrenadeLauncher_NineToes_BigToe").Manufacturers[0].Grades[0].GameStageRequirement.MaxGameStage = 15


        # Enemies
    obj("ItemPoolDefinition","gd_itempools.Bandits.Heavy_Badass_Weapons").BalancedItems.append(current_obj.BalancedItems[2])
    obj("ItemPoolDefinition","gd_itempools.Bandits.Heavy_Badass_Weapons").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

    obj("ItemPoolDefinition","gd_itempools.Bandits.Heavy_Weapons").BalancedItems.append(current_obj.BalancedItems[3])
    obj("ItemPoolDefinition","gd_itempools.Bandits.Heavy_Weapons").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

    obj("ItemPoolDefinition","gd_itempools.CrimsonLance.Infantry_Weapons").BalancedItems.append(current_obj.BalancedItems[3])
    obj("ItemPoolDefinition","gd_itempools.CrimsonLance.Infantry_Weapons").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

    obj("ItemPoolDefinition","gd_itempools.CrimsonLance.Infantry_Weapons_Badass").BalancedItems.append(current_obj.BalancedItems[2])
    obj("ItemPoolDefinition","gd_itempools.CrimsonLance.Infantry_Weapons_Badass").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

    obj("ItemPoolDefinition","dlc3_gd_itempools.CrimsonLance.Infantry_Weapons_Badass_enhance").BalancedItems.append(current_obj.BalancedItems[2])
    obj("ItemPoolDefinition","dlc3_gd_itempools.CrimsonLance.Infantry_Weapons_Badass_enhance").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

    obj("ItemPoolDefinition","dlc3_gd_itempools.CrimsonLance.Rocket_Badass_Weapons_enhance").BalancedItems.append(current_obj.BalancedItems[0])
    obj("ItemPoolDefinition","dlc3_gd_itempools.CrimsonLance.Rocket_Badass_Weapons_enhance").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")


        # General
    obj("ItemPoolDefinition","gd_itempools.WeaponPools.Weapons_All").BalancedItems.append(current_obj.BalancedItems[5])
    obj("ItemPoolDefinition","gd_itempools.WeaponPools.Weapons_All").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

    obj("ItemPoolDefinition","gd_itempools.WeaponPools.Weapons_Launchers").BalancedItems.append(current_obj.BalancedItems[1])
    obj("ItemPoolDefinition","gd_itempools.WeaponPools.Weapons_Launchers").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

    obj("ItemPoolDefinition","gd_itempools.Treasure_ChestPools.Chest_Weapons_Launchers").BalancedItems.append(current_obj.BalancedItems[0])
    obj("ItemPoolDefinition","gd_itempools.Treasure_ChestPools.Chest_Weapons_Launchers").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

    obj("ItemPoolDefinition","gd_itempools.CustomPools.WeaponsFor_Brick").BalancedItems.append(current_obj.BalancedItems[2])
    obj("ItemPoolDefinition","gd_itempools.CustomPools.WeaponsFor_Brick").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")

    obj("ItemPoolDefinition","dlc3_gd_itempools.Treasure_ChestPools.Chest_Weapons_Launchers_enhance").BalancedItems.append(current_obj.BalancedItems[0])
    obj("ItemPoolDefinition","dlc3_gd_itempools.Treasure_ChestPools.Chest_Weapons_Launchers_enhance").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade")



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
    hooks=[on_level_loaded, on_commit_map_change],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/GrenadeLaunchersSDK.json"),
)

logging.info(f"Grenade Launchers SDK Loaded: {__version__}, {__version_info__}")
