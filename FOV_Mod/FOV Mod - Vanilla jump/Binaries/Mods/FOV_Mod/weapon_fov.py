import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command
from mods_base.options import BaseOption, SliderOption

current_obj = None

def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)

def SetWeaponFOV(option:BaseOption, value:float):
    


    obj("WeaponTypeDefinition","gd_weap_assault_shotgun.A_Weapon.WeaponType_assault_shotgun").FirstPersonMeshFOV = assaultshotgunFOV.value
    obj("WeaponTypeDefinition","gd_weap_combat_rifle.A_Weapon.WeaponType_combat_rifle").FirstPersonMeshFOV = combatrifleFOV.value
    obj("WeaponTypeDefinition","gd_weap_combat_shotgun.A_Weapon.WeaponType_combat_shotgun").FirstPersonMeshFOV = combatshotgunFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Acid_Storm").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Blaster").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Launcher.a_weap.WeaponType_Eridan_Cannon").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Rifle.a_weap.WeaponType_Eridan_Elementalgun").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_SMG.a_weap.WeaponType_Eridan_Fire_Storm").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Sniper.a_weap.WeaponType_Eridan_Lightning").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Rifle").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Riflede").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Shotgun.a_weap.WeaponType_Eridan_ShockGun").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.DELETEDELETE.WeaponType_Eridan_Sniperde").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_alien_rifle.A_Shotgun.a_weap.WeaponType_Eridan_Thunder_Storm").FirstPersonMeshFOV = alienFOV.value
    obj("WeaponTypeDefinition","gd_weap_grenade_launcher.A_Weapon.WeaponType_grenade_launcher").FirstPersonMeshFOV = grenadelauncherFOV.value
    obj("WeaponTypeDefinition","gd_weap_machine_pistol.A_Weapon.WeaponType_machine_pistol").FirstPersonMeshFOV = MachinePistolFOV.value
    obj("WeaponTypeDefinition","gd_weap_patrol_smg.A_Weapon.WeaponType_patrol_smg").FirstPersonMeshFOV = patrolsmgFOV.value
    obj("WeaponTypeDefinition","gd_weap_repeater_pistol.A_Weapon.WeaponType_repeater_pistol").FirstPersonMeshFOV = RepeaterFOV.value
    obj("WeaponTypeDefinition","gd_weap_rocket_launcher.A_Weapon.WeaponType_rocket_launcher").FirstPersonMeshFOV = rocketlauncherFOV.value
    obj("WeaponTypeDefinition","gd_weap_sniper_rifle.A_Weapon.WeaponType_sniper_rifle").FirstPersonMeshFOV = sniperrifleFOV.value
    obj("WeaponTypeDefinition","gd_weap_sniper_rifle_semiauto.A_Weapon.WeaponType_sniper_rifle_semiauto").FirstPersonMeshFOV = sniperriflesemiautoFOV.value
    obj("WeaponTypeDefinition","gd_weap_support_machinegun.A_Weapon.WeaponType_support_machinegun").FirstPersonMeshFOV = supportmachinegunFOV.value

    if get_pc().pawn != None:
        if get_pc().pawn.weapon != None:
            weapon = str(get_pc().pawn.weapon.definitiondata)
            revolver_pistol = weapon.find("WeaponType_revolver_pistol")
            repeater_pistol = weapon.find("WeaponType_repeater_pistol")
            machine_pistol = weapon.find("WeaponType_machine_pistol")
            assault_shotgun = weapon.find("WeaponType_assault_shotgun")
            combat_shotgun = weapon.find("WeaponType_combat_shotgun")
            combat_rifle = weapon.find("WeaponType_combat_rifle")
            grenade_launcher = weapon.find("WeaponType_grenade_launcher")
            rocket_launcher = weapon.find("WeaponType_rocket_launcher")
            sniper_rifle = weapon.find("WeaponType_sniper_rifle'")
            sniper_rifle_semiauto = weapon.find("WeaponType_sniper_rifle_semiauto'")
            support_machinegun = weapon.find("WeaponType_support_machinegun")
            patrol_smg = weapon.find("WeaponType_patrol_smg")


            if (revolver_pistol > -1):
                get_pc().foregroundFOV = RevolverFOV.value
            elif (repeater_pistol > -1):
                get_pc().foregroundFOV = RepeaterFOV.value
            elif (machine_pistol > -1):
                get_pc().foregroundFOV = MachinePistolFOV.value
            elif (assault_shotgun > -1):
                get_pc().foregroundFOV = assaultshotgunFOV.value
            elif (combat_shotgun > -1):
                get_pc().foregroundFOV = combatshotgunFOV.value
            elif (combat_rifle > -1):
                get_pc().foregroundFOV = combatrifleFOV.value
            elif (grenade_launcher > -1):
                get_pc().foregroundFOV = grenadelauncherFOV.value
            elif (rocket_launcher > -1):
                get_pc().foregroundFOV = rocketlauncherFOV.value
            elif (sniper_rifle > -1):
                get_pc().foregroundFOV = sniperrifleFOV.value
            elif (sniper_rifle_semiauto > -1):
                get_pc().foregroundFOV = sniperriflesemiautoFOV.value
            elif (support_machinegun > -1):
                get_pc().foregroundFOV = supportmachinegunFOV.value
            elif (patrol_smg > -1):
                get_pc().foregroundFOV = patrolsmgFOV.value
            else:
                get_pc().foregroundFOV = alienFOV.value




