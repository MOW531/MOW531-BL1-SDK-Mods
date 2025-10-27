import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, SETTINGS_DIR, build_mod, ENGINE
from mods_base.options import BaseOption, BoolOption
from unrealsdk import logging, make_struct, find_class

bPatched = False
current_obj = None


def load_obj (definition:str, object:str):
    global current_obj
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

    # Eridian
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Acid_Storm").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Blaster").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Launcher.a_weap.WeaponType_Eridan_Cannon").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Rifle.a_weap.WeaponType_Eridan_Elementalgun").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Fire_Storm").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Sniper.a_weap.WeaponType_Eridan_Lightning").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Rifle").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Riflede").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Shotgun.a_weap.WeaponType_Eridan_ShockGun").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Sniperde").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Shotgun.a_weap.WeaponType_Eridan_Thunder_Storm").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_alien_rifle.acc.acc1","weap_alien_rifle.acc.acc1")
    SetSkeletalMesh("gd_weap_alien_rifle.acc.acc2","weap_alien_rifle.acc.acc2")
    SetSkeletalMesh("gd_weap_alien_rifle.acc.acc3","weap_alien_rifle.acc.acc3")
    SetSkeletalMesh("gd_weap_alien_rifle.acc.acc4","weap_alien_rifle.acc.acc4")
    SetSkeletalMesh("gd_weap_alien_rifle.acc.acc5","weap_alien_rifle.acc.acc5")
    SetSkeletalMesh("gd_weap_alien_rifle.acc.acc6","weap_alien_rifle.acc.acc6")
        # Barrel
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel1","weap_alien_rifle.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel4_BallBlaster","weap_alien_rifle.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel4_Blaster","weap_alien_rifle.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel4_MercurialBlaster","weap_alien_rifle.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel4_WaveBlaster","weap_alien_rifle.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel5_Cannon","weap_alien_rifle.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel6","weap_alien_rifle.Barrel.barrel6")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel2_Fireball","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel2_Firebomb","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel2_Flaregun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel2_GlobGun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel2_Rifle","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel2_RollingSpattergun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel2_Splatgun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel2_StampedingSpattergun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel3_Rifle","weap_alien_rifle.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_alien_rifle.Barrel.barrel5_MegaCannon","weap_alien_rifle.Barrel.barrel5")
        # Body
    SetSkeletalMesh("gd_weap_alien_rifle.Body.body1","weap_alien_rifle.Body.body1")
    SetSkeletalMesh("gd_weap_alien_rifle.Body.body2","weap_alien_rifle.Body.body2")
    SetSkeletalMesh("gd_weap_alien_rifle.Body.body3","weap_alien_rifle.Body.body3")
    SetSkeletalMesh("gd_weap_alien_rifle.Body.body4","weap_alien_rifle.Body.body4")
    SetSkeletalMesh("gd_weap_alien_rifle.Body.body5","weap_alien_rifle.Body.body5")
    SetSkeletalMesh("gd_weap_alien_rifle.Body.body6","weap_alien_rifle.Body.body6")
        # Grip
    SetSkeletalMesh("gd_weap_alien_rifle.Grip.grip1","weap_alien_rifle.Grip.grip1")
    SetSkeletalMesh("gd_weap_alien_rifle.Grip.grip2","weap_alien_rifle.Grip.grip2")
    SetSkeletalMesh("gd_weap_alien_rifle.Grip.grip3","weap_alien_rifle.Grip.grip3")
    SetSkeletalMesh("gd_weap_alien_rifle.Grip.grip4","weap_alien_rifle.Grip.grip4")
    SetSkeletalMesh("gd_weap_alien_rifle.Grip.grip5","weap_alien_rifle.Grip.grip5")
    SetSkeletalMesh("gd_weap_alien_rifle.Grip.grip6","weap_alien_rifle.Grip.grip6")
        # Mag
    SetSkeletalMesh("gd_weap_alien_rifle.mag.mag1","weap_alien_rifle.mag.mag1")
    SetSkeletalMesh("gd_weap_alien_rifle.mag.mag2","weap_alien_rifle.mag.mag2")
    SetSkeletalMesh("gd_weap_alien_rifle.mag.mag3","weap_alien_rifle.mag.mag3")
    SetSkeletalMesh("gd_weap_alien_rifle.mag.mag4","weap_alien_rifle.mag.mag4")
    SetSkeletalMesh("gd_weap_alien_rifle.mag.mag5","weap_alien_rifle.mag.mag5")
    SetSkeletalMesh("gd_weap_alien_rifle.mag.mag6","weap_alien_rifle.mag.mag6")
        # Sight
    SetSkeletalMesh("gd_weap_alien_rifle.Sight.sight1","weap_alien_rifle.Sight.sight1")
    SetSkeletalMesh("gd_weap_alien_rifle.Sight.sight2","weap_alien_rifle.Sight.sight2")
    SetSkeletalMesh("gd_weap_alien_rifle.Sight.sight3","weap_alien_rifle.Sight.sight3")
    SetSkeletalMesh("gd_weap_alien_rifle.Sight.sight4","weap_alien_rifle.Sight.sight4")
    SetSkeletalMesh("gd_weap_alien_rifle.Sight.sight5","weap_alien_rifle.Sight.sight5")
    SetSkeletalMesh("gd_weap_alien_rifle.Sight.sight6","weap_alien_rifle.Sight.sight6")
        # Stock
    SetSkeletalMesh("gd_weap_alien_rifle.Stock.stock1","weap_alien_rifle.Stock.stock1")
    SetSkeletalMesh("gd_weap_alien_rifle.Stock.stock2","weap_alien_rifle.Stock.stock2")
    SetSkeletalMesh("gd_weap_alien_rifle.Stock.stock3","weap_alien_rifle.Stock.stock3")
    SetSkeletalMesh("gd_weap_alien_rifle.Stock.stock4","weap_alien_rifle.Stock.stock4")
    SetSkeletalMesh("gd_weap_alien_rifle.Stock.stock5","weap_alien_rifle.Stock.stock5")
    SetSkeletalMesh("gd_weap_alien_rifle.Stock.stock6","weap_alien_rifle.Stock.stock6")


    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.Cannon.barrel5_MegaCannon","weap_alien_rifle.Barrel.barrel5")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_Fireball","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_Firebomb","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_Flaregun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_GlobGun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_RollingSpattergun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_Splatgun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_StampedingSpattergun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel3_Rifle","weap_alien_rifle.Barrel.barrel3")







    # Assault Shotgun 
    load_obj("WeaponTypeDefinition","gd_weap_assault_shotgun.A_Weapon.WeaponType_assault_shotgun").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_assault_shotgun.acc.acc1_Spiked","weap_combat_shotgun.acc.acc1")
    SetSkeletalMesh("gd_weap_assault_shotgun.acc.acc2_Raging","weap_combat_shotgun.acc.acc2")
    SetSkeletalMesh("gd_weap_assault_shotgun.acc.acc3_Maliwan_Corrosive_Plague","weap_combat_shotgun.acc.acc3")
    SetSkeletalMesh("gd_weap_assault_shotgun.acc.acc4_Painful","weap_combat_shotgun.acc.acc4")
    SetSkeletalMesh("gd_weap_assault_shotgun.acc.acc5_SandSCrux","weap_combat_shotgun.acc.acc5")
    SetSkeletalMesh("gd_weap_assault_shotgun.acc.acc5_Vladof_Hammer","weap_combat_shotgun.acc.acc5")
        # Barrel
    SetSkeletalMesh("gd_weap_assault_shotgun.Barrel.barrel4_Hyperion_Butcher","weap_combat_shotgun.Barrel.barrel4")
        # Mag
    SetSkeletalMesh("gd_weap_assault_shotgun.mag.mag3","weap_combat_shotgun.mag.mag3")
    SetSkeletalMesh("gd_weap_assault_shotgun.mag.mag3a","weap_combat_shotgun.mag.mag3")








    # Combat Rifle 
    load_obj("WeaponTypeDefinition","gd_weap_combat_rifle.A_Weapon.WeaponType_combat_rifle").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_combat_rifle.acc.acc2_Intense","weap_combat_rifle.acc.acc2")
    SetSkeletalMesh("gd_weap_combat_rifle.acc.acc3_Corrosive","weap_combat_rifle.acc.acc3")
    SetSkeletalMesh("gd_weap_combat_rifle.acc.acc3_Shock","weap_combat_rifle.acc.acc3")
    SetSkeletalMesh("gd_weap_combat_rifle.acc.acc4_Deathly","weap_combat_rifle.acc.acc4")
    SetSkeletalMesh("gd_weap_combat_rifle.acc.acc5_Explosive","weap_combat_rifle.acc.acc5")
    SetSkeletalMesh("gd_weap_combat_rifle.acc.acc5_Incendiary","weap_combat_rifle.acc.acc5")
        # Barrel
    SetSkeletalMesh("gd_weap_combat_rifle.Barrel.barrel1","weap_combat_rifle.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_combat_rifle.Barrel.barrel1_starter","weap_combat_rifle.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_combat_rifle.Barrel.barrel2","weap_combat_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_combat_rifle.Barrel.barrel3","weap_combat_rifle.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_combat_rifle.Barrel.barrel4","weap_combat_rifle.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_combat_rifle.Barrel.barrel4_Dahl_Raven","weap_combat_rifle.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_combat_rifle.Barrel.barrel5","weap_combat_rifle.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_combat_rifle.Barrel.barrel5_Hyperion_Destroyer","weap_combat_rifle.Barrel.barrel5")
        # Body
    SetSkeletalMesh("gd_weap_combat_rifle.Body.body1","weap_combat_rifle.Body.body1")
    SetSkeletalMesh("gd_weap_combat_rifle.Body.body2","weap_combat_rifle.Body.body2")
    SetSkeletalMesh("gd_weap_combat_rifle.Body.body3","weap_combat_rifle.Body.body3")
    SetSkeletalMesh("gd_weap_combat_rifle.Body.body4","weap_combat_rifle.Body.body4")
    SetSkeletalMesh("gd_weap_combat_rifle.Body.body4_Tediore_Guardian","weap_combat_rifle.Body.body4")
    SetSkeletalMesh("gd_weap_combat_rifle.Body.body5","weap_combat_rifle.Body.body5")
        # Grip
    SetSkeletalMesh("gd_weap_combat_rifle.Grip.grip1","weap_combat_rifle.Grip.grip1")
    SetSkeletalMesh("gd_weap_combat_rifle.Grip.grip2","weap_combat_rifle.Grip.grip2")
    SetSkeletalMesh("gd_weap_combat_rifle.Grip.grip3","weap_combat_rifle.Grip.grip3")
    SetSkeletalMesh("gd_weap_combat_rifle.Grip.grip4","weap_combat_rifle.Grip.grip4")
    SetSkeletalMesh("gd_weap_combat_rifle.Grip.grip5","weap_combat_rifle.Grip.grip5")
    SetSkeletalMesh("gd_weap_combat_rifle.Grip.grip5_Gearbox","weap_combat_rifle.Grip.grip5")
        # Mag
    SetSkeletalMesh("gd_weap_combat_rifle.mag.mag1","weap_combat_rifle.mag.mag1")
    SetSkeletalMesh("gd_weap_combat_rifle.mag.mag1a_pounder","weap_combat_rifle.mag.mag1")
    SetSkeletalMesh("gd_weap_combat_rifle.mag.mag3","weap_combat_rifle.mag.mag3")
    SetSkeletalMesh("gd_weap_combat_rifle.mag.mag3_Dahl_Raven","weap_combat_rifle.mag.mag3")
        # Sight
    SetSkeletalMesh("gd_weap_combat_rifle.Sight.sight1","weap_combat_rifle.Sight.sight1")
    SetSkeletalMesh("gd_weap_combat_rifle.Sight.sight2","weap_combat_rifle.Sight.sight2")
    SetSkeletalMesh("gd_weap_combat_rifle.Sight.sight3","weap_combat_rifle.Sight.sight3")
    SetSkeletalMesh("gd_weap_combat_rifle.Sight.sight4","weap_combat_rifle.Sight.sight4")
    SetSkeletalMesh("gd_weap_combat_rifle.Sight.sight5","weap_combat_rifle.Sight.sight5")
        # Stock
    SetSkeletalMesh("gd_weap_combat_rifle.Stock.stock1","weap_combat_rifle.Stock.stock1")
    SetSkeletalMesh("gd_weap_combat_rifle.Stock.stock2","weap_combat_rifle.Stock.stock2")
    SetSkeletalMesh("gd_weap_combat_rifle.Stock.stock3","weap_combat_rifle.Stock.stock3")
    SetSkeletalMesh("gd_weap_combat_rifle.Stock.stock4","weap_combat_rifle.Stock.stock4")
    SetSkeletalMesh("gd_weap_combat_rifle.Stock.stock5","weap_combat_rifle.Stock.stock5")
        # UniqueParts
    SetSkeletalMesh("gd_weap_combat_rifle.UniqueParts.Sentinel_sight4","weap_combat_rifle.Sight.sight4")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.CombatRifle.TedioreAvenger_sight5","weap_combat_rifle.Sight.sight5")






    # Combat Shotgun 
    load_obj("WeaponTypeDefinition","gd_weap_combat_shotgun.A_Weapon.WeaponType_combat_shotgun").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc1_Jagged","weap_combat_shotgun.acc.acc1")
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc2_Frenzied","weap_combat_shotgun.acc.acc2")
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc3_Corrosive","weap_combat_shotgun.acc.acc3")
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc3_Shock","weap_combat_shotgun.acc.acc3")
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc4_Atlas_Hydra","weap_combat_shotgun.acc.acc4")
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc4_Terrible","weap_combat_shotgun.acc.acc4")
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc5","weap_combat_shotgun.acc.acc5")
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc5_Explosive","weap_combat_shotgun.acc.acc5")
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc5_Incendiary","weap_combat_shotgun.acc.acc5")
    SetSkeletalMesh("gd_weap_combat_shotgun.acc.acc5_Torgue_FriendlyFire","weap_combat_shotgun.acc.acc5")
        # Barrel
    SetSkeletalMesh("gd_weap_combat_shotgun.Barrel.barrel1","weap_combat_shotgun.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_combat_shotgun.Barrel.barrel2","weap_combat_shotgun.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_combat_shotgun.Barrel.barrel2_Shredder","weap_combat_shotgun.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_combat_shotgun.Barrel.barrel3","weap_combat_shotgun.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_combat_shotgun.Barrel.barrel3_Carnage","weap_combat_shotgun.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_combat_shotgun.Barrel.barrel4","weap_combat_shotgun.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_combat_shotgun.Barrel.barrel5","weap_combat_shotgun.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_combat_shotgun.Barrel.barrel5_JakobsStriker","weap_combat_shotgun.Barrel.barrel5")
        # Body
    SetSkeletalMesh("gd_weap_combat_shotgun.Body.body1","weap_combat_shotgun.Body.body1")
    SetSkeletalMesh("gd_weap_combat_shotgun.Body.body2","weap_combat_shotgun.Body.body2")
    SetSkeletalMesh("gd_weap_combat_shotgun.Body.body3","weap_combat_shotgun.Body.body3")
    SetSkeletalMesh("gd_weap_combat_shotgun.Body.body3_Tediore_Defender","weap_combat_shotgun.Body.body3")
    SetSkeletalMesh("gd_weap_combat_shotgun.Body.body4","weap_combat_shotgun.Body.body4")
    SetSkeletalMesh("gd_weap_combat_shotgun.Body.body5","weap_combat_shotgun.Body.body5")
        # Grip
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip1","weap_combat_shotgun.Grip.grip1")
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip1a","weap_combat_shotgun.Grip.grip1")
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip2","weap_combat_shotgun.Grip.grip2")
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip2_gearbox","weap_combat_shotgun.Grip.grip2")
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip2a_Torgue","weap_combat_shotgun.Grip.grip2")
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip3","weap_combat_shotgun.Grip.grip3")
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip3a","weap_combat_shotgun.Grip.grip3")
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip3b","weap_combat_shotgun.Grip.grip3")
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip4","weap_combat_shotgun.Grip.grip4")
    SetSkeletalMesh("gd_weap_combat_shotgun.Grip.grip5","weap_combat_shotgun.Grip.grip5")
        # Mag
    SetSkeletalMesh("gd_weap_combat_shotgun.mag.mag1","weap_combat_shotgun.mag.mag1")
    SetSkeletalMesh("gd_weap_combat_shotgun.mag.mag2","weap_combat_shotgun.mag.mag2")
    SetSkeletalMesh("gd_weap_combat_shotgun.mag.mag2_Dahl_Bulldog","weap_combat_shotgun.mag.mag2")
    SetSkeletalMesh("gd_weap_combat_shotgun.mag.mag3","weap_combat_shotgun.mag.mag3")
    SetSkeletalMesh("gd_weap_combat_shotgun.mag.mag4","weap_combat_shotgun.mag.mag4")
    SetSkeletalMesh("gd_weap_combat_shotgun.mag.mag5","weap_combat_shotgun.mag.mag5")
        # Sight
    SetSkeletalMesh("gd_weap_combat_shotgun.Sight.sight1_","weap_combat_shotgun.Sight.sight2")
    SetSkeletalMesh("gd_weap_combat_shotgun.Sight.sight2_","weap_combat_shotgun.Sight.sight1")
    SetSkeletalMesh("gd_weap_combat_shotgun.Sight.sight3","weap_combat_shotgun.Sight.sight3")
    SetSkeletalMesh("gd_weap_combat_shotgun.Sight.sight4","weap_combat_shotgun.Sight.sight4")
    SetSkeletalMesh("gd_weap_combat_shotgun.Sight.sight5","weap_combat_shotgun.Sight.sight5")
        # UniqueParts
    SetSkeletalMesh("gd_weap_combat_shotgun.UniqueParts.Blister_barrel3","weap_combat_shotgun.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_combat_shotgun.UniqueParts.BoomStick_barrel3_Carnage","weap_combat_shotgun.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_combat_shotgun.UniqueParts.SledgesShotgun_barrel2","weap_combat_shotgun.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_combat_shotgun.UniqueParts.TKsWave_barrel2","weap_combat_shotgun.Barrel.barrel2")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.CombatShotgun.barrel3_DahlJackal","weap_combat_shotgun.Barrel.barrel3")










    # Grenade Launcher 
    load_obj("WeaponTypeDefinition","gd_weap_grenade_launcher.A_Weapon.WeaponType_grenade_launcher").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_grenade_launcher.acc.acc1_Divine","weap_rocket_launcher.acc.acc1")
    SetSkeletalMesh("gd_weap_grenade_launcher.acc.acc2_Blitz","weap_rocket_launcher.acc.acc2")
    SetSkeletalMesh("gd_weap_grenade_launcher.acc.acc4_Mad","weap_rocket_launcher.acc.acc4")
        # Barrel
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel3","weap_rocket_launcher.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel3_Dahl_Onslaught","weap_rocket_launcher.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel3_impact","weap_rocket_launcher.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel3_rebounding","weap_rocket_launcher.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel3_sticky","weap_rocket_launcher.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel4_Atlas_Leviathan","weap_rocket_launcher.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel4_Mortar","weap_rocket_launcher.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel5","weap_rocket_launcher.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel5_impact","weap_rocket_launcher.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel5_rebounding","weap_rocket_launcher.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel5_SandS_Rainmaker","weap_rocket_launcher.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_grenade_launcher.Barrel.barrel5_sticky","weap_rocket_launcher.Barrel.barrel5")
        # Body
    SetSkeletalMesh("gd_weap_grenade_launcher.Body.body2","weap_rocket_launcher.Body.body2")
    SetSkeletalMesh("gd_weap_grenade_launcher.Body.body4","weap_rocket_launcher.Body.body4")
    SetSkeletalMesh("gd_weap_grenade_launcher.Body.body4_Jakobs_Terror","weap_rocket_launcher.Body.body4")
        # Mag
    SetSkeletalMesh("gd_weap_grenade_launcher.mag.mag1","weap_rocket_launcher.mag.mag1")
        # Stock
    SetSkeletalMesh("gd_weap_grenade_launcher.Stock.stock1","weap_rocket_launcher.Stock.stock1")







    # Machine Pistols
    load_obj("WeaponTypeDefinition","gd_weap_machine_pistol.A_Weapon.WeaponType_machine_pistol").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_machine_pistol.acc.acc1_Hyperion_Reaper","weap_repeater_pistol.acc.acc1")
    SetSkeletalMesh("gd_weap_machine_pistol.acc.acc2_Cold","weap_repeater_pistol.acc.acc2")
    SetSkeletalMesh("gd_weap_machine_pistol.acc.acc2_Rage","weap_repeater_pistol.acc.acc2")
        # Barrel
    SetSkeletalMesh("gd_weap_machine_pistol.Barrel.barrel5_Vladof_Vengence","weap_repeater_pistol.Barrel.barrel5")
        # Body
    SetSkeletalMesh("gd_weap_machine_pistol.Body.body5","weap_repeater_pistol.Body.body5")
        # Grip
    SetSkeletalMesh("gd_weap_machine_pistol.Grip.grip2","weap_repeater_pistol.Grip.grip2")
    SetSkeletalMesh("gd_weap_machine_pistol.Grip.grip3","weap_repeater_pistol.Grip.grip3")
    SetSkeletalMesh("gd_weap_machine_pistol.Grip.grip5","weap_repeater_pistol.Grip.grip5")
        # Mag
    SetSkeletalMesh("gd_weap_machine_pistol.mag.mag2","weap_repeater_pistol.mag.mag2")
    SetSkeletalMesh("gd_weap_machine_pistol.mag.mag3","weap_repeater_pistol.mag.mag3")
    SetSkeletalMesh("gd_weap_machine_pistol.mag.mag3_SandS_Thanatos","weap_repeater_pistol.mag.mag3")
        # UniqueParts
    SetSkeletalMesh("gd_weap_machine_pistol.UniqueParts.TheClipper_acc5_Incendiary","weap_repeater_pistol.acc.acc5")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.MachinePistol.barrel4_VladofStalker","weap_repeater_pistol.Barrel.barrel4")







    # SMG 
    load_obj("WeaponTypeDefinition","gd_weap_patrol_smg.A_Weapon.WeaponType_patrol_smg").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_patrol_smg.acc.acc1_Relentless","weap_patrol_smg.acc.acc1")
    SetSkeletalMesh("gd_weap_patrol_smg.acc.acc2_Ruthless","weap_patrol_smg.acc.acc2")
    SetSkeletalMesh("gd_weap_patrol_smg.acc.acc2_Vector","weap_patrol_smg.acc.acc2")
    SetSkeletalMesh("gd_weap_patrol_smg.acc.acc3_Corrosive","weap_patrol_smg.acc.acc3")
    SetSkeletalMesh("gd_weap_patrol_smg.acc.acc3_Shock","weap_patrol_smg.acc.acc3")
    SetSkeletalMesh("gd_weap_patrol_smg.acc.acc4_Double","weap_patrol_smg.acc.acc4")
    SetSkeletalMesh("gd_weap_patrol_smg.acc.acc5_Explosive","weap_patrol_smg.acc.acc5")
    SetSkeletalMesh("gd_weap_patrol_smg.acc.acc5_Incendiary","weap_patrol_smg.acc.acc5")
    SetSkeletalMesh("gd_weap_patrol_smg.acc.acc5_Maliwan_HellFire","weap_patrol_smg.acc.acc5")
        # Barrel
    SetSkeletalMesh("gd_weap_patrol_smg.Barrel.barrel1","weap_patrol_smg.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_patrol_smg.Barrel.barrel2","weap_patrol_smg.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_patrol_smg.Barrel.barrel2_Torgue_Gasher","weap_patrol_smg.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_patrol_smg.Barrel.barrel3","weap_patrol_smg.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_patrol_smg.Barrel.barrel3_Twisted","weap_patrol_smg.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_patrol_smg.Barrel.barrel4","weap_patrol_smg.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_patrol_smg.Barrel.barrel5","weap_patrol_smg.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_patrol_smg.Barrel.barrel5_Hyperion_Bitch","weap_patrol_smg.Barrel.barrel5")
        # Body
    SetSkeletalMesh("gd_weap_patrol_smg.Body.body1","weap_patrol_smg.Body.body1")
    SetSkeletalMesh("gd_weap_patrol_smg.Body.body2","weap_patrol_smg.Body.body2")
    SetSkeletalMesh("gd_weap_patrol_smg.Body.body3","weap_patrol_smg.Body.body3")
    SetSkeletalMesh("gd_weap_patrol_smg.Body.body3_Tediore_Savior","weap_patrol_smg.Body.body3")
    SetSkeletalMesh("gd_weap_patrol_smg.Body.body4","weap_patrol_smg.Body.body4")
    SetSkeletalMesh("gd_weap_patrol_smg.Body.body5","weap_patrol_smg.Body.body5")
        # Grip
    SetSkeletalMesh("gd_weap_patrol_smg.Grip.grip1","weap_patrol_smg.Grip.grip1")
    SetSkeletalMesh("gd_weap_patrol_smg.Grip.grip2","weap_patrol_smg.Grip.grip2")
    SetSkeletalMesh("gd_weap_patrol_smg.Grip.grip3","weap_patrol_smg.Grip.grip3")
    SetSkeletalMesh("gd_weap_patrol_smg.Grip.grip4","weap_patrol_smg.Grip.grip4")
    SetSkeletalMesh("gd_weap_patrol_smg.Grip.grip4_gearbox","weap_patrol_smg.Grip.grip4")
    SetSkeletalMesh("gd_weap_patrol_smg.Grip.grip5","weap_patrol_smg.Grip.grip5")
        # Mag
    SetSkeletalMesh("gd_weap_patrol_smg.mag.mag1_thumper","weap_patrol_smg.mag.mag1")
    SetSkeletalMesh("gd_weap_patrol_smg.mag.mag2","weap_patrol_smg.mag.mag2")
    SetSkeletalMesh("gd_weap_patrol_smg.mag.mag3","weap_patrol_smg.mag.mag3")
    SetSkeletalMesh("gd_weap_patrol_smg.mag.mag4","weap_patrol_smg.mag.mag4")
    SetSkeletalMesh("gd_weap_patrol_smg.mag.mag4_Dahl_Wildcat","weap_patrol_smg.mag.mag4")
    SetSkeletalMesh("gd_weap_patrol_smg.mag.mag5","weap_patrol_smg.mag.mag5")
        # Sight
    SetSkeletalMesh("gd_weap_patrol_smg.Sight.sight1","weap_patrol_smg.Sight.sight1")
    SetSkeletalMesh("gd_weap_patrol_smg.Sight.sight2","weap_patrol_smg.Sight.sight2")
    SetSkeletalMesh("gd_weap_patrol_smg.Sight.sight3","weap_patrol_smg.Sight.sight3")
    SetSkeletalMesh("gd_weap_patrol_smg.Sight.sight4","weap_patrol_smg.Sight.sight4")
    SetSkeletalMesh("gd_weap_patrol_smg.Sight.sight5","weap_patrol_smg.Sight.sight5")
        # Stock
    SetSkeletalMesh("gd_weap_patrol_smg.Stock.stock1","weap_patrol_smg.Stock.stock1")
    SetSkeletalMesh("gd_weap_patrol_smg.Stock.stock2","weap_patrol_smg.Stock.stock2")
    SetSkeletalMesh("gd_weap_patrol_smg.Stock.stock3","weap_patrol_smg.Stock.stock3")
    SetSkeletalMesh("gd_weap_patrol_smg.Stock.stock4","weap_patrol_smg.Stock.stock4")
    SetSkeletalMesh("gd_weap_patrol_smg.Stock.stock5","weap_patrol_smg.Stock.stock5")
        # UniqueParts
    SetSkeletalMesh("gd_weap_patrol_smg.UniqueParts.BoneShredder_mag5","weap_patrol_smg.mag.mag5")
    SetSkeletalMesh("gd_weap_patrol_smg.UniqueParts.TheSpy_sight4","weap_patrol_smg.Sight.sight4")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SMG.acc2_Typhoon","weap_patrol_smg.acc.acc2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SMG.acc3_Maliwan_Tsunami","weap_patrol_smg.acc.acc3")













    # Repeater Pistol 
    load_obj("WeaponTypeDefinition","gd_weap_repeater_pistol.A_Weapon.WeaponType_repeater_pistol").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc1_Fanged","weap_repeater_pistol.acc.acc1")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc1_Lacerator","weap_repeater_pistol.acc.acc1")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc2_Atlas_Troll","weap_repeater_pistol.acc.acc2")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc2_Stabilizer","weap_repeater_pistol.acc.acc2")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc3_LaserSight","weap_repeater_pistol.acc.acc3")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc4_DoubleShot","weap_repeater_pistol.acc.acc4")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc4_SandS_Gemini","weap_repeater_pistol.acc.acc4")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc5_Corrosive","weap_repeater_pistol.acc.acc5")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc5_Explosive","weap_repeater_pistol.acc.acc5")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc5_Hornet_Dahl_Corrosive","weap_repeater_pistol.acc.acc5")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc5_Incendiary","weap_repeater_pistol.acc.acc5")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc5_Maliwan_Firehawk","weap_repeater_pistol.acc.acc5")
    SetSkeletalMesh("gd_weap_repeater_pistol.acc.acc5_Shock","weap_repeater_pistol.acc.acc5")
        # Action
    SetSkeletalMesh("gd_weap_repeater_pistol.Action.action1","weap_repeater_pistol.Action.action1")
    SetSkeletalMesh("gd_weap_repeater_pistol.Action.action2","weap_repeater_pistol.Action.action2")
    SetSkeletalMesh("gd_weap_repeater_pistol.Action.action3","weap_repeater_pistol.Action.action3")
    SetSkeletalMesh("gd_weap_repeater_pistol.Action.action4","weap_repeater_pistol.Action.action4")
    SetSkeletalMesh("gd_weap_repeater_pistol.Action.action5","weap_repeater_pistol.Action.action5")
        # Barrel
    SetSkeletalMesh("gd_weap_repeater_pistol.Barrel.barrel0","weap_repeater_pistol.Barrel.barrel0")
    SetSkeletalMesh("gd_weap_repeater_pistol.Barrel.barrel1","weap_repeater_pistol.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_repeater_pistol.Barrel.barrel2","weap_repeater_pistol.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_repeater_pistol.Barrel.barrel3","weap_repeater_pistol.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_repeater_pistol.Barrel.barrel4","weap_repeater_pistol.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_repeater_pistol.Barrel.barrel4_Torgue_Violator","weap_repeater_pistol.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_repeater_pistol.Barrel.barrel5","weap_repeater_pistol.Barrel.barrel5")
        # Body
    SetSkeletalMesh("gd_weap_repeater_pistol.Body.body1","weap_repeater_pistol.Body.body1")
    SetSkeletalMesh("gd_weap_repeater_pistol.Body.body2","weap_repeater_pistol.Body.body2")
    SetSkeletalMesh("gd_weap_repeater_pistol.Body.body3","weap_repeater_pistol.Body.body3")
    SetSkeletalMesh("gd_weap_repeater_pistol.Body.body3_Tediore_Protector","weap_repeater_pistol.Body.body3")
    SetSkeletalMesh("gd_weap_repeater_pistol.Body.body4","weap_repeater_pistol.Body.body4")
        # Grip
    SetSkeletalMesh("gd_weap_repeater_pistol.Grip.grip1","weap_repeater_pistol.Grip.grip1")
    SetSkeletalMesh("gd_weap_repeater_pistol.Grip.grip2","weap_repeater_pistol.Grip.grip2")
    SetSkeletalMesh("gd_weap_repeater_pistol.Grip.grip2_Atlas","weap_repeater_pistol.Grip.grip2")
    SetSkeletalMesh("gd_weap_repeater_pistol.Grip.grip3","weap_repeater_pistol.Grip.grip3")
    SetSkeletalMesh("gd_weap_repeater_pistol.Grip.grip3_Gearbox","weap_repeater_pistol.Grip.grip3")
    SetSkeletalMesh("gd_weap_repeater_pistol.Grip.grip3_Maliwan","weap_repeater_pistol.Grip.grip3")
    SetSkeletalMesh("gd_weap_repeater_pistol.Grip.grip4","weap_repeater_pistol.Grip.grip4")
    SetSkeletalMesh("gd_weap_repeater_pistol.Grip.grip4_Dahl","weap_repeater_pistol.Grip.grip4")
    SetSkeletalMesh("gd_weap_repeater_pistol.Grip.grip5","weap_repeater_pistol.Grip.grip5")
        # Mag
    SetSkeletalMesh("gd_weap_repeater_pistol.mag.mag1","weap_repeater_pistol.mag.mag1")
    SetSkeletalMesh("gd_weap_repeater_pistol.mag.mag2","weap_repeater_pistol.mag.mag2")
    SetSkeletalMesh("gd_weap_repeater_pistol.mag.mag2a","weap_repeater_pistol.mag.mag2")
    SetSkeletalMesh("gd_weap_repeater_pistol.mag.mag3","weap_repeater_pistol.mag.mag3")
    SetSkeletalMesh("gd_weap_repeater_pistol.mag.mag3_Vladof_Rebel","weap_repeater_pistol.mag.mag3")
        # Sight
    SetSkeletalMesh("gd_weap_repeater_pistol.Sight.sight1","weap_repeater_pistol.Sight.sight1")
    SetSkeletalMesh("gd_weap_repeater_pistol.Sight.sight2","weap_repeater_pistol.Sight.sight2")
    SetSkeletalMesh("gd_weap_repeater_pistol.Sight.sight3","weap_repeater_pistol.Sight.sight3")
    SetSkeletalMesh("gd_weap_repeater_pistol.Sight.sight4","weap_repeater_pistol.Sight.sight4")
    SetSkeletalMesh("gd_weap_repeater_pistol.Sight.sight5","weap_repeater_pistol.Sight.sight5")
    SetSkeletalMesh("gd_weap_repeater_pistol.Sight.sight5_Hyperion_Invader","weap_repeater_pistol.Sight.sight5")
        # UniqueParts
    SetSkeletalMesh("gd_weap_repeater_pistol.UniqueParts.KromsSidearm_barrel5","weap_repeater_pistol.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_repeater_pistol.UniqueParts.LadyFinger_barrel1","weap_repeater_pistol.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_repeater_pistol.UniqueParts.TheDove_barrel4","weap_repeater_pistol.Barrel.barrel4")

    SetSkeletalMesh("gd_weap_machine_pistol.UniqueParts.TheClipper_acc5_Incendiary","weap_repeater_pistol.acc.acc1")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RepeaterPistol.acc5_Shock_HyperionNemesis","weap_repeater_pistol.acc.acc5")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RepeaterPistol.barrel0_ChiquitoAmigo","weap_repeater_pistol.Barrel.barrel0")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RepeaterPistol.barrel5_AthenasWisdom","weap_repeater_pistol.Barrel.barrel5")








    # Revolver Pistol 
    load_obj("WeaponTypeDefinition","gd_weap_revolver_pistol.A_Weapon.WeaponType_revolver_pistol").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc1_Bladed","weap_revolver_pistol.acc.acc1")
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc1_Razor","weap_revolver_pistol.acc.acc1")
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc2_Masher","weap_revolver_pistol.acc.acc2")
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc3_Corrosive","weap_revolver_pistol.acc.acc5")
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc3_Maliwan_Defiler_Corrosive","weap_revolver_pistol.acc.acc5")
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc3_Shock","weap_revolver_pistol.acc.acc5")
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc4_stabilized","weap_revolver_pistol.acc.acc4")
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc5_Atlas_Chimera","weap_revolver_pistol.acc.acc3")
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc5_Explosive","weap_revolver_pistol.acc.acc3")
    SetSkeletalMesh("gd_weap_revolver_pistol.acc.acc5_Incendiary","weap_revolver_pistol.acc.acc3")
        # Barrel
    SetSkeletalMesh("gd_weap_revolver_pistol.Barrel.barrel1","weap_revolver_pistol.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_revolver_pistol.Barrel.barrel2","weap_revolver_pistol.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_revolver_pistol.Barrel.barrel3","weap_revolver_pistol.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_revolver_pistol.Barrel.barrel4","weap_revolver_pistol.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_revolver_pistol.Barrel.barrel4_Dahl_Anaconda","weap_revolver_pistol.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_revolver_pistol.Barrel.barrel5","weap_revolver_pistol.Barrel.barrel5")
    SetSkeletalMesh("gd_weap_revolver_pistol.Barrel.barrel5_Jakobs_Unforgiven","weap_revolver_pistol.Barrel.barrel5")
        # Body
    SetSkeletalMesh("gd_weap_revolver_pistol.Body.body1","weap_revolver_pistol.Body.body1")
    SetSkeletalMesh("gd_weap_revolver_pistol.Body.body2","weap_revolver_pistol.Body.body2")
    SetSkeletalMesh("gd_weap_revolver_pistol.Body.body3","weap_revolver_pistol.Body.body3")
    SetSkeletalMesh("gd_weap_revolver_pistol.Body.body3_tediore_Equalizer","weap_revolver_pistol.Body.body3")
    SetSkeletalMesh("gd_weap_revolver_pistol.Body.body4","weap_revolver_pistol.Body.body4")
    SetSkeletalMesh("gd_weap_revolver_pistol.Body.body5","weap_revolver_pistol.Body.body5")
        # Grip
    SetSkeletalMesh("gd_weap_revolver_pistol.Grip.grip1","weap_revolver_pistol.Grip.grip1")
    SetSkeletalMesh("gd_weap_revolver_pistol.Grip.grip2","weap_revolver_pistol.Grip.grip2")
    SetSkeletalMesh("gd_weap_revolver_pistol.Grip.grip3","weap_revolver_pistol.Grip.grip3")
    SetSkeletalMesh("gd_weap_revolver_pistol.Grip.grip3_Gearbox","weap_revolver_pistol.Grip.grip3")
    SetSkeletalMesh("gd_weap_revolver_pistol.Grip.grip4","weap_revolver_pistol.Grip.grip4")
    SetSkeletalMesh("gd_weap_revolver_pistol.Grip.grip5","weap_revolver_pistol.Grip.grip5")
        # Mag
    SetSkeletalMesh("gd_weap_revolver_pistol.mag.mag1","weap_revolver_pistol.mag.mag1")
    SetSkeletalMesh("gd_weap_revolver_pistol.mag.mag2","weap_revolver_pistol.mag.mag2")
    SetSkeletalMesh("gd_weap_revolver_pistol.mag.mag3","weap_revolver_pistol.mag.mag3")
    SetSkeletalMesh("gd_weap_revolver_pistol.mag.mag4","weap_revolver_pistol.mag.mag4")
    SetSkeletalMesh("gd_weap_revolver_pistol.mag.mag5","weap_revolver_pistol.mag.mag5")
        # Sight
    SetSkeletalMesh("gd_weap_revolver_pistol.Sight.sight1","weap_revolver_pistol.Sight.sight1")
    SetSkeletalMesh("gd_weap_revolver_pistol.Sight.sight2","weap_revolver_pistol.Sight.sight2")
    SetSkeletalMesh("gd_weap_revolver_pistol.Sight.sight3","weap_revolver_pistol.Sight.sight3")
    SetSkeletalMesh("gd_weap_revolver_pistol.Sight.sight4","weap_revolver_pistol.Sight.sight4")
    SetSkeletalMesh("gd_weap_revolver_pistol.Sight.sight5","weap_revolver_pistol.Sight.sight5")
        # UniqueParts
    SetSkeletalMesh("gd_weap_revolver_pistol.UniqueParts.MadJack_acc5_Explosive","weap_revolver_pistol.acc.acc3")
    SetSkeletalMesh("gd_weap_revolver_pistol.UniqueParts.MadJack_barrel3","weap_revolver_pistol.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_revolver_pistol.UniqueParts.Patton_grip5","weap_revolver_pistol.Grip.grip5")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RevolverPistol.acc5_Heal_AtlasAries","weap_revolver_pistol.acc.acc5")













    # Rocket Launcher 
    load_obj("WeaponTypeDefinition","gd_weap_rocket_launcher.A_Weapon.WeaponType_rocket_launcher").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_rocket_launcher.acc.acc1_Recoiless","weap_rocket_launcher.acc.acc1")
    SetSkeletalMesh("gd_weap_rocket_launcher.acc.acc2_Evil","weap_rocket_launcher.acc.acc2")
    SetSkeletalMesh("gd_weap_rocket_launcher.acc.acc3_Corrosive","weap_rocket_launcher.acc.acc3")
    SetSkeletalMesh("gd_weap_rocket_launcher.acc.acc3_Shock","weap_rocket_launcher.acc.acc3")
    SetSkeletalMesh("gd_weap_rocket_launcher.acc.acc4_Devastating","weap_rocket_launcher.acc.acc4")
    SetSkeletalMesh("gd_weap_rocket_launcher.acc.acc5_Explosive","weap_rocket_launcher.acc.acc5")
    SetSkeletalMesh("gd_weap_rocket_launcher.acc.acc5_Incendiary","weap_rocket_launcher.acc.acc5")
        # Barrel
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel1_3shot","weap_rocket_launcher.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel1_helix","weap_rocket_launcher.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel1_spread","weap_rocket_launcher.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel1_triple","weap_rocket_launcher.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel1_Vladof_Mongol","weap_rocket_launcher.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel2_2shot","weap_rocket_launcher.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel2_Hyperion_Nidhogg","weap_rocket_launcher.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel2_Maliwan_Rhino","weap_rocket_launcher.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel4_1shot","weap_rocket_launcher.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_rocket_launcher.Barrel.barrel4_Torgue_Redemption","weap_rocket_launcher.Barrel.barrel4")
        # Body
    SetSkeletalMesh("gd_weap_rocket_launcher.Body.body1","weap_rocket_launcher.Body.body1")
    SetSkeletalMesh("gd_weap_rocket_launcher.Body.body3","weap_rocket_launcher.Body.body3")
    SetSkeletalMesh("gd_weap_rocket_launcher.Body.body5","weap_rocket_launcher.Body.body5")
        # Grip
    SetSkeletalMesh("gd_weap_rocket_launcher.Grip.grip1","weap_rocket_launcher.Grip.grip1")
    SetSkeletalMesh("gd_weap_rocket_launcher.Grip.grip2","weap_rocket_launcher.Grip.grip2")
    SetSkeletalMesh("gd_weap_rocket_launcher.Grip.grip3","weap_rocket_launcher.Grip.grip3")
    SetSkeletalMesh("gd_weap_rocket_launcher.Grip.grip3_Gearbox","weap_rocket_launcher.Grip.grip3")
    SetSkeletalMesh("gd_weap_rocket_launcher.Grip.grip4","weap_rocket_launcher.Grip.grip4")
    SetSkeletalMesh("gd_weap_rocket_launcher.Grip.grip5","weap_rocket_launcher.Grip.grip5")
        # Mag
    SetSkeletalMesh("gd_weap_rocket_launcher.mag.mag1","weap_rocket_launcher.mag.mag1")
    SetSkeletalMesh("gd_weap_rocket_launcher.mag.mag2","weap_rocket_launcher.mag.mag2")
    SetSkeletalMesh("gd_weap_rocket_launcher.mag.mag3","weap_rocket_launcher.mag.mag3")
    SetSkeletalMesh("gd_weap_rocket_launcher.mag.mag4","weap_rocket_launcher.mag.mag4")
    SetSkeletalMesh("gd_weap_rocket_launcher.mag.mag5","weap_rocket_launcher.mag.mag5")
        # Sight
    SetSkeletalMesh("gd_weap_rocket_launcher.Sight.sight1","weap_rocket_launcher.Sight.sight1")
    SetSkeletalMesh("gd_weap_rocket_launcher.Sight.sight2","weap_rocket_launcher.Sight.sight2")
    SetSkeletalMesh("gd_weap_rocket_launcher.Sight.sight3","weap_rocket_launcher.Sight.sight3")
    SetSkeletalMesh("gd_weap_rocket_launcher.Sight.sight4","weap_rocket_launcher.Sight.sight4")
    SetSkeletalMesh("gd_weap_rocket_launcher.Sight.sight5","weap_rocket_launcher.Sight.sight5")
        # Stock
    SetSkeletalMesh("gd_weap_rocket_launcher.Stock.stock1","weap_rocket_launcher.Stock.stock1")
    SetSkeletalMesh("gd_weap_rocket_launcher.Stock.stock2","weap_rocket_launcher.Stock.stock2")
    SetSkeletalMesh("gd_weap_rocket_launcher.Stock.stock3","weap_rocket_launcher.Stock.stock3")
    SetSkeletalMesh("gd_weap_rocket_launcher.Stock.stock4","weap_rocket_launcher.Stock.stock4")
    SetSkeletalMesh("gd_weap_rocket_launcher.Stock.stock5","weap_rocket_launcher.Stock.stock5")
        # UniqueParts
    SetSkeletalMesh("gd_weap_rocket_launcher.UniqueParts.Leviathan_barrel1_3shot","weap_rocket_launcher.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_rocket_launcher.UniqueParts.TheRoaster_acc5_Incendiary","weap_rocket_launcher.acc.acc5")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RocketLauncher.barrel2_TorgueUndertaker","weap_rocket_launcher.Barrel.barrel2")











    # Sniper Rifle 
    load_obj("WeaponTypeDefinition","gd_weap_sniper_rifle.A_Weapon.WeaponType_sniper_rifle").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_sniper_rifle.acc.acc1_Rolling","weap_sniper_rifle.acc.acc1")
    SetSkeletalMesh("gd_weap_sniper_rifle.acc.acc2_Explosive","weap_sniper_rifle.acc.acc2")
    SetSkeletalMesh("gd_weap_sniper_rifle.acc.acc2_Incendiary","weap_sniper_rifle.acc.acc2")
    SetSkeletalMesh("gd_weap_sniper_rifle.acc.acc2_Maliwan_Volcano_Incendiary","weap_sniper_rifle.acc.acc2")
    SetSkeletalMesh("gd_weap_sniper_rifle.acc.acc3_Corrosive","weap_sniper_rifle.acc.acc3")
    SetSkeletalMesh("gd_weap_sniper_rifle.acc.acc3_Shock","weap_sniper_rifle.acc.acc3")
    SetSkeletalMesh("gd_weap_sniper_rifle.acc.acc4_Heavy","weap_sniper_rifle.acc.acc4")
    SetSkeletalMesh("gd_weap_sniper_rifle.acc.acc5_Long","weap_sniper_rifle.acc.acc5")
        # Barrel
    SetSkeletalMesh("gd_weap_sniper_rifle.Barrel.barrel1","weap_sniper_rifle.Barrel.barrel1")
    SetSkeletalMesh("gd_weap_sniper_rifle.Barrel.barrel2","weap_sniper_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_sniper_rifle.Barrel.barrel2_Vladof_Surkov","weap_sniper_rifle.Barrel.barrel2")
    SetSkeletalMesh("gd_weap_sniper_rifle.Barrel.barrel3","weap_sniper_rifle.Barrel.barrel3")
    SetSkeletalMesh("gd_weap_sniper_rifle.Barrel.barrel4","weap_sniper_rifle.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_sniper_rifle.Barrel.barrel4_Jakobs_Skullmasher","weap_sniper_rifle.Barrel.barrel4")
    SetSkeletalMesh("gd_weap_sniper_rifle.Barrel.barrel5","weap_sniper_rifle.Barrel.barrel5")
        # Body
    SetSkeletalMesh("gd_weap_sniper_rifle.Body.body1","weap_sniper_rifle.Body.body1")
    SetSkeletalMesh("gd_weap_sniper_rifle.Body.body3","weap_sniper_rifle.Body.body3")
    SetSkeletalMesh("gd_weap_sniper_rifle.Body.body4","weap_sniper_rifle.Body.body4")
        # Grip
    SetSkeletalMesh("gd_weap_sniper_rifle.Grip.grip1","weap_sniper_rifle.Grip.grip1")
    SetSkeletalMesh("gd_weap_sniper_rifle.Grip.grip1a","weap_sniper_rifle.Grip.grip1")
    SetSkeletalMesh("gd_weap_sniper_rifle.Grip.grip2","weap_sniper_rifle.Grip.grip2")
    SetSkeletalMesh("gd_weap_sniper_rifle.Grip.grip2a_Torgue","weap_sniper_rifle.Grip.grip2")
    SetSkeletalMesh("gd_weap_sniper_rifle.Grip.grip3","weap_sniper_rifle.Grip.grip3")
    SetSkeletalMesh("gd_weap_sniper_rifle.Grip.grip3_Gearbox","weap_sniper_rifle.Grip.grip3")
    SetSkeletalMesh("gd_weap_sniper_rifle.Grip.grip4","weap_sniper_rifle.Grip.grip4")
    SetSkeletalMesh("gd_weap_sniper_rifle.Grip.grip5","weap_sniper_rifle.Grip.grip5")
        # Mag
    SetSkeletalMesh("gd_weap_sniper_rifle.mag.mag1","weap_sniper_rifle.mag.mag1")
    SetSkeletalMesh("gd_weap_sniper_rifle.mag.mag3","weap_sniper_rifle.mag.mag3")
    SetSkeletalMesh("gd_weap_sniper_rifle.mag.mag4","weap_sniper_rifle.mag.mag4")
        # Sight
    SetSkeletalMesh("gd_weap_sniper_rifle.Sight.sight1","weap_sniper_rifle.Sight.sight2")
    SetSkeletalMesh("gd_weap_sniper_rifle.Sight.sight2","weap_sniper_rifle.Sight.sight1")
    SetSkeletalMesh("gd_weap_sniper_rifle.Sight.sight3","weap_sniper_rifle.Sight.sight3")
    SetSkeletalMesh("gd_weap_sniper_rifle.Sight.sight4","weap_sniper_rifle.Sight.sight4")
    SetSkeletalMesh("gd_weap_sniper_rifle.Sight.sight5","weap_sniper_rifle.Sight.sight5")
    SetSkeletalMesh("gd_weap_sniper_rifle.Sight.sight5_Atlas_Cyclops","weap_sniper_rifle.Sight.sight5")
        # Stock
    SetSkeletalMesh("gd_weap_sniper_rifle.Stock.stock1","weap_sniper_rifle.Stock.stock1")
    SetSkeletalMesh("gd_weap_sniper_rifle.Stock.stock2","weap_sniper_rifle.Stock.stock2")
    SetSkeletalMesh("gd_weap_sniper_rifle.Stock.stock3","weap_sniper_rifle.Stock.stock3")
    SetSkeletalMesh("gd_weap_sniper_rifle.Stock.stock4","weap_sniper_rifle.Stock.stock4")
    SetSkeletalMesh("gd_weap_sniper_rifle.Stock.stock5","weap_sniper_rifle.Stock.stock5")
        # UniqueParts
    SetSkeletalMesh("gd_weap_sniper_rifle.UniqueParts.Nailer_barrel3","weap_sniper_rifle.Barrel.barrel3")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SniperRifle.sight4_Jakobs_Bessie","weap_sniper_rifle.Sight.sight4")




    # Semi Auto Sniper Rifle 
    load_obj("WeaponTypeDefinition","gd_weap_sniper_rifle_semiauto.A_Weapon.WeaponType_sniper_rifle_semiauto").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.acc.acc1_Brisk","weap_sniper_rifle.acc.acc1")
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.acc.acc2_Explosive_Torgue_Cobra","weap_sniper_rifle.acc.acc2")
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.acc.acc3_SandS_Orion_Shock","weap_sniper_rifle.acc.acc3")
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.acc.acc4_Deep","weap_sniper_rifle.acc.acc4")
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.acc.acc5_Sober","weap_sniper_rifle.acc.acc5")
        # Barrel
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.Barrel.barrel1_Dahl_Penetrator","weap_sniper_rifle.Barrel.barrel1")
        # Body
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.Body.body2","weap_sniper_rifle.Body.body2")
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.Body.body5","weap_sniper_rifle.Body.body5")
        # Mag
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.mag.mag2","weap_sniper_rifle.mag.mag2")
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.mag.mag5","weap_sniper_rifle.mag.mag5")
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.mag.mag5_Hyperion_Executioner","weap_sniper_rifle.mag.mag5")
        # UniqueParts
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.UniqueParts.ReaversEdge_sight4","weap_sniper_rifle.Sight.sight4")
    SetSkeletalMesh("gd_weap_sniper_rifle_semiauto.UniqueParts.Ryder_mag5","weap_sniper_rifle.mag.mag5")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SemiAutoSniper.acc2_KyrosPower","weap_sniper_rifle.acc.acc2")


    # Support Machine Gun 
    load_obj("WeaponTypeDefinition","gd_weap_support_machinegun.A_Weapon.WeaponType_support_machinegun").gestaltmesh = None
        # Acc
    SetSkeletalMesh("gd_weap_support_machinegun.acc.acc1_Frantic","weap_combat_rifle.acc.acc1")
    SetSkeletalMesh("gd_weap_support_machinegun.acc.acc1_Shattering","weap_combat_rifle.acc.acc1")
    SetSkeletalMesh("gd_weap_support_machinegun.acc.acc4_SandS_Draco_Incendiary","weap_combat_rifle.acc.acc4")
    SetSkeletalMesh("gd_weap_support_machinegun.acc.acc5_Atlas_Ogre_Explosive","weap_combat_rifle.acc.acc5")
        # Barrel
    SetSkeletalMesh("gd_weap_support_machinegun.Barrel.barrel4_Torgue_Bastard","weap_combat_rifle.Barrel.barrel4")
        # Mag
    SetSkeletalMesh("gd_weap_support_machinegun.mag.mag2","weap_combat_rifle.mag.mag2")
    SetSkeletalMesh("gd_weap_support_machinegun.mag.mag4","weap_combat_rifle.mag.mag4")
    SetSkeletalMesh("gd_weap_support_machinegun.mag.mag5","weap_combat_rifle.mag.mag5")
    SetSkeletalMesh("gd_weap_support_machinegun.mag.mag5_VladofRevolution","weap_combat_rifle.mag.mag5")
        # Sight
    SetSkeletalMesh("gd_weap_support_machinegun.Sight.sight1","weap_combat_rifle.Sight.sight1")
    SetSkeletalMesh("gd_weap_support_machinegun.Sight.sight2","weap_combat_rifle.Sight.sight2")
    SetSkeletalMesh("gd_weap_support_machinegun.Sight.sight3","weap_combat_rifle.Sight.sight3")
        # UniqueParts
    SetSkeletalMesh("gd_weap_support_machinegun.UniqueParts.TheMeatGringer_mag5","weap_combat_rifle.mag.mag5")

    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SupportMachineGun.acc4_SandS_Serpens","weap_combat_rifle.acc.acc4")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SupportMachineGun.acc4_TheChopper","weap_combat_rifle.acc.acc4")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SupportMachineGun.barrel5_AjaxSpear","weap_combat_rifle.Barrel.barrel5")


    # DLC Weapons
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.CombatRifle.TedioreAvenger_sight5","weap_combat_rifle.Sight.sight5")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.CombatShotgun.barrel3_DahlJackal","weap_combat_shotgun.Barrel.barrel3")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.Cannon.barrel5_MegaCannon","weap_alien_rifle.Barrel.barrel5")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_Fireball","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_Firebomb","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_Flaregun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_GlobGun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_RollingSpattergun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_Splatgun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel2_StampedingSpattergun","weap_alien_rifle.Barrel.barrel2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.EridanRifle.ElementalRifle.barrel3_Rifle","weap_alien_rifle.Barrel.barrel3")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.MachinePistol.barrel4_VladofStalker","weap_repeater_pistol.Barrel.barrel4")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RepeaterPistol.acc5_Shock_HyperionNemesis","weap_repeater_pistol.acc.acc5")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RepeaterPistol.barrel0_ChiquitoAmigo","weap_repeater_pistol.Barrel.barrel0")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RepeaterPistol.barrel5_AthenasWisdom","weap_repeater_pistol.Barrel.barrel5")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RevolverPistol.acc5_Heal_AtlasAries","weap_revolver_pistol.acc.acc3")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.RocketLauncher.barrel2_TorgueUndertaker","weap_rocket_launcher.Barrel.barrel3")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SemiAutoSniper.acc2_KyrosPower","weap_sniper_rifle.acc.acc2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SMG.acc2_Typhoon","weap_patrol_smg.acc.acc2")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SMG.acc3_Maliwan_Tsunami","weap_patrol_smg.acc.acc3")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SniperRifle.sight4_Jakobs_Bessie","weap_sniper_rifle.Sight.sight4")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SupportMachineGun.acc4_SandS_Serpens","weap_combat_rifle.acc.acc4")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SupportMachineGun.acc4_TheChopper","weap_combat_rifle.acc.acc4")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SupportMachineGun.barrel5_AjaxSpear","weap_combat_rifle.Barrel.barrel5")
    SetSkeletalMesh("dlc3_gd_weap_UniqueParts.SniperRifle.sight4_Jakobs_Bessie","weap_sniper_rifle.Sight.sight4")






    # Stock Weapons 
    load_obj("WeaponTypeDefinition","gd_weap_stock_weapons.A_Weapon.WeaponType_combat_shotgun_stock").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_stock_weapons.A_Weapon.WeaponType_machine_pistol_stock").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_stock_weapons.A_Weapon.WeaponType_patrol_smg_stock").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_stock_weapons.A_Weapon.WeaponType_repeater_pistol_stock").gestaltmesh = None
    load_obj("WeaponTypeDefinition","gd_weap_stock_weapons.A_Weapon.WeaponType_support_machinegun_stock").gestaltmesh = None





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


@hook(
    hook_func="WillowGame.WillowWeapon:InitMeshes",
    hook_type=Type.POST,
)
def InitMeshes(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    count = 0
    if obj.firstpersonmesh is None or obj.firstpersonmesh.skeletalmesh is None:
        return
    for mat in obj.firstpersonmesh.skeletalmesh.materials:
        count = count + 1

        newmat = unrealsdk.construct_object("MaterialInstanceConstant", obj)
        newmat.SetParent(mat)
        obj.InitInventoryMaterial(obj.DefinitionData.WeaponTypeDefinition, obj.WeaponMaterial, newmat)
        obj.FirstPersonMesh.SetMaterial(count - 1, newmat)
        obj.ThirdPersonMesh.SetMaterial(count - 1, newmat)
        obj.PickupMesh.SetMaterial(count - 1, newmat)



# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    keybinds=[],
    hooks=[on_startgame, InitMeshes],
    commands=[],
)