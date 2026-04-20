import unrealsdk
from pathlib import Path
from mods_base import SETTINGS_DIR, build_mod, EInputEvent, keybind, hook, get_pc, ENGINE
from unrealsdk import logging
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from unrealsdk.hooks import Type, Block
from mods_base.options import BaseOption, SliderOption, NestedOption, BoolOption

from.world_fov import on_startgame, BeginSprint, EndSprint, Landed, DoJump, Falling, BerserkEnter, BerserkExit, ToggleBerserk, Falling, ClientStartZoom, WorldFOV, SprintFOVModifier, EyeHeight, PainFOV, bKeepFOVInAir, bScaleADSFov
from .weapon_fov import on_startgame_weapon, RevolverFOV, RepeaterFOV, MachinePistolFOV, AssaultShotgunFOV, CombatShotgunFOV, CombatRifleFOV, GrenadeLauncherFOV, RocketLauncherFOV, SniperRifleFOV, SniperRifleSemiAutoFOV, SupportMachinegunFOV, PatrolSMGFOV, AlienFOV
from .input import bReloadFix

World_fov_options = NestedOption("World FOV Options", [SprintFOVModifier, EyeHeight, PainFOV, bScaleADSFov, bKeepFOVInAir])
weapon_fovs = NestedOption("Weapon FOV Options", [RevolverFOV, RepeaterFOV, MachinePistolFOV, AssaultShotgunFOV, CombatShotgunFOV, CombatRifleFOV, GrenadeLauncherFOV, RocketLauncherFOV, SniperRifleFOV, SniperRifleSemiAutoFOV, SupportMachinegunFOV, PatrolSMGFOV, AlienFOV])

bPatched = False
AccelerationDotProduct = 0



def obj (definition:str, object:str):
    object_class = unrealsdk.find_class(definition)
    current_obj = ENGINE.DynamicLoadObject(object, object_class, False)
    current_obj.ObjectFlags |= 0x4000
    return current_obj



