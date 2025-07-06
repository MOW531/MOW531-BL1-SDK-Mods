import unrealsdk
from pathlib import Path
from mods_base import SETTINGS_DIR, build_mod, EInputEvent, keybind, hook
from unrealsdk import logging
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from unrealsdk.hooks import Type, Block
from mods_base.options import BaseOption, SliderOption, BoolOption, SpinnerOption


def Change_AOPersistence(option:BaseOption, value:str):
    if value == "High":
        unrealsdk.find_all("AmbientOcclusionEffect")[2].HistoryConvergenceTime = 0.6
    elif value == "Medium":
        unrealsdk.find_all("AmbientOcclusionEffect")[2].HistoryConvergenceTime = 0.4
    elif value == "Low":
        unrealsdk.find_all("AmbientOcclusionEffect")[2].HistoryConvergenceTime = 0.2
    elif value == "None":
        unrealsdk.find_all("AmbientOcclusionEffect")[2].HistoryConvergenceTime = 0

def Change_AOFilterSize(option:BaseOption, value:float):
    unrealsdk.find_all("AmbientOcclusionEffect")[2].FilterSize = int(value)

def Change_AOQuality(option:BaseOption, value:str):
    if value == "High":
        unrealsdk.find_all("AmbientOcclusionEffect")[2].OcclusionQuality = 0
    elif value == "Medium":
        unrealsdk.find_all("AmbientOcclusionEffect")[2].OcclusionQuality = 1
    elif value == "Low":
        unrealsdk.find_all("AmbientOcclusionEffect")[2].OcclusionQuality = 2


def Change_LineThickness(option:BaseOption, value:float):
    unrealsdk.find_all("EdgeDetectionPostProcessEffect")[2].TexelOffset = value

def Turn_Lines_OnAndOff(option:BaseOption, value:bool):
    unrealsdk.find_all("EdgeDetectionPostProcessEffect")[2].bShowInGame = value

#def Change_MaxFarBlur(option:BaseOption, value:float):
#    unrealsdk.find_all("UberPostProcessEffect")[2].MaxFarBlurAmount = value

#def Change_BloomScale(option:BaseOption, value:float):
#    unrealsdk.find_all("UberPostProcessEffect")[2].BloomScale = value

bLines = BoolOption("Black Outlines", True, on_change=Turn_Lines_OnAndOff)
LineThickness = SliderOption("Line Thickness", 2, 0, 20, 1, True, on_change=Change_LineThickness)
AOPersistence = SpinnerOption("AO Persistence", value="Medium", choices=["None","Low","Medium","High"], wrap_enabled=True, on_change=Change_AOPersistence)
AOQuality = SpinnerOption("AO Quality", value="Medium", choices=["Low","Medium","High"], wrap_enabled=True, on_change=Change_AOQuality)
AOFilterSize = SliderOption("AO Filter Size", 12, 0, 128, 1, True, on_change=Change_AOFilterSize)
#MaxFarBlur = SliderOption("Max Far Blur", 0.3, 0, 10, 0.05, False, on_change=Change_MaxFarBlur)
#BloomScale = SliderOption("Bloom Scale", 0.18, 0, 10, 0.01, False, on_change=Change_BloomScale)



__version__: str
__version_info__: tuple[int, ...]


build_mod(
    options=[bLines, LineThickness, AOQuality, AOFilterSize, AOPersistence],
    keybinds=[],
    hooks=[],
    commands=[],
    settings_file=Path(f"{SETTINGS_DIR}/PostProcessEffects.json"),
)

logging.info(f"Post-Process Effects Loaded: {__version__}, {__version_info__}")
