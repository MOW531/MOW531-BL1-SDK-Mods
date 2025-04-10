import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption, SliderOption
import math

FontSize = SliderOption("Font size", 9, 0, 24, 1, True)

def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    return unrealsdk.find_object(definition, object)


def GetElementIconForItem(Item):
    NormalDef = ["WillowDamageTypeDefinition'gd_Impact.DamageType.DmgType_Normal'"]
    CorrosiveDef = ["WillowDamageTypeDefinition'gd_Corrosive.DamageType.DmgType_Corrosive_Impact'","WillowDamageTypeDefinition'Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Eridian_Corrosive_Impact'","WillowDamageTypeDefinition'Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Corrosive_Slow_Impact'"]
    ExplosiveDef = ["WillowDamageTypeDefinition'gd_Explosive.DamageType.DmgType_Explosive'"]
    ShockDef = ["WillowDamageTypeDefinition'gd_Shock.DamageType.DmgType_Shock_Impact'","WillowDamageTypeDefinition'Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Eridian_Shock_Impact'"]
    IncendiaryDef = ["WillowDamageTypeDefinition'gd_Incendiary.DamageType.DmgType_Incendiary_Impact'","WillowDamageTypeDefinition'Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Eridian_Incendiary_Impact'"]
    SlagDef = []
    CryoDef = []
    RadiationDef = []
    DarkMagicDef = []
    EnergyDef = ["WillowDamageTypeDefinition'Eridian_Weapons_Overhaul.Shared.DamageType.Weapon.DmgType_Eridian_Energy_Impact'"]

    DmgTypeIcon = ""
    TechUILevel = ""
    
    if "WillowWeapon" in str(Item.Class.Name):
        TechUILevel = str(Item.StaticCalculateWeaponTechLevelForUI(Item.DefinitionData)[0])
        DmgType = str(Item.StaticGetWeaponDamageType(Item.definitiondata)[0])

        if DmgType is None:
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




def GetFunStats(Item):
    global FontSize
    list = []

    if "WillowWeapon" in str(Item.Class):
        for presentation in Item.WeaponCardModifierStats:
            PrefixText = str(presentation.AttributePresentation.GetNoConstraintText())
            MainText = str(presentation.AttributePresentation.GetDescription())
            SuffixText = str(presentation.AttributePresentation.GetSuffix())
            Number = presentation.AttributePresentation.ApplyPresentationRulesToValue(presentation.ModifierValue, 1, False)

            Number = presentation.AttributePresentation.RoundValue(Number,presentation.AttributePresentation.GetRoundingMode())

            if presentation.AttributePresentation.GetRoundingMode() == 0 or presentation.AttributePresentation.GetRoundingMode() == 4:
                Number = round(Number,1)

            elif presentation.AttributePresentation.GetRoundingMode() == 1:
                Number = round(Number)

            elif presentation.AttributePresentation.GetRoundingMode() == 2:
                Number = math.floor(Number)

            elif presentation.AttributePresentation.GetRoundingMode() == 3:
                Number = math.ceil(Number)


            NumberString = str(Number)

            if presentation.AttributePresentation.ShouldDisplayAsPercentage() is True:
                NumberString = (str(round(Number)) + "%")
            if Number >= 0 and presentation.AttributePresentation.ShouldDisplayPlusSign() is True:
                NumberString = ("+" + NumberString)


            if PrefixText == "Weapon":
                PrefixText = ""

            temp = PrefixText + MainText + SuffixText

            if presentation.AttributePresentation.ShouldDisplayNumberInTranslation() is True:
                if presentation.AttributePresentation.ShouldUseCustomNumberPlacement() is True:
                    temp = temp.replace("$NUMBER$",NumberString)
                else:    
                    temp = (NumberString + " " + temp)


            TextColor = "#{0:02x}{1:02x}{2:02x}".format(presentation.AttributePresentation.GetTextColor().R,presentation.AttributePresentation.GetTextColor().G,presentation.AttributePresentation.GetTextColor().B)

            if not (Number == 0 and presentation.AttributePresentation.ShouldDisplayNumberInTranslation() is True):
                if presentation.bShouldDisplay is True:
                    list.append(f"<font size=\"{FontSize.value}\" color=\"{TextColor}\">{temp}</font>")


    if "WillowEquipAbleItem" in str(Item.Class) or "WillowUsableItem" in str(Item.Class):
        for presentation in Item.ItemCardModifierStats:
            PrefixText = str(presentation.AttributePresentation.GetNoConstraintText())
            MainText = str(presentation.AttributePresentation.GetDescription())
            SuffixText = str(presentation.AttributePresentation.GetSuffix())
            Number = presentation.AttributePresentation.ApplyPresentationRulesToValue(presentation.ModifierValue, 1, False)

            Number = presentation.AttributePresentation.RoundValue(Number,presentation.AttributePresentation.GetRoundingMode())

            if presentation.AttributePresentation.GetRoundingMode() == 0 or presentation.AttributePresentation.GetRoundingMode() == 4:
                Number = round(Number,1)

            elif presentation.AttributePresentation.GetRoundingMode() == 1:
                Number = round(Number)

            elif presentation.AttributePresentation.GetRoundingMode() == 2:
                Number = math.floor(Number)

            elif presentation.AttributePresentation.GetRoundingMode() == 3:
                Number = math.ceil(Number)


            NumberString = str(Number)

            if presentation.AttributePresentation.ShouldDisplayAsPercentage() is True:
                NumberString = (str(round(Number)) + "%")
            if Number >= 0 and presentation.AttributePresentation.ShouldDisplayPlusSign() is True:
                NumberString = ("+" + NumberString)


            if PrefixText == "Weapon":
                PrefixText = ""

            temp = PrefixText + MainText + SuffixText

            if presentation.AttributePresentation.ShouldDisplayNumberInTranslation() is True:
                if presentation.AttributePresentation.ShouldUseCustomNumberPlacement() is True:
                    temp = temp.replace("$NUMBER$",NumberString)
                else:    
                    temp = (NumberString + " " + temp)


            TextColor = "#{0:02x}{1:02x}{2:02x}".format(presentation.AttributePresentation.GetTextColor().R,presentation.AttributePresentation.GetTextColor().G,presentation.AttributePresentation.GetTextColor().B)
            if not (Number == 0 and presentation.AttributePresentation.ShouldDisplayNumberInTranslation() is True):
                if presentation.bShouldDisplay is True:
                    list.append(f"<font size=\"{FontSize.value}\" color=\"{TextColor}\">{temp}</font>")



    finaltext = "\n".join(list)
    return finaltext
