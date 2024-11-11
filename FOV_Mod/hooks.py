import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc 
from mods_base.options import BaseOption, SliderOption


def set_fov(option:BaseOption, value:float):
    global FOV
    FOV = value
    pc = get_pc()
    pc.SetFOV(FOV)

    if pc.pawn != None:

        pc.CharacterClass.FOV = FOV

        Vehicle = (str(pc.pawn.objectarchetype).find("Vehicle"))

        if Vehicle != -1:
            Cheetah_Paw = (str(pc.pawn.objectarchetype).find("DLC3_Cheetah_Paw"))

            if Cheetah_Paw > -1:
                 pc.Pawn.AfterburnerMaxFOV = (FOV + 10)
            else:
                  pc.Pawn.AfterburnerMaxFOV = (FOV + 20)


def set_revolver_pistol_fov(option:BaseOption, value:float):
    global Revolver_pistol_FOV
    Revolver_pistol_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        revolver_pistol = (str(pc.pawn.weapon.definitiondata).find("WeaponType_revolver_pistol"))
        if (revolver_pistol > -1):
            pc.foregroundFOV = Revolver_pistol_FOV

def set_repeater_pistol_fov(option:BaseOption, value:float):
    global Repeater_pistol_FOV
    Repeater_pistol_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        repeater_pistol = (str(pc.pawn.weapon.definitiondata).find("WeaponType_repeater_pistol"))
        if (repeater_pistol > -1):
            pc.foregroundFOV = Repeater_pistol_FOV

def set_machine_pistol_fov(option:BaseOption, value:float):
    global Machine_pistol_FOV
    Machine_pistol_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        machine_pistol = (str(pc.pawn.weapon.definitiondata).find("WeaponType_machine_pistol"))
        if (machine_pistol > -1):
            pc.foregroundFOV = Machine_pistol_FOV

def set_assault_shotgun_fov(option:BaseOption, value:float):
    global Assault_shotgun_FOV
    Assault_shotgun_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        assault_shotgun = (str(pc.pawn.weapon.definitiondata).find("WeaponType_assault_shotgun"))
        if (assault_shotgun > -1):
            pc.foregroundFOV = Assault_shotgun_FOV

def set_combat_shotgun_fov(option:BaseOption, value:float):
    global Combat_shotgun_FOV
    Combat_shotgun_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        combat_shotgun = (str(pc.pawn.weapon.definitiondata).find("WeaponType_combat_shotgun"))
        if (combat_shotgun > -1):
            pc.foregroundFOV = Combat_shotgun_FOV

def set_combat_rifle_fov(option:BaseOption, value:float):
    global Combat_rifle_FOV
    Combat_rifle_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        combat_rifle = (str(pc.pawn.weapon.definitiondata).find("WeaponType_combat_rifle"))
        if (combat_rifle > -1):
            pc.foregroundFOV = Combat_rifle_FOV

def set_grenade_launcher_fov(option:BaseOption, value:float):
    global Grenade_launcher_FOV
    Grenade_launcher_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        grenade_launcher = (str(pc.pawn.weapon.definitiondata).find("WeaponType_grenade_launcher"))
        if (grenade_launcher > -1):
            pc.foregroundFOV = Grenade_launcher_FOV

def set_rocket_launcher_fov(option:BaseOption, value:float):
    global Rocket_launcher_FOV
    Rocket_launcher_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        rocket_launcher = (str(pc.pawn.weapon.definitiondata).find("WeaponType_rocket_launcher"))
        if (rocket_launcher > -1):
            pc.foregroundFOV = Rocket_launcher_FOV

def set_sniper_rifle_fov(option:BaseOption, value:float):
    global Sniper_rifle_FOV
    Sniper_rifle_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        sniper_rifle = (str(pc.pawn.weapon.definitiondata).find("WeaponType_sniper_rifle'"))
        if (sniper_rifle > -1):
            pc.foregroundFOV = Sniper_rifle_FOV

def set_sniper_rifle_semiauto_fov(option:BaseOption, value:float):
    global Sniper_rifle_semiauto_FOV
    Sniper_rifle_semiauto_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        sniper_rifle_semiauto = (str(pc.pawn.weapon.definitiondata).find("WeaponType_sniper_rifle_semiauto'"))
        if (sniper_rifle_semiauto > -1):
            pc.foregroundFOV = Sniper_rifle_semiauto_FOV

def set_support_machinegun_fov(option:BaseOption, value:float):
    global Support_machinegun_FOV
    Support_machinegun_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        support_machinegun = (str(pc.pawn.weapon.definitiondata).find("WeaponType_support_machinegun"))
        if (support_machinegun > -1):
            pc.foregroundFOV = Support_machinegun_FOV

