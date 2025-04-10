import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem, GetFunStats

flash_path = "topLevel_mc.card"
flash_element_main = "rls.text"
flash_element_main_text = "Reload Time"
flash_element_main_text_eridian = "Recharge Delay"
flash_element_number = "reloadspeed.text"
flash_element_arrow3 = "arrow3.gotoAndStop"
flash_element_arrow4 = "arrow4.gotoAndStop"
flash_element_techicon = "chemical.gotoAndStop"
flash_element_funstats = "funstats.htmlText"


ComparingItem = None
LeftCard = 0

# Non-comparing view
def Vendor_NormalView(obj):
    global LeftCard
    if obj.IsComparing() is False:
        
        if obj.bOnItemOfTheDay is True:
            SelectedItem = obj.ItemOfTheDayData.Item
        else:
            SelectedItem = obj.ActiveTextList.GetHighlightedObject()

        if SelectedItem is not None:
            
            #Set Element Icon
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(SelectedItem))

            # Set FunStats
            obj.SetVariableString(flash_path + "1." + flash_element_funstats, GetFunStats(SelectedItem))

            # Add reload info to card
            if "WillowWeapon" in str(SelectedItem.Class):
                
                if str(SelectedItem.DefinitionData.ManufacturerDefinition) in ["ManufacturerDefinition'gd_manufacturers.Manufacturers.Eridian'","ManufacturerDefinition'Eridian_Weapons_Overhaul.Shared.Manufacturers.Eridian'"]:
                    obj.SetVariableString(flash_path + "1." + flash_element_main, flash_element_main_text_eridian)
                else:
                    obj.SetVariableString(flash_path + "1." + flash_element_main, flash_element_main_text)
                    
                obj.SetVariableString(flash_path + "1." + flash_element_number, str(round(SelectedItem.ReloadTimeBaseValue, 1)))
                obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

            else:
                obj.SetVariableString(flash_path + "1." + flash_element_main, "")
                obj.SetVariableString(flash_path + "1." + flash_element_number, "")
                obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

        else:

            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")

            obj.SetVariableString(flash_path + "1." + flash_element_main, "")
            obj.SetVariableString(flash_path + "1." + flash_element_number, "")
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

# Comparing view
def Vendor_CompareView(obj):
    global LeftCard
    global ComparingItem
    if obj.IsComparing() is True:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
        if SelectedItem is not None:
            
            # Set Element Icon
            obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, GetElementIconForItem(SelectedItem))
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(ComparingItem))

            # Set FunStats
            obj.SetVariableString(flash_path + "1." + flash_element_funstats, GetFunStats(ComparingItem))
            obj.SetVariableString(flash_path + "2." + flash_element_funstats, GetFunStats(SelectedItem))


            # Add shield delay arrow and compare
            if "WillowEquipAbleItem" in str(SelectedItem.Class):
                if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                    RightCard = SelectedItem.UIStatModifiers[2].ModifierTotal
                    if RightCard < LeftCard:
                        obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow3,"Up")
                        obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow3,"Down")
                    if RightCard > LeftCard:
                        obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow3,"Down")
                        obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow3,"Up")
                    if RightCard == LeftCard:
                        obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow3,"Same")
                        obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow3,"Same")


            # Add reload info and compare
            if "WillowWeapon" in str(SelectedItem.Class):

                # Second card
                if str(SelectedItem.DefinitionData.ManufacturerDefinition) in ["ManufacturerDefinition'gd_manufacturers.Manufacturers.Eridian'","ManufacturerDefinition'Eridian_Weapons_Overhaul.Shared.Manufacturers.Eridian'"]:
                    obj.SetVariableString(flash_path + "2." + flash_element_main, flash_element_main_text_eridian)
                else:
                    obj.SetVariableString(flash_path + "2." + flash_element_main, flash_element_main_text)

                obj.SetVariableString(flash_path + "2." + flash_element_number, str(round(SelectedItem.ReloadTimeBaseValue, 1)))


                # First card
                if str(ComparingItem.DefinitionData.ManufacturerDefinition) in ["ManufacturerDefinition'gd_manufacturers.Manufacturers.Eridian'","ManufacturerDefinition'Eridian_Weapons_Overhaul.Shared.Manufacturers.Eridian'"]:
                    obj.SetVariableString(flash_path + "1." + flash_element_main, flash_element_main_text_eridian)
                else:
                    obj.SetVariableString(flash_path + "1." + flash_element_main, flash_element_main_text)

                obj.SetVariableString(flash_path + "1." + flash_element_number, str(round(ComparingItem.ReloadTimeBaseValue, 1)))


                if round(ComparingItem.ReloadTimeBaseValue, 1) < round(SelectedItem.ReloadTimeBaseValue, 1):

                    obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow4,"Down")

                    obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Up")

                elif round(ComparingItem.ReloadTimeBaseValue, 1) > round(SelectedItem.ReloadTimeBaseValue, 1):

                    obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow4,"Up")

                    obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Down")

                elif round(ComparingItem.ReloadTimeBaseValue, 1) == round(SelectedItem.ReloadTimeBaseValue, 1):

                    obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow4,"Same")

                    obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Same")
            else:
                obj.SetVariableString(flash_path + "1." + flash_element_main, "")
                obj.SetVariableString(flash_path + "1." + flash_element_number, "")
                obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

                obj.SetVariableString(flash_path + "2." + flash_element_main, "")
                obj.SetVariableString(flash_path + "2." + flash_element_number, "")
                obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow4,"Blank")

        else:

            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")
            obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, "none")

            obj.SetVariableString(flash_path + "1." + flash_element_main, "")
            obj.SetVariableString(flash_path + "1." + flash_element_number, "")
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

            obj.SetVariableString(flash_path + "2." + flash_element_main, "")
            obj.SetVariableString(flash_path + "2." + flash_element_number, "")
            obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow4,"Blank")



@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:extCard2Visible",
    hook_type=Type.POST,
)
def VendorStartCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global LeftCard
    Vendor_NormalView(obj)
    Vendor_CompareView(obj)


@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:UpdateCardPanelWithItemOfTheDay",
    hook_type=Type.POST,
)
def VendorChangeSelectedItemKey(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    Vendor_NormalView(obj)
    Vendor_CompareView(obj)

@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:UpdateCardPanelWithCurrentActiveListEntry",
    hook_type=Type.POST,
)
def VendorChangeSelectedItemMouse(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    Vendor_NormalView(obj)
    Vendor_CompareView(obj)


@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:extCompare",
    hook_type=Type.PRE,
)
def VendorPrepCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global LeftCard
    global ComparingItem
    if obj.bOnItemOfTheDay is True:
        SelectedItem = obj.ItemOfTheDayData.Item
    else:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
    if SelectedItem is not None:

        ComparingItem = SelectedItem

        if "WillowEquipAbleItem" in str(SelectedItem.Class):
            if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                LeftCard = SelectedItem.UIStatModifiers[2].ModifierTotal
