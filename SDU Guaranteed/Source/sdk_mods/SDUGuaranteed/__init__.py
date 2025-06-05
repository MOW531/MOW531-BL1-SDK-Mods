import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, SETTINGS_DIR, build_mod
from unrealsdk import logging

bPatched = False
bPatched_volatile = False
Count = 0
current_obj = None

struct = unrealsdk.make_struct
wclass = unrealsdk.find_class


def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)


def patch_volatile():
    # Base Game
    obj("InventoryBalanceDefinition","gd_itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers = [struct("InventoryManufacturerBalanceData", Manufacturer=obj("ManufacturerDefinition","gd_manufacturers.Manufacturers.Dahl"), Grades=[struct("InventoryGameStageGradeWeightData", GradeModifiers=struct("InventoryGradeModifierData", ExpLevel=1, CustomInventoryDefinition=obj("ItemDefinition","gd_StorageDeckUpgrade.INV_InventorySpace.INV_InventorySpace")))])]
    obj("InventoryBalanceDefinition","gd_itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage = 1
    obj("InventoryBalanceDefinition","gd_itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers[0].Grades[0].GameStageRequirement.MaxGameStage = 100
    obj("InventoryBalanceDefinition","gd_itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers[0].Grades[0].MinSpawnProbabilityModifier.BaseValueConstant = 1
    obj("InventoryBalanceDefinition","gd_itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers[0].Grades[0].MinSpawnProbabilityModifier.BaseValueScaleConstant = 1
    obj("InventoryBalanceDefinition","gd_itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers[0].Grades[0].MaxSpawnProbabilityModifier.BaseValueConstant = 1
    obj("InventoryBalanceDefinition","gd_itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers[0].Grades[0].MaxSpawnProbabilityModifier.BaseValueScaleConstant = 1

    # DLC
    obj("InventoryBalanceDefinition","dlc1_gd_itemgrades.StorageDeckUpgrades.dlc1_ItemGrade_SDU_InventorySlots").Manufacturers = obj("InventoryBalanceDefinition","gd_itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers
    obj("InventoryBalanceDefinition","DLC4_Itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers = obj("InventoryBalanceDefinition","gd_itemgrades.StorageDeckUpgrades.ItemGrade_SDU_InventorySlots").Manufacturers



@hook(
    hook_func="Engine.WorldInfo:CommitMapChange",
    hook_type=Type.POST,
)
def on_commit_map_change(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched_volatile
    bPatched_volatile = False

@hook(
    hook_func="Engine.WorldInfo:PostBeginPlay",
    hook_type=Type.POST,
)
def on_level_loaded(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched_volatile
    global Count
    if Count >= 2:
        Count = 0
        if bPatched_volatile != True:
            bPatched_volatile = True
            patch_volatile()
    else:
        Count = Count + 1




# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    keybinds=[],
    hooks=[on_level_loaded, on_commit_map_change],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/SDUGuaranteed.json"),
)

logging.info(f"SDU Guaranteed Mod Loaded: {__version__}, {__version_info__}")