def set_patrol_smg_fov(option:BaseOption, value:float):
    global Patrol_smg_FOV
    Patrol_smg_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        patrol_smg = (str(pc.pawn.weapon.definitiondata).find("WeaponType_patrol_smg"))
        if (patrol_smg > -1):
            pc.foregroundFOV = Patrol_smg_FOV

def set_alien_fov(option:BaseOption, value:float):
    global Alien_FOV
    Alien_FOV = value
    if get_pc().pawn != None:
        pc = get_pc()
        Alien = (str(pc.pawn.weapon.definitiondata).find("Eridan"))
        if (Alien > -1):
            pc.foregroundFOV = Alien_FOV




fov_setting = SliderOption("World FOV", 70, 0, 999, 1, True, on_change=set_fov)

revolver_pistol_fov_setting = SliderOption("Revolver FOV", 55, 0, 999, 1, True, on_change=set_revolver_pistol_fov)
repeater_pistol_setting = SliderOption("Repeater FOV", 55, 0, 999, 1, True, on_change=set_repeater_pistol_fov)
machine_pistol_setting = SliderOption("Machine Pistol FOV", 55, 0, 999, 1, True, on_change=set_machine_pistol_fov)
assault_shotgun_setting = SliderOption("Assault Shotgun FOV", 55, 0, 999, 1, True, on_change=set_assault_shotgun_fov)
combat_shotgun_setting = SliderOption("Combat Shotgun FOV", 55, 0, 999, 1, True, on_change=set_combat_shotgun_fov)
combat_rifle_setting = SliderOption("Combat Rifle FOV", 55, 0, 999, 1, True, on_change=set_combat_rifle_fov)
grenade_launcher_setting = SliderOption("Grenade Launcher FOV", 55, 0, 999, 1, True, on_change=set_grenade_launcher_fov)
rocket_launcher_setting = SliderOption("Rocket Launcher FOV", 55, 0, 999, 1, True, on_change=set_rocket_launcher_fov)
sniper_rifle_setting = SliderOption("Sniper Rifle FOV", 55, 0, 999, 1, True, on_change=set_sniper_rifle_fov)
sniper_rifle_semiauto_setting = SliderOption("Semi-auto Sniper Rifle FOV", 55, 0, 999, 1, True, on_change=set_sniper_rifle_semiauto_fov)
support_machinegun_setting = SliderOption("Support Machinegun FOV", 55, 0, 999, 1, True, on_change=set_support_machinegun_fov)
patrol_smg_setting = SliderOption("SMG FOV", 55, 0, 999, 1, True, on_change=set_patrol_smg_fov)
alien_setting = SliderOption("Eridian FOV", 55, 0, 999, 1, True, on_change=set_alien_fov)


