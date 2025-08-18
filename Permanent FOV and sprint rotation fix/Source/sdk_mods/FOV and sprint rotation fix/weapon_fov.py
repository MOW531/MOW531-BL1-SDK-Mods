import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command, ENGINE
from mods_base.options import BaseOption, SliderOption


def obj (definition:str, object:str):
    object_class = unrealsdk.find_class(definition)
    current_obj = ENGINE.DynamicLoadObject(object, object_class, False)
    current_obj.ObjectFlags |= 0x4000
    return current_obj





def Set_weapon_FOV():
    obj("WeaponTypeDefinition","gd_weap_revolver_pistol.A_Weapon.WeaponType_revolver_pistol").FirstPersonMeshFOV = RepeaterFOV.value
    obj("WeaponTypeDefinition","gd_weap_assault_shotgun.A_Weapon.WeaponType_assault_shotgun").FirstPersonMeshFOV = AssaultShotgunFOV.value
    obj("WeaponTypeDefinition","gd_weap_combat_rifle.A_Weapon.WeaponType_combat_rifle").FirstPersonMeshFOV = CombatRifleFOV.value
    obj("WeaponTypeDefinition","gd_weap_combat_shotgun.A_Weapon.WeaponType_combat_shotgun").FirstPersonMeshFOV = CombatShotgunFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Acid_Storm").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Blaster").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Launcher.a_weap.WeaponType_Eridan_Cannon").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Rifle.a_weap.WeaponType_Eridan_Elementalgun").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Fire_Storm").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Sniper.a_weap.WeaponType_Eridan_Lightning").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Rifle").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Riflede").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Shotgun.a_weap.WeaponType_Eridan_ShockGun").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Sniperde").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Shotgun.a_weap.WeaponType_Eridan_Thunder_Storm").FirstPersonMeshFOV = AlienFOV.value
    obj("WeaponTypeDefinition","gd_weap_grenade_launcher.A_Weapon.WeaponType_grenade_launcher").FirstPersonMeshFOV = GrenadeLauncherFOV.value
    obj("WeaponTypeDefinition","gd_weap_machine_pistol.A_Weapon.WeaponType_machine_pistol").FirstPersonMeshFOV = MachinePistolFOV.value
    obj("WeaponTypeDefinition","gd_weap_patrol_smg.A_Weapon.WeaponType_patrol_smg").FirstPersonMeshFOV = PatrolSMGFOV.value
    obj("WeaponTypeDefinition","gd_weap_repeater_pistol.A_Weapon.WeaponType_repeater_pistol").FirstPersonMeshFOV = RepeaterFOV.value
    obj("WeaponTypeDefinition","gd_weap_rocket_launcher.A_Weapon.WeaponType_rocket_launcher").FirstPersonMeshFOV = RocketLauncherFOV.value
    obj("WeaponTypeDefinition","gd_weap_sniper_rifle.A_Weapon.WeaponType_sniper_rifle").FirstPersonMeshFOV = SniperRifleFOV.value
    obj("WeaponTypeDefinition","gd_weap_sniper_rifle_semiauto.A_Weapon.WeaponType_sniper_rifle_semiauto").FirstPersonMeshFOV = SniperRifleSemiAutoFOV.value
    obj("WeaponTypeDefinition","gd_weap_support_machinegun.A_Weapon.WeaponType_support_machinegun").FirstPersonMeshFOV = SupportMachinegunFOV.value

