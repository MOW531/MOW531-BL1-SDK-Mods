import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem

flash_path = "currentPage.card"
flash_element_main = "rls.text"
flash_element_main_text = "Reload Time"
flash_element_number = "reloadspeed.text"
flash_element_main_text_eridian = "Recharge Delay"
flash_element_arrow3 = "arrow3.gotoAndStop"
flash_element_arrow4 = "arrow4.gotoAndStop"
flash_element_techicon = "chemical.gotoAndStop"

IsComparing = False

ComparingItem = None

LeftCard = 0

# Non-comparing view
def bank_NormalView(obj):
    global IsComparing
    if IsComparing is False:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
        if SelectedItem is not None:

            # Set Element Icon
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(SelectedItem))

            # Add reload info to the card
            if "WillowWeapon" in str(SelectedItem.Class):

                if SelectedItem.DefinitionData.ManufacturerDefinition == unrealsdk.find_object("ManufacturerDefinition","gd_manufacturers.Manufacturers.Eridian"):
                    obj.SetVariableString(flash_path + "1." + flash_element_main, flash_element_main_text_eridian)
                else:
                    obj.SetVariableString(flash_path + "1." + flash_element_main, flash_element_main_text)

                obj.SetVariableString(flash_path + "1." + flash_element_number, str(round(SelectedItem.ReloadTimeBaseValue, 1)))
                obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

            # Make sure the reload text it cleared when not wanted
            else:
                obj.SetVariableString(flash_path + "1." + flash_element_main, "")
                obj.SetVariableString(flash_path + "1." + flash_element_number, "")
                obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

        # Make sure the reload text and element icon are cleared when not wanted
        else:

            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")

            obj.SetVariableString(flash_path + "1." + flash_element_main, "")
            obj.SetVariableString(flash_path + "1." + flash_element_number, "")
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

# Compare view
def bank_CompareView(obj):
    global ComparingItem
    global IsComparing
    global LeftCard
    if IsComparing is True:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
        if SelectedItem is not None:

            # Set Element Icon
            if SelectedItem is not None and ComparingItem is not None:
                obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, GetElementIconForItem(SelectedItem))
                obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, GetElementIconForItem(ComparingItem))

            #Set shield delay arrow
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

            # Add reload info to the card and compare
            if "WillowWeapon" in str(SelectedItem.Class):

                # The second card that appears
                if SelectedItem.DefinitionData.ManufacturerDefinition == unrealsdk.find_object("ManufacturerDefinition","gd_manufacturers.Manufacturers.Eridian"):
                    obj.SetVariableString(flash_path + "2." + flash_element_main, flash_element_main_text_eridian)
                else:
                    obj.SetVariableString(flash_path + "2." + flash_element_main, flash_element_main_text)

                obj.SetVariableString(flash_path + "2." + flash_element_number, str(round(SelectedItem.ReloadTimeBaseValue, 1)))
                

                # The first card that appears
                if ComparingItem.DefinitionData.ManufacturerDefinition == unrealsdk.find_object("ManufacturerDefinition","gd_manufacturers.Manufacturers.Eridian"):
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



                # Clear unwanted info
            else:
                obj.SetVariableString(flash_path + "1." + flash_element_main, "")
                obj.SetVariableString(flash_path + "1." + flash_element_number, "")
                obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

                obj.SetVariableString(flash_path + "2." + flash_element_main, "")
                obj.SetVariableString(flash_path + "2." + flash_element_number, "")
                obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow4,"Blank")

            # Clear unwanted info
        else:

            obj.SingleArgInvokeS(flash_path + "2." + flash_element_techicon, "none")
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_techicon, "none")


            obj.SetVariableString(flash_path + "1." + flash_element_main, "")
            obj.SetVariableString(flash_path + "1." + flash_element_number, "")
            obj.SingleArgInvokeS(flash_path + "1." + flash_element_arrow4,"Blank")

            obj.SetVariableString(flash_path + "2." + flash_element_main, "")
            obj.SetVariableString(flash_path + "2." + flash_element_number, "")
            obj.SingleArgInvokeS(flash_path + "2." + flash_element_arrow4,"Blank")



@hook(
    hook_func="WillowGame.BankGFxMovie:extCard2Visible",
    hook_type=Type.POST,
)
def bankStartCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    bank_NormalView(obj)
    bank_CompareView(obj)


@hook(
    hook_func="WillowGame.BankGFxMovie:UpdateCardPanelWithCurrentActiveListEntry",
    hook_type=Type.POST,
)
def bankChangeSelectedItemMouse(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    bank_NormalView(obj)
    bank_CompareView(obj)


@hook(
    hook_func="WillowGame.BankGFxMovie:StartComparing",
    hook_type=Type.PRE,
)
def bankPrepCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global LeftCard
    global ComparingItem
    global IsComparing
    IsComparing = True
    SelectedItem = obj.ActiveTextList.GetHighlightedObject()
    if SelectedItem is not None:
        ComparingItem = SelectedItem

        if "WillowEquipAbleItem" in str(SelectedItem.Class):
            if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                LeftCard = SelectedItem.UIStatModifiers[2].ModifierTotal


@hook(
    hook_func="WillowGame.BankGFxMovie:LeaveCompare",
    hook_type=Type.PRE,
)
def bankStopCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global IsComparing
    IsComparing = False