RevolverFOV = SliderOption("Revolver FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
RepeaterFOV = SliderOption("Repeater FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
MachinePistolFOV = SliderOption("Machine Pistol FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
assaultshotgunFOV = SliderOption("Assault Shotgun FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
combatshotgunFOV = SliderOption("Combat Shotgun FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
combatrifleFOV = SliderOption("Combat Rifle FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
grenadelauncherFOV = SliderOption("Grenade Launcher FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
rocketlauncherFOV = SliderOption("Rocket Launcher FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
sniperrifleFOV = SliderOption("Sniper Rifle FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
sniperriflesemiautoFOV = SliderOption("Semi-auto Sniper Rifle FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
supportmachinegunFOV = SliderOption("Support Machinegun FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
patrolsmgFOV = SliderOption("SMG FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)
alienFOV = SliderOption("Eridian FOV", 55, 0, 160, 1, True, on_change=SetWeaponFOV)


@hook(
    hook_func="WillowGame.WillowPawn:WeaponChanged",
    hook_type=Type.POST,
)
def WeaponActionComplete(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    if get_pc().pawn != None:
        if get_pc().pawn.weapon != None:
            weapon = str(get_pc().pawn.weapon.definitiondata)
            revolver_pistol = weapon.find("WeaponType_revolver_pistol")
            repeater_pistol = weapon.find("WeaponType_repeater_pistol")
            machine_pistol = weapon.find("WeaponType_machine_pistol")
            assault_shotgun = weapon.find("WeaponType_assault_shotgun")
            combat_shotgun = weapon.find("WeaponType_combat_shotgun")
            combat_rifle = weapon.find("WeaponType_combat_rifle")
            grenade_launcher = weapon.find("WeaponType_grenade_launcher")
            rocket_launcher = weapon.find("WeaponType_rocket_launcher")
            sniper_rifle = weapon.find("WeaponType_sniper_rifle'")
            sniper_rifle_semiauto = weapon.find("WeaponType_sniper_rifle_semiauto'")
            support_machinegun = weapon.find("WeaponType_support_machinegun")
            patrol_smg = weapon.find("WeaponType_patrol_smg")


            if (revolver_pistol > -1):
                get_pc().foregroundFOV = RevolverFOV.value
            elif (repeater_pistol > -1):
                get_pc().foregroundFOV = RepeaterFOV.value
            elif (machine_pistol > -1):
                get_pc().foregroundFOV = MachinePistolFOV.value
            elif (assault_shotgun > -1):
                get_pc().foregroundFOV = assaultshotgunFOV.value
            elif (combat_shotgun > -1):
                get_pc().foregroundFOV = combatshotgunFOV.value
            elif (combat_rifle > -1):
                get_pc().foregroundFOV = combatrifleFOV.value
            elif (grenade_launcher > -1):
                get_pc().foregroundFOV = grenadelauncherFOV.value
            elif (rocket_launcher > -1):
                get_pc().foregroundFOV = rocketlauncherFOV.value
            elif (sniper_rifle > -1):
                get_pc().foregroundFOV = sniperrifleFOV.value
            elif (sniper_rifle_semiauto > -1):
                get_pc().foregroundFOV = sniperriflesemiautoFOV.value
            elif (support_machinegun > -1):
                get_pc().foregroundFOV = supportmachinegunFOV.value
            elif (patrol_smg > -1):
                get_pc().foregroundFOV = patrolsmgFOV.value
            else:
                get_pc().foregroundFOV = alienFOV.value