def Set_Revolver_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_revolver_pistol.A_Weapon.WeaponType_revolver_pistol").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_Repeater_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_repeater_pistol.A_Weapon.WeaponType_repeater_pistol").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_MachinePistol_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_machine_pistol.A_Weapon.WeaponType_machine_pistol").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_AssaultShotgun_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_assault_shotgun.A_Weapon.WeaponType_assault_shotgun").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_CombatShotgun_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_combat_shotgun.A_Weapon.WeaponType_combat_shotgun").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_CombatRifle_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_combat_rifle.A_Weapon.WeaponType_combat_rifle").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_GrenadeLauncher_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_grenade_launcher.A_Weapon.WeaponType_grenade_launcher").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_RocketLauncher_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_rocket_launcher.A_Weapon.WeaponType_rocket_launcher").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_SniperRifle_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_sniper_rifle.A_Weapon.WeaponType_sniper_rifle").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_SniperRifleSemiAuto_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_sniper_rifle_semiauto.A_Weapon.WeaponType_sniper_rifle_semiauto").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_SupportMachinegun_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_support_machinegun.A_Weapon.WeaponType_support_machinegun").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_PatrolSMG_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_patrol_smg.A_Weapon.WeaponType_patrol_smg").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV


def Set_Alien_FOV(option:BaseOption, value:float):
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Acid_Storm").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Blaster").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Launcher.a_weap.WeaponType_Eridan_Cannon").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Rifle.a_weap.WeaponType_Eridan_Elementalgun").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Fire_Storm").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Sniper.a_weap.WeaponType_Eridan_Lightning").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Rifle").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Riflede").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Shotgun.a_weap.WeaponType_Eridan_ShockGun").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Sniperde").FirstPersonMeshFOV = value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Shotgun.a_weap.WeaponType_Eridan_Thunder_Storm").FirstPersonMeshFOV = value
    pc = get_pc()
    if pc is not None and pc.pawn is not None and pc.pawn.weapon is not None and pc.pawn.weapon.definitiondata is not None and pc.pawn.weapon.definitiondata.weapontypedefinition is not None:
        pc.ForegroundFOV = pc.pawn.weapon.definitiondata.weapontypedefinition.FirstPersonMeshFOV



RevolverFOV = SliderOption("Revolver FOV", 55, 30, 100, 1, True, on_change=Set_Revolver_FOV)
RepeaterFOV = SliderOption("Repeater FOV", 55, 30, 100, 1, True, on_change=Set_Repeater_FOV)
MachinePistolFOV = SliderOption("Machine Pistol FOV", 55, 30, 100, 1, True, on_change=Set_MachinePistol_FOV)
AssaultShotgunFOV = SliderOption("Assault Shotgun FOV", 55, 30, 100, 1, True, on_change=Set_AssaultShotgun_FOV)
CombatShotgunFOV = SliderOption("Combat Shotgun FOV", 55, 30, 100, 1, True, on_change=Set_CombatShotgun_FOV)
CombatRifleFOV = SliderOption("Combat Rifle FOV", 55, 30, 100, 1, True, on_change=Set_CombatRifle_FOV)
GrenadeLauncherFOV = SliderOption("Grenade Launcher FOV", 55, 30, 100, 1, True, on_change=Set_GrenadeLauncher_FOV)
RocketLauncherFOV = SliderOption("Rocket Launcher FOV", 55, 30, 100, 1, True, on_change=Set_RocketLauncher_FOV)
SniperRifleFOV = SliderOption("Sniper Rifle FOV", 55, 30, 100, 1, True, on_change=Set_SniperRifle_FOV)
SniperRifleSemiAutoFOV = SliderOption("Semi-auto Sniper Rifle FOV", 55, 30, 100, 1, True, on_change=Set_SniperRifleSemiAuto_FOV)
SupportMachinegunFOV = SliderOption("Support Machinegun FOV", 55, 30, 100, 1, True, on_change=Set_SupportMachinegun_FOV)
PatrolSMGFOV = SliderOption("SMG FOV", 55, 30, 100, 1, True, on_change=Set_PatrolSMG_FOV)
AlienFOV = SliderOption("Eridian FOV", 55, 30, 100, 1, True, on_change=Set_Alien_FOV)

@hook(
    hook_func="Engine.WorldInfo:IsMenuLevel",
    hook_type=Type.PRE,
)
def on_startgame_weapon(
    __obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    Set_weapon_FOV()