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
wclass = unrealsdk.find_class


def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)


def patch():

    # Titles & Prefixes
    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Acc4_Mad").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Barrel_Sticky").ObjectFlags |= 0x4000

    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Acc4_Mad").PartName = "Mad"
    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Acc4_Mad").Priority = 3
    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Barrel_Sticky").PartName = "Sticky"


    #Parts
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_grenade_launcher.acc.acc2_Blitz").ObjectFlags |= 0x4000

    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts.append(current_obj.WeightedParts[10])
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("WeaponPartDefinition","gd_weap_grenade_launcher.Barrel.barrel3_Dahl_Onslaught")
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition","gd_manufacturers.Manufacturers.Dahl")
    obj("WeaponPartDefinition","gd_weap_grenade_launcher.acc.acc2_Blitz").WeaponAttributeEffects.append(current_obj.ExternalAttributeEffects[2])
    obj("WeaponPartDefinition","gd_weap_grenade_launcher.acc.acc2_Blitz").WeaponAttributeEffects.append(current_obj.ExternalAttributeEffects[1])


    # Skills

        # Brick
    # obj("SkillDefinition","gd_Skills2_Brick.Blaster.Revenge").ObjectFlags |= 0x4000

    # obj("SkillDefinition","gd_Skills2_Brick.Blaster.Revenge").SkillEffectDefinitions.append(current_obj.SkillEffectDefinitions[1])
    # obj("SkillDefinition","gd_Skills2_Brick.Blaster.Revenge").SkillEffectDefinitions[(len(current_obj.SkillEffectDefinitions)) - 1].AttributeToModify = obj("AttributeDefinition","d_attributes.DamageSourceModifiers.InstigatedGrenadeDamageModifier")

    # Projectiles

    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Impact").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Leviathan").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Impact").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Rebounder").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Rainmaker_Children").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Sticky").ObjectFlags |= 0x4000

    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Impact").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Leviathan").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Impact").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Rebounder").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Rainmaker_Children").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Sticky").bUseAccurateCollision = False

    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").DefaultBehaviorSet.OnExplode[1].ChildProjectileBaseValues.append(obj("ProjectileDefinition","gd_grenades.Longbow.HandGrenade_LongBow").DefaultBehaviorSet.OnExplode[2].ChildProjectileBaseValues[0])

    # Misc
    obj("AttributeDefinition","d_attributes.WeaponType.Weapon_Is_RocketLauncher").ObjectFlags |= 0x4000

    obj("AttributeDefinition","d_attributes.WeaponType.Weapon_Is_RocketLauncher").ValueResolverChain.append(obj("AttributeDefinition","GL_Assets.WeaponType.Weapon_Is_RocketLauncher").ValueResolverChain[0])

    obj("WeaponTypeDefinition","gd_weap_grenade_launcher.A_Weapon.WeaponType_grenade_launcher").InstantHitDamageType = wclass("WillowDmgSource_Rocket")


    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Impact").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Leviathan").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Impact").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Rebounder").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Rainmaker_Children").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Sticky").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")



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
    hooks=[on_level_loaded, on_commit_map_change, on_startgame],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/GrenadeLaunchersSDK.json"),
)

logging.info(f"Grenade Launchers SDK Loaded: {__version__}, {__version_info__}")
