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

bPatched_volatile = False
Count = 0

blacklist = ["InventoryBalanceDefinition'gd_itemgrades.Weapons.ItemGrade_Weapon_Scorpio'","InventoryBalanceDefinition'gd_turrets.gatling.Weapons.ItemGrade_Turret_Gatling'","InventoryBalanceDefinition'gd_turrets.Grenade.Weapons.ItemGrade_Turret_Grenade'","InventoryBalanceDefinition'gd_turrets.rocket.Weapons.ItemGrade_Turret_Rocket'"]


def obj (definition:str, object:str):
    object_class = unrealsdk.find_class(definition)
    current_obj = ENGINE.DynamicLoadObject(object, object_class, False)
    current_obj.ObjectFlags |= 0x4000
    return current_obj

def ReplaceStock(StockBalance):

    if StockBalance == obj("InventoryBalanceDefinition","gd_itemgrades.Gear.ItemGrade_Gear_GrenadeMODs_Stock"):
        return obj("InventoryBalanceDefinition","gd_itemgrades.Gear.ItemGrade_Gear_GrenadeMODs")

    elif StockBalance == obj("InventoryBalanceDefinition","gd_itemgrades.Gear.ItemGrade_Gear_Shield_Stock"):
        return obj("InventoryBalanceDefinition","gd_itemgrades.Gear.ItemGrade_Gear_Shield")

    elif StockBalance == obj("InventoryBalanceDefinition","gd_itemgrades.Weapons_Stock.ItemGrade_Stock_CombatShotgun"):
        return obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_CombatShotgun")

    elif StockBalance == obj("InventoryBalanceDefinition","gd_itemgrades.Weapons_Stock.ItemGrade_Stock_MachinePistol"):
        return obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_MachinePistol")

    elif StockBalance == obj("InventoryBalanceDefinition","gd_itemgrades.Weapons_Stock.ItemGrade_Stock_RepeaterPistol"):
        return obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_RepeaterPistol")

    elif StockBalance == obj("InventoryBalanceDefinition","gd_itemgrades.Weapons_Stock.ItemGrade_Stock_SMG"):
        return obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_PatrolSMG")

    elif StockBalance == obj("InventoryBalanceDefinition","gd_itemgrades.Weapons_Stock.ItemGrade_Stock_SupportMG"):
        return obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_SupportMachineGun")

    elif StockBalance == obj("InventoryBalanceDefinition","dlc3_gd_itemgrades.Weapons_Stock.ItemGrade_Stock_CombatRifle"):
        return obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_CombatRifle")

    else:
        return StockBalance




def SetLoot():
    global blacklist
    for itempool in unrealsdk.find_all("ItemPoolDefinition"):
        if "WillowGame.Default" not in str(itempool):
            for itembalance in itempool.BalancedItems:
                if str(itembalance.InvBalanceDefinition) not in blacklist:
                    itembalance.bDropOnDeath = True
                    itembalance.InvBalanceDefinition = ReplaceStock(itembalance.InvBalanceDefinition)

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
            SetLoot()
    else:
        Count = Count + 1



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
    settings_file=Path(f"{SETTINGS_DIR}/LegitLoot.json"),
)

logging.info(f"Legit Loot SDK Loaded: {__version__}, {__version_info__}")
