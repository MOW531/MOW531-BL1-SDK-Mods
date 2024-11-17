import argparse

import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, EInputEvent, keybind, command
from mods_base.options import BaseOption, SliderOption

RevolverFOV = SliderOption("Revolver FOV", 55, 0, 160, 1, True)
RepeaterFOV = SliderOption("Repeater FOV", 55, 0, 160, 1, True)
MachinePistolFOV = SliderOption("Machine Pistol FOV", 55, 0, 160, 1, True)
assaultshotgunFOV = SliderOption("Assault Shotgun FOV", 55, 0, 160, 1, True)
combatshotgunFOV = SliderOption("Combat Shotgun FOV", 55, 0, 160, 1, True)
combatrifleFOV = SliderOption("Combat Rifle FOV", 55, 0, 160, 1, True)
grenadelauncherFOV = SliderOption("Grenade Launcher FOV", 55, 0, 160, 1, True)
rocketlauncherFOV = SliderOption("Rocket Launcher FOV", 55, 0, 160, 1, True)
sniperrifleFOV = SliderOption("Sniper Rifle FOV", 55, 0, 160, 1, True)
sniperriflesemiautoFOV = SliderOption("Semi-auto Sniper Rifle FOV", 55, 0, 160, 1, True)
supportmachinegunFOV = SliderOption("Support Machinegun FOV", 55, 0, 160, 1, True)
patrolsmgFOV = SliderOption("SMG FOV", 55, 0, 160, 1, True)
alienFOV = SliderOption("Eridian FOV", 55, 0, 160, 1, True)


@hook(
    hook_func="WillowGame.WillowPlayerController:AdjustFOV",
    hook_type=Type.POST,
)
def SetWeaponFOV(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    for controllers in unrealsdk.find_all("WillowPlayerController"):
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
                    controllers.foregroundFOV = RevolverFOV.value
                elif (repeater_pistol > -1):
                    controllers.foregroundFOV = RepeaterFOV.value
                elif (machine_pistol > -1):
                    controllers.foregroundFOV = MachinePistolFOV.value
                elif (assault_shotgun > -1):
                    controllers.foregroundFOV = assaultshotgunFOV.value
                elif (combat_shotgun > -1):
                    controllers.foregroundFOV = combatshotgunFOV.value
                elif (combat_rifle > -1):
                    controllers.foregroundFOV = combatrifleFOV.value
                elif (grenade_launcher > -1):
                    controllers.foregroundFOV = grenadelauncherFOV.value
                elif (rocket_launcher > -1):
                    controllers.foregroundFOV = rocketlauncherFOV.value
                elif (sniper_rifle > -1):
                    controllers.foregroundFOV = sniperrifleFOV.value
                elif (sniper_rifle_semiauto > -1):
                    controllers.foregroundFOV = sniperriflesemiautoFOV.value
                elif (support_machinegun > -1):
                    controllers.foregroundFOV = supportmachinegunFOV.value
                elif (patrol_smg > -1):
                    controllers.foregroundFOV = patrolsmgFOV.value
                else:
                    controllers.foregroundFOV = alienFOV.value
