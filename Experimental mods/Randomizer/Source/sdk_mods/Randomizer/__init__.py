import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, SETTINGS_DIR, build_mod, ENGINE
from mods_base.options import BaseOption, BoolOption
from unrealsdk import logging, make_struct, find_class

from .enemies import randomize_enemies

bRandomizeEnemies = BoolOption("Randomize Enemies", True)

bPatched = False

def load_obj (definition:str, object:str):
    object_class = unrealsdk.find_class(definition)
    current_obj = ENGINE.DynamicLoadObject(object, object_class, False)
    current_obj.ObjectFlags |= 0x4000
    return current_obj

def SetSkeletalMesh (part:str, mesh:str):
    part = load_obj("WeaponPartDefinition",part)
    mesh = load_obj("SkeletalMesh",mesh)
    part.bIsGestaltMode = False
    part.NongestaltSkeletalMesh = mesh




def patch():

    Acc_lists = [load_obj("WeaponPartListDefinition","gd_weap_alien_rifle.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_assault_shotgun.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_rifle.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_shotgun.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_grenade_launcher.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_machine_pistol.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_patrol_smg.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_repeater_pistol.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_revolver_pistol.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_rocket_launcher.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.acc.Acc_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_support_machinegun.acc.Acc_PartList")]



    Barrel_lists = [load_obj("WeaponPartListDefinition","gd_weap_alien_rifle.Barrel.Barrel_xx_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_assault_shotgun.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_rifle.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_shotgun.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_machine_pistol.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_patrol_smg.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_repeater_pistol.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_revolver_pistol.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_rocket_launcher.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.Barrel.Barrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_CombatRifle_parts.Barrel_PartListBarrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_CombatShotgun_parts.Barrel_PartListBarrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_PatrolSMG_parts.Barrel_PartListBarrel_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_RepeaterPistol_parts.Barrel_PartListBarrel_PartList")]




    Body_lists = [load_obj("WeaponPartListDefinition","gd_weap_alien_rifle.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_assault_shotgun.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_rifle.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_shotgun.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_machine_pistol.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_patrol_smg.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_repeater_pistol.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_revolver_pistol.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_rocket_launcher.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_support_machinegun.Body.Body_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_CombatRifle_parts.Body_PartListBody_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_CombatShotgun_parts.Body_PartListBody_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_PatrolSMG_parts.Body_PartListBody_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_RepeaterPistol_parts.Body_PartListBody_PartList")]




    Grip_lists = [load_obj("WeaponPartListDefinition","gd_weap_alien_rifle.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_assault_shotgun.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_rifle.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_shotgun.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_machine_pistol.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_patrol_smg.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_repeater_pistol.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_revolver_pistol.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_rocket_launcher.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_support_machinegun.Grip.Grip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_CombatRifle_parts.Grip_PartListGrip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_CombatShotgun_parts.Grip_PartListGrip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_PatrolSMG_parts.Grip_PartListGrip_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_RepeaterPistol_parts.Grip_PartListGrip_PartList")]



    Mag_lists = [load_obj("WeaponPartListDefinition","gd_weap_alien_rifle.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_assault_shotgun.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_rifle.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_shotgun.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_grenade_launcher.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_machine_pistol.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_patrol_smg.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_repeater_pistol.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_revolver_pistol.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_rocket_launcher.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_support_machinegun.mag.Mag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_CombatRifle_parts.Mag_PartListMag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_CombatShotgun_parts.Mag_PartListMag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_PatrolSMG_parts.Mag_PartListMag_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_RepeaterPistol_parts.Mag_PartListMag_PartList")]
    


    Sight_lists = [load_obj("WeaponPartListDefinition","gd_weap_alien_rifle.Sight.Sight_Rifle_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_alien_rifle.Sight.Sight_Sniper_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_assault_shotgun.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_rifle.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_shotgun.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_machine_pistol.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_patrol_smg.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_repeater_pistol.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_revolver_pistol.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_rocket_launcher.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.Sight.Sight_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_support_machinegun.Sight.Sight_PartList")]







    Stock_lists = [load_obj("WeaponPartListDefinition","gd_weap_alien_rifle.Stock.Stock_Rifle_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_alien_rifle.Stock.Stock_Sniper_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_assault_shotgun.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_rifle.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_combat_shotgun.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_machine_pistol.Action.Action_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_patrol_smg.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_repeater_pistol.Action.Action_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_revolver_pistol.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_rocket_launcher.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_support_machinegun.Stock.Stock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_CombatRifle_parts.Stock_PartListStock_PartList"),
                 load_obj("WeaponPartListDefinition","gd_weap_stock_weapons.stock_RepeaterPistol_parts.Action_PartListAction_PartList")]





    Final_Acc_list = []
    Final_Barrel_list = []
    Final_Body_list = []
    Final_Grip_list = []
    Final_Mag_list = []
    Final_Sight_list = []
    Final_Stock_list = []


    for x in Acc_lists:
        for y in x.WeightedParts:
            y.Manufacturers.clear()
            Final_Acc_list.append(y)

    for x in Barrel_lists:
        for y in x.WeightedParts:
            y.Manufacturers.clear()
            Final_Barrel_list.append(y)

    for x in Body_lists:
        for y in x.WeightedParts:
            y.Manufacturers.clear()
            Final_Body_list.append(y)

    for x in Grip_lists:
        for y in x.WeightedParts:
            y.Manufacturers.clear()
            Final_Grip_list.append(y)

    for x in Mag_lists:
        for y in x.WeightedParts:
            y.Manufacturers.clear()
            Final_Mag_list.append(y)

    for x in Sight_lists:
        for y in x.WeightedParts:
            y.Manufacturers.clear()
            Final_Sight_list.append(y)

    for x in Stock_lists:
        for y in x.WeightedParts:
            y.Manufacturers.clear()
            Final_Stock_list.append(y)


    
    for x in Acc_lists:
        x.WeightedParts = Final_Acc_list

    for x in Barrel_lists:
        x.WeightedParts = Final_Barrel_list

    for x in Body_lists:
        x.WeightedParts = Final_Body_list

    for x in Grip_lists:
        x.WeightedParts = Final_Grip_list

    for x in Mag_lists:
        x.WeightedParts = Final_Mag_list

    for x in Sight_lists:
        x.WeightedParts = Final_Sight_list

    for x in Stock_lists:
        x.WeightedParts = Final_Stock_list

    
    Projectile_Fix = unrealsdk.make_struct("AttributeBaseValueData")
    Projectile_Fix.Attribute = load_obj("AttributeDefinition","d_attributes.Projectile.ProjectileDamage")
    Projectile_Fix.BaseValue.BaseValueAttribute = load_obj("AttributeDefinition","d_attributes.Weapon.WeaponDamage")
    Projectile_Fix.BaseValue.BaseValueScaleConstant = 1

    for x in unrealsdk.find_all("WeaponTypeDefinition"):
        x.ProjectileBaseValues.clear()
        x.ProjectileBaseValues.append(Projectile_Fix)




@hook(
    hook_func="Engine.CurrentGameDataStore:NotifyGameSessionEnded",
    hook_type=Type.POST,
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











@hook("WillowGame.WillowGameInfo:PreCommitMapChange", Type.POST)
def FinalizedMapChange(obj:UObject, args:WrappedStruct, ret:any, func:BoundFunction) -> None:
    if bRandomizeEnemies.value is True:
        randomize_enemies()







# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    options=[bRandomizeEnemies],
    keybinds=[],
    hooks=[on_startgame, FinalizedMapChange],
    commands=[],
)