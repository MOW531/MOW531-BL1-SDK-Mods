import unrealsdk #type: ignore
import re
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

pickup_Weapon = None
pickup_Item = None

bDisplayFullName = BoolOption("Display full name:", False)


#Guns


def GenWeaponName(DefData, bIncludeManufacturer, bIncludeModelName, bIncludePrefixTitle, Rarity):

    if bDisplayFullName.value is True:
        bIncludeManufacturer = True
        bIncludeModelName = True
        bIncludePrefixTitle = True

    X = 0
    Success = False
    FinalPrefix = ""
    FinalTitle = ""

    if ((DefData.WeaponTypeDefinition.bTypeNameIsFullName is False and DefData.GripPartDefinition != None) and DefData.BodyPartDefinition != None):

        # End:0xB6
        if ((DefData.ManufacturerDefinition != None) and DefData.ManufacturerGradeIndex != -1):

            ManufacturerName = DefData.ManufacturerDefinition.GetManufacturerGradeDisplayName(DefData.ManufacturerGradeIndex)

        else:

            ManufacturerName = DefData.WeaponTypeDefinition.NoManufacturerName

        Core = DefData.BodyPartDefinition.PartName

        # End:0x152
        if(DefData.WeaponTypeDefinition != unrealsdk.find_object("WeaponTypeDefinition", "gd_weap_grenade_launcher.A_Weapon.WeaponType_grenade_launcher")):

            if(DefData.StockPartDefinition != None):
        
                X += DefData.StockPartDefinition.PartNumberAddend
                Rarity = DefData.StockPartDefinition.GetRarityLevel() > 0
        
        # End:0x1B9
        if(DefData.MagazinePartDefinition != None):
        
            X += DefData.MagazinePartDefinition.PartNumberAddend
            Rarity = Rarity and DefData.MagazinePartDefinition.GetRarityLevel() > 0

        if(DefData.WeaponTypeDefinition == unrealsdk.find_object("WeaponTypeDefinition", "gd_weap_grenade_launcher.A_Weapon.WeaponType_grenade_launcher")):

            if(DefData.BarrelPartDefinition != None):
        
                X += DefData.BarrelPartDefinition.PartNumberAddend
                Rarity = DefData.BarrelPartDefinition.GetRarityLevel() > 0
        
        # End:0x1CD
        if(Rarity is True):
        
            X *= int(10)
        
        # End:0x253
        if(((DefData.PrefixPartDefinition != None) and DefData.PrefixPartDefinition.bNameIsUnique is True) or ((DefData.TitlePartDefinition != None) and DefData.TitlePartDefinition.bNameIsUnique is True)):
        
            bIncludeManufacturer = False
            bIncludeModelName = False
            bIncludePrefixTitle = True
        
        # End:0x26A
        if(bIncludeManufacturer is True):
        
            WeaponName = ManufacturerName
        
        else:
        
            WeaponName = ""
        
        # End:0x2A4
        if(bIncludeModelName is True):
        
            # End:0x299
            if(bIncludeManufacturer is True):
            
                WeaponName = "{} {}".format(WeaponName, Core)               
            
            else:
            
                WeaponName = Core
            
        
        # End:0x2D9
        if((X > 0) and bIncludeModelName is True):
        
            Number = str(X)
            WeaponName = WeaponName + Number
        
        # End:0x32C
        if((DefData.MaterialPartDefinition != None) and bIncludeModelName is True):
        
            Letter = DefData.MaterialPartDefinition.PartName
            WeaponName = WeaponName + Letter
        
        # End:0x362
        if(DefData.PrefixPartDefinition != None):
        
            FinalPrefix = DefData.PrefixPartDefinition.PartName
        
        # End:0x398
        if(DefData.TitlePartDefinition != None):
        
            FinalTitle = DefData.TitlePartDefinition.PartName
        
        # End:0x3D6
        if((len(FinalPrefix) > 0) and bIncludePrefixTitle is True):
        
            WeaponName = "{} {}".format(WeaponName, FinalPrefix) # ((len(WeaponName) == 0) ? FinalPrefix : WeaponName @ FinalPrefix)
        
        # End:0x414
        if((len(FinalTitle) > 0) and bIncludePrefixTitle is True):
        
            WeaponName = "{} {}".format(WeaponName, FinalTitle) # ((Len(WeaponName) == 0) ? FinalTitle : WeaponName @ FinalTitle)
        
        Success = True
    
    # End:0x447
    if Success is not True:
    
        WeaponName = DefData.WeaponTypeDefinition.TypeName

    WeaponName = WeaponName.strip()
    WeaponName = re.sub(' {2,}', ' ', WeaponName)
    return WeaponName

