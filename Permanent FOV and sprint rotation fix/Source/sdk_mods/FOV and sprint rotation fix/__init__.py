import unrealsdk
from pathlib import Path
from mods_base import SETTINGS_DIR, build_mod, EInputEvent, keybind, hook
from unrealsdk import logging
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from unrealsdk.hooks import Type, Block
from mods_base.options import BaseOption, SliderOption

from .world_fov import on_startgame, WorldFOV
from .weapon_fov import on_startgame_weapon, RevolverFOV, RepeaterFOV, MachinePistolFOV, AssaultShotgunFOV, CombatShotgunFOV, CombatRifleFOV, GrenadeLauncherFOV, RocketLauncherFOV, SniperRifleFOV, SniperRifleSemiAutoFOV, SupportMachinegunFOV, PatrolSMGFOV, AlienFOV
from .input import bReloadFix

current_obj = None
bPatched = False

def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)



def _on_enable():
    global bPatched
    if bPatched is False:
        bPatched = True
        GlobalsDef = obj("GlobalsDefinition","gd_globals.General.Globals")

        obj("SkillDefinition","gd_skills_common.Basic.DoDuck").EventResponses.append(current_obj.EventResponses[1])
        obj("SkillDefinition","gd_skills_common.Basic.DoDuck").EventResponses[1].Action.SkillToDeactivate = obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime")
        obj("SkillDefinition","gd_skills_common.Basic.DoDuck").EventResponses[len(current_obj.EventResponses) - 1].Action.SkillToDeactivate = obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime_Animation")

        obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime").EventResponses[0].Action.SkillToDeactivate = obj("SkillDefinition","gd_skills_common.Basic.DoDuck")
        obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime_Animation").EventResponses[0].Action.SkillToDeactivate = obj("SkillDefinition","gd_skills_common.Basic.DoDuck")
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime:ExpressionTree_4.SkillExpressionEvaluator_0").Skill = obj("SkillDefinition","gd_skills_common.Basic.Fire")
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime:ExpressionTree_4.SkillExpressionEvaluator_1").Skill = obj("SkillDefinition","gd_skills_common.Basic.Melee")
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime:ExpressionTree_4.SkillExpressionEvaluator_2").Skill = obj("SkillDefinition","gd_skills_common.Basic.Grenade")
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime:ExpressionTree_4.SkillExpressionEvaluator_3").Skill = obj("SkillDefinition","gd_skills_common.Basic.ZoomWeapon")

        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime_Animation:ExpressionTree_14.SkillExpressionEvaluator_0").Skill = obj("SkillDefinition","gd_skills_common.Basic.Fire")
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime_Animation:ExpressionTree_14.SkillExpressionEvaluator_1").Skill = obj("SkillDefinition","gd_skills_common.Basic.Melee")
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime_Animation:ExpressionTree_14.SkillExpressionEvaluator_2").Skill = obj("SkillDefinition","gd_skills_common.Basic.Grenade")
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime_Animation:ExpressionTree_14.SkillExpressionEvaluator_3").Skill = obj("SkillDefinition","gd_skills_common.Basic.ZoomWeapon")


        obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime").SkillEffectDefinitions[4].BaseModifierValue.BaseValueConstant = 15

        obj("SkillDefinition","gd_skills_common.Basic.Melee").InitialDuration = 0.6


        GlobalsDef.BasicSkills[16] = obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime")
        GlobalsDef.BasicSkills.append(obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime_Animation"))
        GlobalsDef.BasicSkills.append(obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime_Dummy"))

        obj("InterpTrackFloatProp", "weap_camera_animations.Melee.melee_mordacai:InterpGroup_2.InterpTrackFloatProp_0").PropertyName = ""
        obj("InterpTrackFloatProp", "weap_camera_animations.Melee.melee_lilith:InterpGroup_3.InterpTrackFloatProp_0").PropertyName = ""


# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]


build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[WorldFOV, RevolverFOV, RepeaterFOV, MachinePistolFOV, AssaultShotgunFOV, CombatShotgunFOV, CombatRifleFOV, GrenadeLauncherFOV, RocketLauncherFOV, SniperRifleFOV, SniperRifleSemiAutoFOV, SupportMachinegunFOV, PatrolSMGFOV, AlienFOV, bReloadFix],
    keybinds=[],
    hooks=[on_startgame, on_startgame_weapon],
    commands=[],
    on_enable=_on_enable,
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/FOV.json"),
)

logging.info(f"FOV and sprint rotation fix Loaded: {__version__}, {__version_info__}")