def _on_enable():
    global bPatched
    global AccelerationDotProduct
    if bPatched is False:
        bPatched = True

        GlobalsDef = obj("GlobalsDefinition","gd_globals.General.Globals")


        DoubleTimeSkill = obj("SkillDefinition","gd_skills_common.Basic.DoubleTime")
        DoubleTimeSkill.SkillEffectDefinitions.pop(5)
        DoubleTimeSkill.SkillActivationActions.pop(2)
        DoubleTimeSkill.SkillDeactivationActions.pop(0)
        DoubleTimeConstraint = unrealsdk.make_struct("SkillConstraintData")
        DoubleTimeConstraint.bApplyConstraintOnActivatation = True
        DoubleTimeConstraint.bApplyConstraintWhileActive = True
        DoubleTimeConstraint.bApplyConstraintWhilePaused = True
        DoubleTimeConstraint.bEvaluateExpression = False
        DoubleTimeConstraint.Evaluator = unrealsdk.construct_object("SkillExpressionEvaluator", DoubleTimeSkill)
        DoubleTimeConstraint.Evaluator.Skill = obj("SkillDefinition","gd_FOV.Basic.DoubleTime_Master")
        DoubleTimeConstraint.Evaluator.SkillState = 0
        DoubleTimeSkill.SkillConstraints.append(DoubleTimeConstraint)
        
        DoubleTimeSkillDeactivationActions = unrealsdk.make_struct("SkillActionData")
        DoubleTimeSkillDeactivationActions.bSkillOnRecipient = True
        DoubleTimeSkillDeactivationActions.SkillToActivate = obj("SkillDefinition","gd_FOV.Basic.DoubleTime_Dummy")
        DoubleTimeEventResponses = unrealsdk.make_struct("SkillEventResponseData")
        DoubleTimeEventResponses.EventType = 1
        DoubleTimeEventResponses.Action = DoubleTimeSkillDeactivationActions
        DoubleTimeSkill.EventResponses.append(DoubleTimeEventResponses)



        obj("InterpTrackFloatProp", "weap_camera_animations.Melee.melee_mordacai:InterpGroup_2.InterpTrackFloatProp_0").PropertyName = ""
        obj("InterpTrackFloatProp", "weap_camera_animations.Melee.melee_lilith:InterpGroup_3.InterpTrackFloatProp_0").PropertyName = ""
        obj("BerserkDefinition","gd_Brick.Berserk.BerserkDef").FOVIncrease = 0

        obj("AttributeExpressionEvaluator","gd_FOV.Basic.DoubleTime_Master:ExpressionTree_4.AttributeExpressionEvaluator_25").Expression.ComparisonOperator = 4
        obj("AttributeExpressionEvaluator","gd_FOV.Basic.DoubleTime_Master:ExpressionTree_4.AttributeExpressionEvaluator_25").Expression.ConstantOperand2 = AccelerationDotProduct
        obj("AttributeExpressionEvaluator","gd_FOV.Basic.DoubleTime_Master:ExpressionTree_2.AttributeExpressionEvaluator_20").Expression.ComparisonOperator = 4
        obj("AttributeExpressionEvaluator","gd_FOV.Basic.DoubleTime_Master:ExpressionTree_2.AttributeExpressionEvaluator_20").Expression.ConstantOperand2 = AccelerationDotProduct
        obj("AttributeExpressionEvaluator","gd_FOV.Basic.DoubleTime_Master:ExpressionTree_0.AttributeExpressionEvaluator_21").Expression.ComparisonOperator = 4
        obj("AttributeExpressionEvaluator","gd_FOV.Basic.DoubleTime_Master:ExpressionTree_0.AttributeExpressionEvaluator_21").Expression.ConstantOperand2 = AccelerationDotProduct


        obj("AttributeExpressionEvaluator","gd_skills_common.Basic.DoubleTime:ExpressionTree_4.AttributeExpressionEvaluator_25").Expression.ComparisonOperator = 4
        obj("AttributeExpressionEvaluator","gd_skills_common.Basic.DoubleTime:ExpressionTree_4.AttributeExpressionEvaluator_25").Expression.ConstantOperand2 = AccelerationDotProduct
        obj("AttributeExpressionEvaluator","gd_skills_common.Basic.DoubleTime:ExpressionTree_2.AttributeExpressionEvaluator_20").Expression.ComparisonOperator = 4
        obj("AttributeExpressionEvaluator","gd_skills_common.Basic.DoubleTime:ExpressionTree_2.AttributeExpressionEvaluator_20").Expression.ConstantOperand2 = AccelerationDotProduct
        obj("AttributeExpressionEvaluator","gd_skills_common.Basic.DoubleTime:ExpressionTree_0.AttributeExpressionEvaluator_21").Expression.ComparisonOperator = 4
        obj("AttributeExpressionEvaluator","gd_skills_common.Basic.DoubleTime:ExpressionTree_0.AttributeExpressionEvaluator_21").Expression.ConstantOperand2 = AccelerationDotProduct

        DoubleTimeMaster = obj("SkillDefinition","gd_FOV.Basic.DoubleTime_Master")
        DoubleTimeMaster.SkillEffectDefinitions.append(DoubleTimeSkill.SkillEffectDefinitions[0])
        DoubleTimeMaster.SkillEffectDefinitions.append(DoubleTimeSkill.SkillEffectDefinitions[1])
        DoubleTimeMaster.SkillEffectDefinitions.append(DoubleTimeSkill.SkillEffectDefinitions[2])
        DoubleTimeMaster.SkillEffectDefinitions.append(DoubleTimeSkill.SkillEffectDefinitions[3])
        DoubleTimeSkill.SkillEffectDefinitions.pop(3)
        DoubleTimeSkill.SkillEffectDefinitions.pop(2)
        DoubleTimeSkill.SkillEffectDefinitions.pop(1)
        DoubleTimeSkill.SkillEffectDefinitions.pop(0)

        obj("SkillDefinition","gd_skills_common.Basic.DoDuck").EventResponses[1].action.SkillToDeactivate = DoubleTimeMaster

        GlobalsDef.BasicSkills[16] = DoubleTimeMaster
        GlobalsDef.BasicSkills.append(DoubleTimeSkill)
        GlobalsDef.BasicSkills.append(obj("SkillDefinition","gd_FOV.Basic.DoubleTime_Dummy"))













# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]


build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[WorldFOV, World_fov_options, weapon_fovs, bReloadFix],
    keybinds=[],
    hooks=[on_startgame, BeginSprint, EndSprint, Landed, DoJump, Falling, BerserkEnter, BerserkExit, ToggleBerserk, ClientStartZoom, on_startgame_weapon],
    commands=[],
    on_enable=_on_enable,
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/FOV.json"),
)

logging.info(f"FOV and sprint rotation fix Loaded: {__version__}, {__version_info__}")
