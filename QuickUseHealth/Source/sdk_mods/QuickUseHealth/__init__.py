import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, keybind, EInputEvent
from unrealsdk import logging


healthpacklist = ["ItemDefinition'gd_HealthDrops.A_Item.HealthPack_1'", "ItemDefinition'gd_HealthDrops.A_Item.HealthPack_2'", "ItemDefinition'gd_HealthDrops.A_Item.HealthPack_3'", "ItemDefinition'gd_HealthDrops.A_Item.HealthPack_4'", "ItemDefinition'gd_HealthDrops.A_Item.HealthPack_5'"]


def gethealthregenamount(healthpack):
    for i in healthpack.definitiondata.itemdefinition.behaviors.onused[0].AttributeEffect.skilleffectdefinitions:
        if str(i.AttributeToModify) in "ResourcePoolAttributeDefinition'd_attributes.HealthResourcePool.HealthActiveRegenerationRate'":
            return (i.BaseModifierValue.BaseValueConstant * 10)


@keybind(identifier="Use Medkit", key="T", event_filter=EInputEvent.IE_Pressed)
def usehealthpack():
    if get_pc() is None:
         return
    
    currenthealth = get_pc().Pawn.GetHealth()
    maxhealth = get_pc().Pawn.GetMaxHealth()

    if currenthealth == maxhealth or get_pc().bStatusMenuOpen is True:
         return
    
    healthpacksininventory = []
    
    invmanager = get_pc().GetPawnInventoryManager()
    for items in invmanager.Backpack:
        if str(items.Class) not in "Class'WillowGame.WillowUsableItem'":
            continue
        
        if str(items.definitiondata.itemdefinition) in healthpacklist:
            healthpacksininventory.append([items, gethealthregenamount(items)])

    if healthpacksininventory:
        healthpacksininventory = sorted(healthpacksininventory, key=lambda x: x[1], reverse=True)
        packsininventory = len(healthpacksininventory)
        count = 0

        for packs in healthpacksininventory:
             count = count + 1
             if (currenthealth + packs[1]) > (maxhealth) and packsininventory > count:
                  pass
             
             else:
                print(f"Healing for {packs[1]} points!")
                invmanager.ReadyBackpackInventory(packs[0])
                break
    else:
        print("No healthpacks found!")
             

__version__: str
__version_info__: tuple[int, ...]

build_mod(
    options=[],
    keybinds=[usehealthpack],
    hooks=[],
    commands=[],
    settings_file=Path(f"{SETTINGS_DIR}/QuickUseMedkits.json"),
)

logging.info(f"Quick Use Medkits Loaded: {__version__}, {__version_info__}")
