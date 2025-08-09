import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc 
from mods_base.options import BaseOption, BoolOption
from mods_base import SETTINGS_DIR
from mods_base import build_mod
from unrealsdk import logging
import os


bAutoLoot = BoolOption("BL3 Auto-Loot", True)

bPatched = False

def obj (definition:str, object:str):
    try:
        current_obj = unrealsdk.find_object(definition, object)
        current_obj.ObjectFlags |= 0x4000
        return current_obj
    except:
        unrealsdk.load_package(object)
        current_obj = unrealsdk.find_object(definition, object)
        current_obj.ObjectFlags |= 0x4000
        return current_obj


def patch():

 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Assault_Rifle_Bullets").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Combat_Shotgun_Shells").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Grenade_Protean").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Patrol_SMG_Clip").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Repeater_Pistol_Clip").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Revolver_Pistol_Rounds").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Rocket_Launcher").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_ammodrops.Pickups.AmmoDrop_Sniper_Rifle_Cartridges").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_currency.A_Item.Bobblehead").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_currency.A_Item.Currency").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_currency.A_Item.Currency_big").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_currency.A_Item.SkagPearl").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_1").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_2").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_3").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_4").bAutomaticallyPickup = True
 obj("ItemDefinition","gd_HealthDrops.A_Item.HealthVial_5").bAutomaticallyPickup = True


@hook(
    hook_func="Engine.WorldInfo:IsMenuLevel",
    hook_type=Type.PRE,
)
def on_startgame(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched
    if bPatched is False:
        bPatched = True
        patch()






# This part was made by RedxYeti
InteractiveObjects = {}


@hook("WillowGame.WillowPickup:SpawnPickupParticles", Type.POST)
def SpawnPickupParticles(obj: UObject,__args: WrappedStruct,__ret: any,__func: BoundFunction,) -> None:
    global bAutoLoot
    if bAutoLoot.value is True:
        global InteractiveObjects
        if obj.Inventory and obj.Inventory.Class.Name == "WillowUsableItem":
            if obj.Base:
                BaseIO = obj.Base
                if BaseIO in InteractiveObjects.keys() and InteractiveObjects[BaseIO] and obj.bPickupable and obj.Inventory.CanBeUsedBy(InteractiveObjects[BaseIO].Pawn):
                    InteractiveObjects[BaseIO].TouchedPickupable(obj)
                    
            else:
                try:
                    obj.Components[1].SetCylinderSize(350, 350)
                except:
                    return
        return

@hook("WillowGame.WillowInteractiveObject:UsedBy", Type.POST)
def UsedBy(obj: UObject,__args: WrappedStruct,__ret: any,__func: BoundFunction,) -> None:
    global bAutoLoot
    if bAutoLoot.value is True:
        global InteractiveObjects
        InteractiveObjects[obj] = __args.User.Controller
        return


@hook("WillowGame.WillowPlayerController:TouchedPickupable", Type.POST)
def TouchedPickupable(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    global bAutoLoot
    if bAutoLoot.value is True:
        CurrentPickupable = obj.GetCurrentPickupable()

        if not CurrentPickupable or not obj.Pawn:
            return
        
        ClassName = CurrentPickupable.Inventory.Class.Name
        if ClassName == "WillowWeapon" or ClassName == "WillowEquipAbleItem" or CurrentPickupable.Inventory.DefinitionData.ItemDefinition.bPlayerUseItemOnPickup is False:
            return
        
        obj.UpdateAmmoCounts(True)
        if not obj.HasRoomInInventoryFor(CurrentPickupable) or not obj.WorldInfo.Game.PickupQuery(obj.Pawn, CurrentPickupable):
            return
        
        if obj.ShouldUseCoopRange(CurrentPickupable):
            obj.CloneAndGiveToCoopPawns(CurrentPickupable, False)

        obj.ClientSpawnPickupableMesh(CurrentPickupable)
        CurrentPickupable.GiveTo(obj.Pawn, False)
        obj.CurrentTouchedPickupable = None
        obj.CurrentSeenPickupable = None
        obj.UpdateAmmoCounts(True)
        return










# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[bAutoLoot],
    keybinds=[],
    hooks=[on_startgame, SpawnPickupParticles, UsedBy, TouchedPickupable],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/AutoPickupSDK.json"),
)

logging.info(f"Auto-Pickup SDK Loaded: {__version__}, {__version_info__}")
