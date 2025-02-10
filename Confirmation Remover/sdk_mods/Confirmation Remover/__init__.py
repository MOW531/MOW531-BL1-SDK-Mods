import unrealsdk #type: ignore
from pathlib import Path
from unrealsdk import logging #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct,UArrayProperty #type: ignore
from mods_base import hook,get_pc,ENGINE,build_mod, SETTINGS_DIR #type: ignore

# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

InteractiveObjects = {}

@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:extAttemptShopOperation",
    hook_type=Type.PRE,
)
def extAttemptShopOperation(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    if obj.bOnItemOfTheDay:
        obj.AttemptedShopOperationThing = obj.ItemOfTheDayData.Item        
    else:
        obj.AttemptedShopOperationThing = obj.ActiveTextList.GetHighlightedObject()

    if obj.AttemptedShopOperationThing is not None and not obj.IsComparing():
        if obj.GetStatusForItem(obj.AttemptedShopOperationThing) == 0:
            obj.PlayUISound('ChaChing')
            obj.extConfirmOK()
            return Block

@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:ShowConfirmWrapper",
    hook_type=Type.PRE,
)
def ShowConfirm(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    return Block


build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    options=[],
    keybinds=[],
    hooks=[extAttemptShopOperation, ShowConfirm],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/ConfirmationRemover.json"),
)

logging.info(f"Confirmation Remover Loaded: {__version__}, {__version_info__}")
