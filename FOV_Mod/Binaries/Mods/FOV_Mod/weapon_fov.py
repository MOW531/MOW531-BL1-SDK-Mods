import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command
from mods_base.options import BaseOption, SliderOption


def SetWeaponFOV(option:BaseOption, value:float):
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