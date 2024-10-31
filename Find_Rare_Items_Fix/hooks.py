import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc


@hook(
    hook_func="WillowGame.WillowInteractiveObject:UsedBy",
    hook_type=Type.PRE,
)
def on_container_open(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    if (str(obj).find("VendingMachine")) == -1:
        pc = get_pc()
        CurrentCom = pc.pawn.InvManager.GetCurrentCommDeck()
        ComName = CurrentCom.ItemName
        if (str(ComName).find("Scavenger")) > -1 or (str(ComName).find("Catalyst")) > -1:
            OldAwesomeLevel = int(obj.GetAwesomeLevel())
            AddAwesomeLevel = int(CurrentCom.ReplicatedAttributeSlotModifierValues[2])
            obj.SetAwesomeLevel(OldAwesomeLevel + AddAwesomeLevel)
            NewAwesomeLevel = int(obj.GetAwesomeLevel())

            print(obj)
            print("Current Chest Awesome Level:", OldAwesomeLevel)
            print("Adding:", AddAwesomeLevel)
            print("New Chest Awesome Level:", NewAwesomeLevel)

@hook(
    hook_func="WillowGame.WillowPawn:PostBeginPlay",
    hook_type=Type.PRE,
)
def on_enemy_spawn(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    if obj.Class.Name != "WillowPlayerPawn":
        pc = get_pc()
        CurrentCom = pc.pawn.InvManager.GetCurrentCommDeck()
        ComName = CurrentCom.ItemName
        if (str(ComName).find("Scavenger")) > -1 or (str(ComName).find("Catalyst")) > -1:
            OldAwesomeLevel = int(obj.GetAwesomeLevel())
            AddAwesomeLevel = int(CurrentCom.ReplicatedAttributeSlotModifierValues[2])
            obj.SetAwesomeLevel(OldAwesomeLevel + AddAwesomeLevel)
            NewAwesomeLevel = int(obj.GetAwesomeLevel())

            print(obj)
            print("Current Enemy Awesome Level:", OldAwesomeLevel)
            print("Adding:", AddAwesomeLevel)
            print("New Enemy Awesome Level:", NewAwesomeLevel)