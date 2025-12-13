import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption, SliderOption, SpinnerOption
import math
import re


NormalDef = ["gd_Impact.DamageType.DmgType_Normal"]
CorrosiveDef = ["gd_Corrosive.DamageType.DmgType_Corrosive_Impact","Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Eridian_Corrosive_Impact","Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Corrosive_Slow_Impact"]
ExplosiveDef = ["gd_Explosive.DamageType.DmgType_Explosive"]
ShockDef = ["gd_Shock.DamageType.DmgType_Shock_Impact","Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Eridian_Shock_Impact"]
IncendiaryDef = ["gd_Incendiary.DamageType.DmgType_Incendiary_Impact","Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Eridian_Incendiary_Impact"]
SlagDef = []
CryoDef = []
RadiationDef = []
DarkMagicDef = []
EnergyDef = ["Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Eridian_Energy_Impact"]

ElementList = NormalDef + CorrosiveDef + ExplosiveDef + ShockDef + IncendiaryDef + SlagDef + CryoDef + RadiationDef+  DarkMagicDef + EnergyDef


def GetElementIconForItem(Item):

    DmgTypeIcon = ""
    TechUILevel = ""
    
    if "WillowWeapon" in str(Item.Class.Name):
        TechUILevel = str(Item.StaticCalculateWeaponTechLevelForUI(Item.DefinitionData)[0])
        DmgType = str(Item.StaticGetWeaponDamageType(Item.definitiondata)[0])
        if Item.StaticGetWeaponDamageType(Item.definitiondata)[0] is not None:
            DmgType = re.findall('(?<=\')(.*?)(?=\')', DmgType)[0]
            DmgType = re.findall('^[^:]*', DmgType)[0]


        if DmgType is None or DmgType == "None":
            return "none"

        elif DmgType in NormalDef:
            return "none"

        elif DmgType in CorrosiveDef:
            DmgTypeIcon = "corr"

        elif DmgType in ExplosiveDef:
            DmgTypeIcon = "exp"

        elif DmgType in ShockDef:
            DmgTypeIcon = "shock"

        elif DmgType in IncendiaryDef:
            DmgTypeIcon = "fire"

        elif DmgType in SlagDef:
            DmgTypeIcon = "slag"

        elif DmgType in CryoDef:
            DmgTypeIcon = "cryo"

        elif DmgType in RadiationDef:
            DmgTypeIcon = "rad"

        elif DmgType in DarkMagicDef:
            DmgTypeIcon = "dmag"
        
        elif DmgType in EnergyDef:
            DmgTypeIcon = "energy"
        
    
    elif "WillowEquipAbleItem" in str(Item.Class.Name):
        tempInstanceData = []
        if Item.GetInstanceData("FlashTechFrame",tempInstanceData)[0] is True:
            TechFrame = Item.GetInstanceData("FlashTechFrame",tempInstanceData)[1][0].Float
            TechUILevel = "0"

            if TechFrame == 11: # Incendiary
                DmgTypeIcon = "fire"

            elif TechFrame == 16: # Corrosive
                DmgTypeIcon = "corr"

            elif TechFrame == 6: # Shock
                DmgTypeIcon = "shock"

            elif TechFrame == 1: # Explosive
                DmgTypeIcon = "exp"

            elif TechFrame == 41: # Slag
                DmgTypeIcon = "slag"

            elif TechFrame == 26: # Cryo
                DmgTypeIcon = "cryo"

            elif TechFrame == 46: # Radiation
                DmgTypeIcon = "rad"

            elif TechFrame == 51: # Dark Magic
                DmgTypeIcon = "dmag"

            elif TechFrame == 21: # Energy
                DmgTypeIcon = "energy"

    if DmgTypeIcon == "":
        return "none"
    return DmgTypeIcon + TechUILevel