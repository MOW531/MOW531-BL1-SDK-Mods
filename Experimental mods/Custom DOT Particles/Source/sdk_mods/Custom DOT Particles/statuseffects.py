import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption







bIgnite = False
bDecay = False
bShock = False
bCurse = False
bAmplifyEffects = False
bSlow = False

bSlag = False
bCryo = False
bRadiation = False
bDarkMagic = False


def GetEffectCount(emitter):
    global bIgnite
    global bDecay
    global bShock
    global bCurse
    global bAmplifyEffects
    global bSlow
    global bSlag
    global bCryo
    global bRadiation
    global bDarkMagic


    num = 0
    ActiveStatusEffects = None

    
    if emitter.owner is not None and emitter.owner.GetStatusEffectsComponent() is not None:
        ActiveStatusEffects = str(emitter.owner.GetStatusEffectsComponent().ActiveStatusEffects)
    
    if ActiveStatusEffects is None:
        return num

    if "gd_Incendiary.StatusEffect.Incendiary_Status" in ActiveStatusEffects or "gd_Skills2_Lilith.MiscData.Status_Phoenix" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Caladbolg_Incendiary_Status_Melee" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Illuminator_Incendiary_Status_Melee" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Incendiary_Status_Melee" in ActiveStatusEffects:
        bIgnite = True
        num += 1
    else:
        bIgnite = False

    if "gd_Corrosive.StatusEffect.Corrosive_Status" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Caladbolg_Corrosive_Status_Melee" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Corrosive_Status_Melee" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Corruptor_Corrosive_Status_Melee" in ActiveStatusEffects:
        bDecay = True
        num += 1
    else:
        bDecay = False

    if "gd_Shock.StatusEffect.Shock_Status" in ActiveStatusEffects or "gd_Skills2_Lilith.MiscData.Status_Radiance" in ActiveStatusEffects or "gd_Skills_Lilith.MiscData.Status_Radiance" in ActiveStatusEffects or "gd_Skills_Lilith.MiscData.Status_EtherealLightning" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Caladbolg_Shock_Status_Melee" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Shock_Status" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Shock_Status_Melee" in ActiveStatusEffects:
        bShock = True
        num += 1
    else:
        bShock = False

    if "gd_Dark.DamageType.Dark_Status" in ActiveStatusEffects:
        bCurse = True
        num += 1
    else:
        bCurse = False

    if "gd_Light.StatusEffect.Light_Status" in ActiveStatusEffects:
        bAmplifyEffects = True
        num += 1
    else:
        bAmplifyEffects = False

    if "gd_Slow.StatusEffect.Slow_Status" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Caladbolg_Slow_Status_Melee" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Delirium_Slow_Status_Melee" in ActiveStatusEffects or "Eridian_Weapons_Overhaul.Shared.DamageType.StatusEffect.Slow_Status_Melee" in ActiveStatusEffects:
        bSlow = True
        num += 1
    else:
        bSlow = False

    if "gd_Slag.StatusEffect.Slag_Status" in ActiveStatusEffects:
        bSlag = True
        num += 1
    else:
        bSlag = False

    if "gd_Cryo.StatusEffect.Cryo_Status" in ActiveStatusEffects:
        bCryo = True
        num += 1
    else:
        bCryo = False

    if "gd_Radiation.StatusEffect.Radiation_Status" in ActiveStatusEffects:
        bRadiation = True
        num += 1
    else:
        bRadiation = False

    if "gd_DarkMagic.StatusEffect.DarkMagic_Status" in ActiveStatusEffects:
        bDarkMagic = True
        num += 1
    else:
        bDarkMagic = False

    return num


def GetParameterName(Type):
    if Type == 1:
        return 'On_Incendiary_Character'
    elif Type == 2:
        return 'On_Corrosive_Character'
    elif Type == 3:
        return 'On_EMPShock_Character'
    elif Type == 5:
        return 'On_AlienPositive'
    elif Type == 4:
        return 'On_AlienNegative'
    elif Type == 6:
        return 'On_Slow_Character'
    elif Type == 7:
        return 'On_Slag_Character'
    elif Type == 8:
        return 'On_Cryo_Character'
    elif Type == 9:
        return 'On_Radiation_Character'
    elif Type == 10:
        return 'On_DarkMagic_Character'
    else:
        return 'None'


def ResetDistributionForEffect(Emitter, Type, Distribution):
    Emitter.SetFloatParameter(Type, Distribution)


@hook(
    hook_func="WillowGame.StatusEffectReplicatedEmitter:UpdateDistributions",
    hook_type=Type.PRE,
)
def UpdateDistributions(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bIgnite
    global bDecay
    global bShock
    global bCurse
    global bAmplifyEffects
    global bSlow
    global bSlag
    global bCryo
    global bRadiation
    global bDarkMagic

    TotalDistribution = 0
    TotalEffectCount = GetEffectCount(obj)
    if(TotalEffectCount > 0):
    
        TotalDistribution = 100.0000000 / TotalEffectCount

    if bIgnite is True:
        ResetDistributionForEffect(obj, "On_Incendiary_Character", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_Incendiary_Character", 0)

    if bDecay is True:
        ResetDistributionForEffect(obj, "On_Corrosive_Character", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_Corrosive_Character", 0)

    if bShock is True:
        ResetDistributionForEffect(obj, "On_EMPShock_Character", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_EMPShock_Character", 0)

    if bCurse is True:
        ResetDistributionForEffect(obj, "On_AlienNegative", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_AlienNegative", 0)

    if bAmplifyEffects is True:
        ResetDistributionForEffect(obj, "On_AlienPositive", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_AlienPositive", 0)

    if bSlow is True:
        ResetDistributionForEffect(obj, "On_Slow_Character", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_Slow_Character", 0)
    
    if bSlag is True:
        ResetDistributionForEffect(obj, "On_Slag_Character", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_Slag_Character", 0)

    if bCryo is True:
        ResetDistributionForEffect(obj, "On_Cryo_Character", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_Cryo_Character", 0)

    if bRadiation is True:
        ResetDistributionForEffect(obj, "On_Radiation_Character", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_Radiation_Character", 0)

    if bDarkMagic is True:
        ResetDistributionForEffect(obj, "On_DarkMagic_Character", TotalDistribution)
    else:
        ResetDistributionForEffect(obj, "On_DarkMagic_Character", 0)


    if obj.BaseTarget is not None and obj.BaseTarget.GetStatusEffectsComponent() is not None:
        obj.BaseTarget.GetStatusEffectsComponent().EmitterUpdated(obj)

    return Block
