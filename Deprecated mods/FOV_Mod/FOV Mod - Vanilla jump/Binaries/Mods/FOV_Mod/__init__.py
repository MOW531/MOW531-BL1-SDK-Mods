import unrealsdk
from pathlib import Path
from mods_base import SETTINGS_DIR, build_mod, EInputEvent, keybind
from unrealsdk import logging
from mods_base.options import BaseOption, SliderOption

from .world_fov import SpawningProcessComplete, DriverEnter, DriverLeave, WorldFOV
from .weapon_fov import WeaponActionComplete, RevolverFOV, RepeaterFOV, MachinePistolFOV, assaultshotgunFOV, combatshotgunFOV, combatrifleFOV, grenadelauncherFOV, rocketlauncherFOV, sniperrifleFOV, sniperriflesemiautoFOV, supportmachinegunFOV, patrolsmgFOV, alienFOV

current_obj = None

def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)

GlobalsDef = obj("GlobalsDefinition","gd_globals.General.Globals")


obj("AttributeExpressionEvaluator","gd_skills_common.Basic.DoubleTime:ExpressionTree_4.AttributeExpressionEvaluator_25").Expression.ConstantOperand2 = 0
obj("AttributeExpressionEvaluator","gd_skills_common.Basic.DoubleTime:ExpressionTree_4.AttributeExpressionEvaluator_25").Expression.ComparisonOperator = 4


obj("SkillDefinition","gd_skills_common.Basic.DoubleTime").SkillEffectDefinitions[5].ModifierType = 2
obj("SkillDefinition","gd_skills_common.Basic.DoubleTime").SkillEffectDefinitions[5].BaseModifierValue.BaseValueConstant = 15
obj("SkillDefinition","gd_skills_common.Basic.DoubleTime").SkillConstraints.append(obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime_Dummy").SkillConstraints[2])
obj("SkillDefinition","gd_skills_common.Basic.DoubleTime").EventResponses.append(obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime_Animation").EventResponses[1])


obj("SkillDefinition","gd_skills_common.Basic.Melee").InitialDuration = 0.6

GlobalsDef.BasicSkills[16] = obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime")
GlobalsDef.BasicSkills.append(obj("SkillDefinition","gd_skills_common_FOV.Basic.DoubleTime_Dummy"))
GlobalsDef.BasicSkills.append(obj("SkillDefinition","gd_skills_common.Basic.DoubleTime"))


MordacaiMelee = obj("InterpTrackFloatProp", "weap_camera_animations.Melee.melee_mordacai:InterpGroup_2.InterpTrackFloatProp_0")
MordacaiMelee.PropertyName = ""
LilithMelee = obj("InterpTrackFloatProp", "weap_camera_animations.Melee.melee_lilith:InterpGroup_3.InterpTrackFloatProp_0")
LilithMelee.PropertyName = ""

# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]


build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[WorldFOV, RevolverFOV, RepeaterFOV, MachinePistolFOV, assaultshotgunFOV, combatshotgunFOV, combatrifleFOV, grenadelauncherFOV, rocketlauncherFOV, sniperrifleFOV, sniperriflesemiautoFOV, supportmachinegunFOV, patrolsmgFOV, alienFOV],
    keybinds=[],
    hooks=[SpawningProcessComplete, DriverEnter, DriverLeave, WeaponActionComplete],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/FOV.json"),
)

logging.info(f"FOV Mod Loaded: {__version__}, {__version_info__}")
