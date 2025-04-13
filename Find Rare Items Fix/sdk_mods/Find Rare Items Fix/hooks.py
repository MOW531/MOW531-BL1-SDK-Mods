import unrealsdk
from unrealsdk import logging
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc

def wobj(definition:str, package:str):
    unrealsdk.load_package(package)
    return unrealsdk.find_object(definition,package)

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
    pc = get_pc()
    if pc.pawn != None:
        CurrentCom = pc.pawn.InvManager.GetCurrentCommDeck()
        if obj.Class.Name == "WillowInteractiveObject" and CurrentCom != None:
            for attribute in CurrentCom.AttributeSlots:
                if attribute.bActivated is True and str(attribute.AttributeToModify) == "AttributeDefinition'd_attributes.Balance.AwesomeLevel'":
                    OldAwesomeLevel = int(obj.GetAwesomeLevel())
                    AddAwesomeLevel = int(attribute.ComputedModifierValue)
                    obj.SetAwesomeLevel(OldAwesomeLevel + AddAwesomeLevel)
                    NewAwesomeLevel = int(obj.GetAwesomeLevel())

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
    pc = get_pc()
    if pc.pawn != None:
        CurrentCom = pc.pawn.InvManager.GetCurrentCommDeck()
        if obj.Class.Name == "WillowAIPawn" and CurrentCom != None:
            for attribute in CurrentCom.AttributeSlots:
                if attribute.bActivated is True and str(attribute.AttributeToModify) == "AttributeDefinition'd_attributes.Balance.AwesomeLevel'":
                    OldAwesomeLevel = int(obj.GetAwesomeLevel())
                    AddAwesomeLevel = int(attribute.ComputedModifierValue)
                    obj.SetAwesomeLevel(OldAwesomeLevel + AddAwesomeLevel)
                    NewAwesomeLevel = int(obj.GetAwesomeLevel())

                    print("Current Enemy Awesome Level:", OldAwesomeLevel)
                    print("Adding:", AddAwesomeLevel)
                    print("New Enemy Awesome Level:", NewAwesomeLevel)