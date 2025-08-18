import unrealsdk
from pathlib import Path
from mods_base import SETTINGS_DIR, build_mod, EInputEvent, keybind, hook, get_pc, ENGINE
from unrealsdk import logging
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from unrealsdk.hooks import Type, Block
from mods_base.options import BaseOption, SliderOption, NestedOption

from .world_fov import on_startgame, WorldFOV
from .weapon_fov import on_startgame_weapon, RevolverFOV, RepeaterFOV, MachinePistolFOV, AssaultShotgunFOV, CombatShotgunFOV, CombatRifleFOV, GrenadeLauncherFOV, RocketLauncherFOV, SniperRifleFOV, SniperRifleSemiAutoFOV, SupportMachinegunFOV, PatrolSMGFOV, AlienFOV
from .input import bReloadFix

weapon_fovs = NestedOption("Weapon FOV", [RevolverFOV, RepeaterFOV, MachinePistolFOV, AssaultShotgunFOV, CombatShotgunFOV, CombatRifleFOV, GrenadeLauncherFOV, RocketLauncherFOV, SniperRifleFOV, SniperRifleSemiAutoFOV, SupportMachinegunFOV, PatrolSMGFOV, AlienFOV])

bPatched = False


def obj (definition:str, object:str):
    object_class = unrealsdk.find_class(definition)
    current_obj = ENGINE.DynamicLoadObject(object, object_class, False)
    current_obj.ObjectFlags |= 0x4000
    return current_obj



def _on_enable():
    global bPatched
    if bPatched is False:
        bPatched = True
        GlobalsDef = obj("GlobalsDefinition","gd_globals.General.Globals")
        DuckSkill = obj("SkillDefinition","gd_skills_common.Basic.DoDuck")
        DoubleTimeSkill = obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime")
        DoubleTimeAnimationSkill = obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime_Animation")

        FireSkill = obj("SkillDefinition","gd_skills_common.Basic.Fire")
        MeleeSkill = obj("SkillDefinition","gd_skills_common.Basic.Melee")
        GrenadeSkill = obj("SkillDefinition","gd_skills_common.Basic.Grenade")
        ZoomSkill = obj("SkillDefinition","gd_skills_common.Basic.ZoomWeapon")

        DuckSkill.EventResponses.append(DuckSkill.EventResponses[1])
        DuckSkill.EventResponses[1].Action.SkillToDeactivate = DoubleTimeSkill
        DuckSkill.EventResponses[len(DuckSkill.EventResponses) - 1].Action.SkillToDeactivate = DoubleTimeAnimationSkill

        DoubleTimeSkill.EventResponses[0].Action.SkillToDeactivate = DuckSkill
        DoubleTimeAnimationSkill.EventResponses[0].Action.SkillToDeactivate = DuckSkill
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime:ExpressionTree_4.SkillExpressionEvaluator_0").Skill = FireSkill
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime:ExpressionTree_4.SkillExpressionEvaluator_1").Skill = MeleeSkill
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime:ExpressionTree_4.SkillExpressionEvaluator_2").Skill = GrenadeSkill
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime:ExpressionTree_4.SkillExpressionEvaluator_3").Skill = ZoomSkill

        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime_Animation:ExpressionTree_14.SkillExpressionEvaluator_0").Skill = FireSkill
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime_Animation:ExpressionTree_14.SkillExpressionEvaluator_1").Skill = MeleeSkill
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime_Animation:ExpressionTree_14.SkillExpressionEvaluator_2").Skill = GrenadeSkill
        obj("SkillExpressionEvaluator","gd_skills_common_FOV.Basic.DoubleTime_Animation:ExpressionTree_14.SkillExpressionEvaluator_3").Skill = ZoomSkill


        DoubleTimeSkill.SkillEffectDefinitions[4].BaseModifierValue.BaseValueConstant = 15
        DoubleTimeAnimationSkill.SkillEffectDefinitions[2].BaseModifierValue.BaseValueConstant = 0
        MeleeSkill.InitialDuration = 0.6


        GlobalsDef.BasicSkills[16] = DoubleTimeSkill
        GlobalsDef.BasicSkills.append(DoubleTimeAnimationSkill)
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
    options=[WorldFOV, weapon_fovs, bReloadFix],
    keybinds=[],
    hooks=[on_startgame, on_startgame_weapon],
    commands=[],
    on_enable=_on_enable,
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/FOV.json"),
)

logging.info(f"FOV and sprint rotation fix Loaded: {__version__}, {__version_info__}")
