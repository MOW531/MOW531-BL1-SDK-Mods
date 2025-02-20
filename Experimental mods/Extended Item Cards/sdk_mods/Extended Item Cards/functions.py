import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption


def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    return unrealsdk.find_object(definition, object)

def GetElementIconForItem(Item):

    SlagDef = None
    CryoDef = None
    RadiationDef = None
    DarkMagicDef = None

    DmgTypeIcon = ""
    TechUILevel = ""
    


    if "WillowWeapon" in str(Item.Class.Name):
        TechUILevel = str(Item.StaticCalculateWeaponTechLevelForUI(Item.DefinitionData)[0])
        DmgType = Item.StaticGetWeaponDamageType(Item.definitiondata)[0]

        if DmgType == obj("WillowDamageTypeDefinition","gd_Corrosive.DamageType.DmgType_Corrosive_Impact"):
            DmgTypeIcon = "corr"

        elif DmgType == obj("WillowDamageTypeDefinition","gd_Explosive.DamageType.DmgType_Explosive"):
            DmgTypeIcon = "exp"

        elif DmgType == obj("WillowDamageTypeDefinition","gd_Shock.DamageType.DmgType_Shock_Impact"):
            DmgTypeIcon = "shock"

        elif DmgType == obj("WillowDamageTypeDefinition","gd_Incendiary.DamageType.DmgType_Incendiary_Impact"):
            DmgTypeIcon = "fire"

        elif DmgType == SlagDef:
            DmgTypeIcon = "slag"

        elif DmgType == CryoDef:
            DmgTypeIcon = "cryo"

        elif DmgType == RadiationDef:
            DmgTypeIcon = "rad"

        elif DmgType == DarkMagicDef:
            DmgTypeIcon = "dmag"
        
    
    elif "WillowEquipAbleItem" in str(Item.Class.Name):
        if len(Item.InstanceDataState.Data) > 0:
            if Item.InstanceDataState.Data[0].Name == "FlashTechFrame":
                TechUILevel = "0"

                if Item.InstanceDataState.Data[0].Float == 11: # Incendiary
                    DmgTypeIcon = "fire"

                elif Item.InstanceDataState.Data[0].Float == 16: # Corrosive
                    DmgTypeIcon = "corr"

                elif Item.InstanceDataState.Data[0].Float == 6: # Shock
                    DmgTypeIcon = "shock"

                elif Item.InstanceDataState.Data[0].Float == 1: # Explosive
                    DmgTypeIcon = "exp"

                elif Item.InstanceDataState.Data[0].Float == 41: # Slag
                    DmgTypeIcon = "slag"

                elif Item.InstanceDataState.Data[0].Float == 26: # Cryo
                    DmgTypeIcon = "cryo"

                elif Item.InstanceDataState.Data[0].Float == 46: # Radiation
                    DmgTypeIcon = "rad"

                elif Item.InstanceDataState.Data[0].Float == 51: # Dark Magic
                    DmgTypeIcon = "dmag"

    if DmgTypeIcon == "":
        return "none"
    return DmgTypeIcon + TechUILevel