@hook(
    hook_func="WillowGame.WillowPlayerController:SpawningProcessComplete",
    hook_type=Type.POST,
)
def on_player_loaded(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    pc = get_pc()
    pc.DesiredFOVBaseValue = FOV
    pc.DesiredFOV = FOV
    MordacaiMelee = unrealsdk.find_object("InterpTrackFloatProp", "weap_camera_animations.Melee.melee_mordacai:InterpGroup_2.InterpTrackFloatProp_0")
    MordacaiMelee.PropertyName = "a"
    LilithMelee = unrealsdk.find_object("InterpTrackFloatProp", "weap_camera_animations.Melee.melee_lilith:InterpGroup_3.InterpTrackFloatProp_0")
    LilithMelee.PropertyName = "a"

    Sprint = unrealsdk.find_object("SkillDefinition", "gd_skills_common.Basic.DoubleTime")
    Sprint.SkillEffectDefinitions[5].ModifierType = 2
    Sprint.SkillEffectDefinitions[5].BaseModifierValue.BaseValueConstant = 0
    SprintLimit = unrealsdk.find_object("AttributeExpressionEvaluator", "gd_skills_common.Basic.DoubleTime:ExpressionTree_4.AttributeExpressionEvaluator_25")
    SprintLimit.Expression.ConstantOperand2 = 0.00001

@hook(
    hook_func="WillowGame.WillowPlayerController:BeginSprint",
    hook_type=Type.POST,
)
def on_player_begin_sprint(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    pc = get_pc()
    if pc.pawn.bIsSprinting == 1:
        pc.DesiredFOVBaseValue = FOV + 15
        pc.DesiredFOV = FOV + 15


@hook(
    hook_func="WillowGame.WillowPlayerController:EndSprint",
    hook_type=Type.POST,
)
def on_player_end_sprint(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    pc = get_pc()
    pc.DesiredFOVBaseValue = FOV
    pc.DesiredFOV = FOV

@hook(
    hook_func="WillowGame.WillowVehicle:DriverLeave",
    hook_type=Type.POST,
)
def on_player_leave_car(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    pc = get_pc()
    pc.DesiredFOVBaseValue = FOV
    pc.DesiredFOV = FOV


    weapon = str(pc.pawn.weapon.definitiondata)

    revolver_pistol = weapon.find("WeaponType_revolver_pistol")
    repeater_pistol = weapon.find("WeaponType_repeater_pistol")
    machine_pistol = weapon.find("WeaponType_machine_pistol")
    assault_shotgun = weapon.find("WeaponType_assault_shotgun")
    combat_shotgun = weapon.find("WeaponType_combat_shotgun")
    combat_rifle = weapon.find("WeaponType_combat_rifle")
    grenade_launcher = weapon.find("WeaponType_grenade_launcher")
    rocket_launcher = weapon.find("WeaponType_rocket_launcher")
    sniper_rifle = weapon.find("WeaponType_sniper_rifle")
    sniper_rifle_semiauto = weapon.find("WeaponType_sniper_rifle_semiauto")
    support_machinegun = weapon.find("WeaponType_support_machinegun")
    patrol_smg = weapon.find("WeaponType_patrol_smg")


    if (revolver_pistol > -1):
        pc.foregroundFOV = Revolver_pistol_FOV
    elif (repeater_pistol > -1):
        pc.foregroundFOV = Repeater_pistol_FOV
    elif (machine_pistol > -1):
        pc.foregroundFOV = Machine_pistol_FOV
    elif (assault_shotgun > -1):
        pc.foregroundFOV = Assault_shotgun_FOV
    elif (combat_shotgun > -1):
        pc.foregroundFOV = Combat_shotgun_FOV
    elif (combat_rifle > -1):
        pc.foregroundFOV = Combat_rifle_FOV
    elif (grenade_launcher > -1):
        pc.foregroundFOV = Grenade_launcher_FOV
    elif (rocket_launcher > -1):
        pc.foregroundFOV = Rocket_launcher_FOV
    elif (sniper_rifle > -1):
        pc.foregroundFOV = Sniper_rifle_FOV
    elif (sniper_rifle_semiauto > -1):
        pc.foregroundFOV = Sniper_rifle_semiauto_FOV
    elif (support_machinegun > -1):
        pc.foregroundFOV = Support_machinegun_FOV
    elif (patrol_smg > -1):
        pc.foregroundFOV = Patrol_smg_FOV
    else:
        pc.foregroundFOV = Alien_FOV


  #  print("Exiting car Worked.")

@hook(
    hook_func="WillowGame.WillowVehicle:DriverEnter",
    hook_type=Type.POST,
)
def on_player_enter_car(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    pc = get_pc()
    pc.CharacterClass.FOV = FOV

    Vehicle = (str(pc.pawn.objectarchetype).find("Vehicle"))

    if Vehicle > -1:
        Cheetah_Paw = (str(pc.pawn.objectarchetype).find("DLC3_Cheetah_Paw"))

        if Cheetah_Paw > -1:
            pc.Pawn.AfterburnerMaxFOV = (FOV + 10)
        else:
            pc.Pawn.AfterburnerMaxFOV = (FOV + 20)

@hook(
    hook_func="WillowGame.WillowPawn:WeaponChanged",
    hook_type=Type.POST,
)
def on_player_weapon_action(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    if obj == get_pc().pawn:
        pc = get_pc()
        weapon = str(pc.pawn.weapon.definitiondata)

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
            pc.foregroundFOV = Revolver_pistol_FOV
        elif (repeater_pistol > -1):
            pc.foregroundFOV = Repeater_pistol_FOV
        elif (machine_pistol > -1):
            pc.foregroundFOV = Machine_pistol_FOV
        elif (assault_shotgun > -1):
            pc.foregroundFOV = Assault_shotgun_FOV
        elif (combat_shotgun > -1):
            pc.foregroundFOV = Combat_shotgun_FOV
        elif (combat_rifle > -1):
            pc.foregroundFOV = Combat_rifle_FOV
        elif (grenade_launcher > -1):
            pc.foregroundFOV = Grenade_launcher_FOV
        elif (rocket_launcher > -1):
            pc.foregroundFOV = Rocket_launcher_FOV
        elif (sniper_rifle > -1):
            pc.foregroundFOV = Sniper_rifle_FOV
        elif (sniper_rifle_semiauto > -1):
            pc.foregroundFOV = Sniper_rifle_semiauto_FOV
        elif (support_machinegun > -1):
            pc.foregroundFOV = Support_machinegun_FOV
        elif (patrol_smg > -1):
            pc.foregroundFOV = Patrol_smg_FOV
        else:
            pc.foregroundFOV = Alien_FOV