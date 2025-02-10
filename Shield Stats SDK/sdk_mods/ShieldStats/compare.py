import unrealsdk #type: ignore
from unrealsdk.hooks import Type #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook


LeftCard = 0
bBankIsComparing = False

# Vendor/Inventory

def MenuCompare(obj):
    global LeftCard

    SelectedItem = obj.ActiveTextList.GetHighlightedObject()
    if obj.IsComparing() is True:
        if SelectedItem is not None:
            if "WillowEquipAbleItem" in str(SelectedItem.Class):
                if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                    RightCard = SelectedItem.UIStatModifiers[2].ModifierTotal
                    if RightCard < LeftCard:
                        obj.SingleArgInvokeS("topLevel_mc.card2.arrow3.gotoAndStop","Up")
                        obj.SingleArgInvokeS("topLevel_mc.card1.arrow3.gotoAndStop","Down")
                    if RightCard > LeftCard:
                        obj.SingleArgInvokeS("topLevel_mc.card2.arrow3.gotoAndStop","Down")
                        obj.SingleArgInvokeS("topLevel_mc.card1.arrow3.gotoAndStop","Up")
                    if RightCard == LeftCard:
                        obj.SingleArgInvokeS("topLevel_mc.card2.arrow3.gotoAndStop","Same")
                        obj.SingleArgInvokeS("topLevel_mc.card1.arrow3.gotoAndStop","Same")

#Bank

def BankCompare(obj):
    global LeftCard
    global bBankIsComparing

    SelectedItem = obj.ActiveTextList.GetHighlightedObject()
    if bBankIsComparing is True:
        if SelectedItem is not None:
            if "WillowEquipAbleItem" in str(SelectedItem.Class):
                if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                    RightCard = SelectedItem.UIStatModifiers[2].ModifierTotal
                    if RightCard < LeftCard:
                        obj.SingleArgInvokeS("currentPage.card2.arrow3.gotoAndStop","Up")
                        obj.SingleArgInvokeS("currentPage.card1.arrow3.gotoAndStop","Down")
                    if RightCard > LeftCard:
                        obj.SingleArgInvokeS("currentPage.card2.arrow3.gotoAndStop","Down")
                        obj.SingleArgInvokeS("currentPage.card1.arrow3.gotoAndStop","Up")
                    if RightCard == LeftCard:
                        obj.SingleArgInvokeS("currentPage.card2.arrow3.gotoAndStop","Same")
                        obj.SingleArgInvokeS("currentPage.card1.arrow3.gotoAndStop","Same")


#Pickup Card

def HUDCompare(HUD, PickupCard):
    EquippedItem = HUD.ItemComparison[1]
    GroundItem = HUD.ItemComparison[0]
    if PickupCard is not None:
        if GroundItem is not None and EquippedItem is not None:
            if "WillowEquipAbleItem" in str(GroundItem.Class) and "WillowEquipAbleItem" in str(EquippedItem.Class):
                if GroundItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield") and EquippedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                    EquippedItemNumber = EquippedItem.UIStatModifiers[2].ModifierTotal
                    GroundItemNumber = GroundItem.UIStatModifiers[2].ModifierTotal
                    if GroundItemNumber < EquippedItemNumber:
                        PickupCard.SingleArgInvokeS("inventory.card1.arrow3.gotoAndStop","Up")
                    if GroundItemNumber > EquippedItemNumber:
                        PickupCard.SingleArgInvokeS("inventory.card1.arrow3.gotoAndStop","Down")
                    if GroundItemNumber == EquippedItemNumber:
                        PickupCard.SingleArgInvokeS("inventory.card1.arrow3.gotoAndStop","Same")



# Vendor

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
    MenuCompare(obj)


@hook(
    hook_func="WillowGame.VendingMachineGFxMovie:extListMove",
    hook_type=Type.POST,
)
def VendorChangeSelectedItemKey(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    MenuCompare(obj)


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
    MenuCompare(obj)


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
    if obj.bOnItemOfTheDay is True:
        SelectedItem = obj.ItemOfTheDayData.Item
    else:
        SelectedItem = obj.ActiveTextList.GetHighlightedObject()
    if SelectedItem is not None:
        if "WillowEquipAbleItem" in str(SelectedItem.Class):
            if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                LeftCard = SelectedItem.UIStatModifiers[2].ModifierTotal



#Bank


@hook(
    hook_func="WillowGame.BankGFxMovie:extCard2Visible",
    hook_type=Type.POST,
)
def BankStartCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    BankCompare(obj)


@hook(
    hook_func="WillowGame.BankGFxMovie:HandleMove",
    hook_type=Type.POST,
)
def BankChangeSelectedItemKey(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    BankCompare(obj)

@hook(
    hook_func="WillowGame.BankGFxMovie:extListDirectHandler",
    hook_type=Type.POST,
)
def BankChangeSelectedItemMouse(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    BankCompare(obj)

@hook(
    hook_func="WillowGame.BankGFxMovie:StartComparing",
    hook_type=Type.POST,
)
def BankPrepCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global LeftCard
    global bBankIsComparing
    bBankIsComparing = True
    SelectedItem = obj.ActiveTextList.GetHighlightedObject()
    if SelectedItem is not None:
        if "WillowEquipAbleItem" in str(SelectedItem.Class):
            if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                LeftCard = SelectedItem.UIStatModifiers[2].ModifierTotal

@hook(
    hook_func="WillowGame.BankGFxMovie:LeaveCompare",
    hook_type=Type.POST,
)
def BankStopCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global LeftCard
    global bBankIsComparing
    bBankIsComparing = False



# Inventory


@hook(
    hook_func="WillowGame.StatusMenuExGFxMovie:extCard2Visible",
    hook_type=Type.POST,
)
def InvStartCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    MenuCompare(obj)


@hook(
    hook_func="WillowGame.StatusMenuExGFxMovie:extInventoryListMove",
    hook_type=Type.POST,
)
def InvChangeSelectedItemKey(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    MenuCompare(obj)

@hook(
    hook_func="WillowGame.StatusMenuExGFxMovie:UpdateCardPanelWithCurrentActiveListEntry",
    hook_type=Type.POST,
)
def InvChangeSelectedItemMouse(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    MenuCompare(obj)

@hook(
    hook_func="WillowGame.StatusMenuExGFxMovie:extCompare",
    hook_type=Type.PRE,
)
def InvPrepCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global LeftCard
    SelectedItem = obj.GetCurrentHighlightedObject() # obj.ActiveTextList.GetHighlightedObject()
    if SelectedItem is not None:
        if "WillowEquipAbleItem" in str(SelectedItem.Class):
            if SelectedItem.DefinitionData.ItemDefinition == unrealsdk.find_object("ItemDefinition","gd_shields.A_Item.Item_Shield"):
                LeftCard = SelectedItem.UIStatModifiers[2].ModifierTotal


# Pickup card


@hook(
    hook_func="WillowGame.ItemPickupGFxMovie:UpdateCompareAgainstThing",
    hook_type=Type.POST,
)
def PickupcardCompare(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    HUDCompare(obj.MyHUDOwner, obj)