@hook(
    hook_func="WillowGame.WillowWeapon:GenerateHumanReadableNameFromDefinitionParts",
    hook_type=Type.PRE,
)
def WeaponCardName(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    WeaponName = GenWeaponName(obj.DefinitionData, __args.bIncludeManufacturer, __args.bIncludeModelName, __args.bIncludePrefixTitle, __args.Rarity)
    return Block, WeaponName


@hook(
    hook_func="WillowGame.WillowWeapon:GenerateHumanReadableNameFromDefinition",
    hook_type=Type.PRE,
)
def WeaponPickupMsgName(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global pickup_Weapon
    if pickup_Weapon is not None:
        return Block, pickup_Weapon
    else:
        return Block

@hook(
    hook_func="WillowGame.ReceivedWeaponMessage:GetWeaponString",
    hook_type=Type.PRE,
)
def WeaponPickupMsg(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global pickup_Weapon
    pickup_Weapon = GenWeaponName(__args.WeaponInfo, True, True, True, False)



#Items

def GenItemName(DefData, bIncludeManufacturer, bIncludeModelName, bIncludePrefixTitle):
    Success = False
    X = 0
    Rarity = False
    GeneratedItemName = ""
    FinalPrefix = ""
    FinalTitle = ""

    if bDisplayFullName.value is True:
        bIncludeManufacturer = True
        bIncludeModelName = True
        bIncludePrefixTitle = True


    # End:0x42F
    if(DefData.ItemDefinition.bItemNameIsFullName is False):
    
        # End:0x86
        if((DefData.ManufacturerDefinition != None) and DefData.ManufacturerGradeIndex != -1):
        
            ManufacturerName = DefData.ManufacturerDefinition.GetManufacturerGradeDisplayName(DefData.ManufacturerGradeIndex)            
        
        else:
        
            ManufacturerName = DefData.ItemDefinition.NoManufacturerName
        
        # End:0x12C
        if(((DefData.PrefixItemNamePartDefinition != None) and DefData.PrefixItemNamePartDefinition.bNameIsUnique is True) or ((DefData.TitleItemNamePartDefinition != None) and DefData.TitleItemNamePartDefinition.bNameIsUnique is True)):
        
            bIncludeManufacturer = False
            bIncludeModelName = False
            bIncludePrefixTitle = True
        
        # End:0x140
        if(bIncludeManufacturer):
        
            GeneratedItemName = ManufacturerName
        
        # End:0x18E
        if((DefData.MaterialItemPartDefinition == None) or (DefData.LeftSideItemPartDefinition == None) and DefData.RightSideItemPartDefinition == None):
        
            bIncludeModelName = False
        
        # End:0x33F
        if(bIncludeModelName):
        
            # End:0x1CD
            if(DefData.MaterialItemPartDefinition != None):
            
                Core = DefData.MaterialItemPartDefinition.PartName
            
            # End:0x229
            if(DefData.LeftSideItemPartDefinition != None):
            
                X += DefData.LeftSideItemPartDefinition.PartNumberAddend
                Rarity = DefData.LeftSideItemPartDefinition.GetRarityLevel() > 0
            
            # End:0x290
            if(DefData.RightSideItemPartDefinition != None):
            
                X += DefData.RightSideItemPartDefinition.PartNumberAddend
                Rarity = Rarity and DefData.RightSideItemPartDefinition.GetRarityLevel() > 0
            
            # End:0x2A4
            if(Rarity):
            
                X *= 10
            
            # End:0x2C2
            if(bIncludeManufacturer):
                            
                GeneratedItemName = "{} {}".format(GeneratedItemName, Core)                
            
            else:
            
                GeneratedItemName = Core
            
            # End:0x2F7
            if(X > 0):
            
                Number = str(X)
                GeneratedItemName = GeneratedItemName + Number
            
            # End:0x33F
            if(DefData.BodyItemPartDefinition != None):
            
                Letter = DefData.BodyItemPartDefinition.PartName
                GeneratedItemName = GeneratedItemName + Letter
            
        
        # End:0x375
        if(DefData.PrefixItemNamePartDefinition != None):
        
            FinalPrefix = DefData.PrefixItemNamePartDefinition.PartName
        
        # End:0x3AB
        if(DefData.TitleItemNamePartDefinition != None):
        
            FinalTitle = DefData.TitleItemNamePartDefinition.PartName
        
        # End:0x3E9
        if((len(FinalPrefix) > 0) and bIncludePrefixTitle is True):
        
            GeneratedItemName = "{} {}".format(GeneratedItemName, FinalPrefix) #((Len(GeneratedItemName) == 0) ? FinalPrefix : GeneratedItemName @ FinalPrefix)
        
        # End:0x427
        if((len(FinalTitle) > 0) and bIncludePrefixTitle is True):
        
            GeneratedItemName = "{} {}".format(GeneratedItemName, FinalTitle) #((Len(GeneratedItemName) == 0) ? FinalTitle : GeneratedItemName @ FinalTitle)
        
        Success = True
    
    # End:0x45A
    if(Success is False):
    
        GeneratedItemName = DefData.ItemDefinition.ItemName

    GeneratedItemName = GeneratedItemName.strip()
    GeneratedItemName = re.sub(' {2,}', ' ', GeneratedItemName)
    return GeneratedItemName
    #return ReturnValue    






@hook(
    hook_func="WillowGame.WillowItem:GenerateHumanReadableNameFromDefinitionParts",
    hook_type=Type.PRE,
)
def ItemCardName(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    ItemName = GenItemName(obj.DefinitionData, __args.bIncludeManufacturer, __args.bIncludeModelName, __args.bIncludePrefixTitle)
    return Block, ItemName


@hook(
    hook_func="WillowGame.WillowItem:GenerateHumanReadableNameFromDefinition",
    hook_type=Type.PRE,
)
def ItemPickupMsgName(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global pickup_Item
    if pickup_Item is not None:
        return Block, pickup_Item
    else:
        return Block

@hook(
    hook_func="WillowGame.ReceivedItemMessage:GetItemString",
    hook_type=Type.PRE,
)
def ItemPickupMsg(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global pickup_Item
    pickup_Item = GenItemName(__args.ItemInfo, True, True, True)



# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[bDisplayFullName],
    keybinds=[],
    hooks=[WeaponPickupMsgName, WeaponPickupMsg, WeaponCardName, ItemPickupMsgName, ItemPickupMsg, ItemCardName],
    commands=[],
    # Defaults to f"SETTINGS_DIR/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"SETTINGS_DIR/SmallNameGenerationFix.json"),
)

logging.info(f"Small Name Generation Fix Loaded: {__version__}, {__version_info__}")