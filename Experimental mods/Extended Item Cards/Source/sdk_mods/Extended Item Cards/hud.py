import unrealsdk #type: ignore
from unrealsdk import logging, find_class, construct_object #type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block #type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UScriptStruct #type: ignore
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, EInputEvent, keybind
from pathlib import Path
from mods_base.options import BaseOption, BoolOption

from .functions import GetElementIconForItem, GetFunStats, compare_items, single_item, default_card

pickup_flash_path = "inventory.card1"
flash_element_techicon = "chemicalmod.gotoAndStop"
flash_element_funstats = "funstatsmod.htmlText"
flash_element_number = "reloadspeed.text"
hud_flash_path = "p1.outerequip.equipcard"

PickupCard_obj = None

EquippedCard_obj = None

DesiredWeapon = None




bBL2ArmoredList = BoolOption("Use whitelist", True, description="Uses a list to determine if an enemy should use the armored health bar or not.")
BL2ArmoredList = ["AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.CrimsonLance.Pawn_Balance_Lance_Engineer'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.CrimsonLance.Pawn_Balance_Lance_Defender'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.CrimsonLance.Pawn_Balance_Lance_Defender_Badass'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.CrimsonLance.Pawn_Balance_Lance_Engineer_Badass'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.CrimsonLance.Pawn_Balance_Infantry'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.CrimsonLance.Pawn_Balance_Infantry_Badass'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.CrimsonLance.Pawn_Balance_MasterMcCloud'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.CrimsonLance.Pawn_Balance_RoyalGuard'",
                  "AIPawnBalanceDefinition'gd_Balance_SkillActors.Turret.Pawn_Balance_Scorpio'",
                  "AIPawnBalanceDefinition'gd_Balance_SkillActors.Turret.Pawn_Balance_Scorpio_CrimsonLance'",

                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.Turret.Pawn_Balance_Turret'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.Turret.Pawn_Balance_Turret_Gatling'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.Turret.Pawn_Balance_Turret_Grenade'",
                  "AIPawnBalanceDefinition'gd_Balance_Enemies_Humans.Turret.Pawn_Balance_Turret_Rocket'",
                  
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrabWorms.Pawn_Balance_dlc3_GreenWorm'",
                  
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Named.Pawn_Balance_Ajax'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_BadassDevastator'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLAssassin'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLAssassinBadass'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Named.Pawn_Balance_CLAssassinNamed1'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Named.Pawn_Balance_CLAssassinNamed2'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Named.Pawn_Balance_CLAssassinNamed3'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Named.Pawn_Balance_CLAssassinNamed4'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Named.Pawn_Balance_CLAssassinNamed5'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLBadassArmor'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLBadassRocketeer'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLCorrosive'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLCorrosiveBadass'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLDefender'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLDefenderBadass'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLDriver'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLEngineer'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLEngineerBadass'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLFire'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLFireBadass'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLInfantry'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLInfantryBadass'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLMedic'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLProbe'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLRocketeer'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLRoyalGuard'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLShock'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_CLShockBadass'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Pawn_Balance_Devastator'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Named.Pawn_Balance_Knoxx'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Named.Pawn_Balance_Kyros'",
                  "AIPawnBalanceDefinition'dlc3_gd_balance_enemies.CrimsonLance.Named.Pawn_Balance_Typhon'",


                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_Basic_radical'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_BoxerFirst'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_BoxerMelee'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_ClubsFirst'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_Clubsmelee'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_FirstA'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_FirstB'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_Kamikaze'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_Kamikaze_radical'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_KFirst'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_melee_Radical'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_PunkFirst'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_Punkmelee'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_RangedA'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Pawn_Balance_DLC4_Claptrap_RangedB'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Named.Pawn_Balance_DLC4_Clucktrap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Named.Pawn_Balance_INAC'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.ClapTrap.Named.Pawn_Balance_MINAC'",
                  
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.trap.Delete'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Soldier.Pawn_Balance_Friendlytech'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Soldier.Pawn_Balance_FrindlyGuard'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Soldier.Pawn_Balance_HyperionFriendly'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Soldier.Pawn_Balance_HyperionGuard'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.trap.Pawn_Balance_HyperionGuard-Badass-trap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.trap.Pawn_Balance_HyperionGuard-trap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.trap.Pawn_Balance_HyperionGuardBadass-trap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Soldier.Pawn_Balance_HyperionSoldier'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.trap.Pawn_Balance_HyperionSoldier-Badass-trap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.trap.Pawn_Balance_Hyperionsoldier-trap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Soldier.Pawn_Balance_HyperionSoldier2'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Soldier.Pawn_Balance_Hyperiontech'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.trap.Pawn_Balance_HyperionTech-Badass-trap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.trap.Pawn_Balance_Hyperiontech-trap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Turret.Pawn_Balance_Scorpio-Trap_Hyp'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Turret.Pawn_Balance_Scorpio_Hyp'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Turret.Pawn_Balance_Scorpio_Hyp_F'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Hyperion.Named.Pawn_Balance_SuperbadSoldier'",

                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.KnoxxTrap.Pawn_Balance_KnoxxTrap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.KnoxxTrap.Pawn_Balance_KnoxxTrap2'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.MINAC.Pawn_Balance_MINAC_Eye'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.MINAC.Pawn_Balance_MINAC_EyeTurret'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.MINAC.Pawn_Balance_MINAC_Gatling'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.MINAC.Pawn_Balance_MINAC_Missile'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.SteeleTrap.Pawn_Balance_SteeleTrap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.SteeleTrap.Pawn_Balance_SteeleTrap2'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Test.Pawn_Balance_DLC4_Kamikaze'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Turret.Pawn_Balance_Turret_GatlingTrap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Turret.Pawn_Balance_Turret_GrenadeTrap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Turret.Pawn_Balance_Turret_Rocket_Player_Friendly'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Turret.Pawn_Balance_Turret_RocketTrap'",
                  "AIPawnBalanceDefinition'dlc4_gd_Balance_Enemies.Turret.Pawn_Balance_TurretTrap'"]





def ArmorHealth (hud, enemy):
    Armored = 2

    if str(enemy.Class.name) in "WillowVehicle_WheeledVehicle":

        hud.SingleArgInvokeS("p1.ring.health.bar.gotoAndStop","armored")
    
    elif bBL2ArmoredList.value is True and str(enemy.BalanceDefinitionState.BalanceDefinition) in BL2ArmoredList:
        
        hud.SingleArgInvokeS("p1.ring.health.bar.gotoAndStop","armored")

    elif bBL2ArmoredList.value is False and enemy.BodyClass.DefaultHitRegion.DefaultDamageSurfaceType == Armored:

        hud.SingleArgInvokeS("p1.ring.health.bar.gotoAndStop","armored")




def PickupCard_CompareView(obj, EquippedItem = None):
    GroundItem =  obj.MyHUDOwner.ItemComparison[0]
    
    if EquippedItem is None:
        EquippedItem = obj.MyHUDOwner.ItemComparison[1]

    if GroundItem is not None:
        obj.SingleArgInvokeS(pickup_flash_path + "." + flash_element_techicon, GetElementIconForItem(GroundItem))

        # Set FunStats
        obj.SetVariableString(pickup_flash_path + "." + flash_element_funstats, GetFunStats(GroundItem))


    if GroundItem is not None and EquippedItem is not None:
            compare_items(obj, GroundItem, EquippedItem, pickup_flash_path)


    elif GroundItem is not None and EquippedItem is None and "WillowWeapon" in str(GroundItem.Class):
        single_item(obj, GroundItem, pickup_flash_path)

    else:
        default_card(obj, pickup_flash_path)




def EquippedCardWhileComparing_Text():
    global EquippedCard_obj
    global PickupCard_obj
    CurrentWeapon = get_pc().pawn.weapon

    if PickupCard_obj is not None and EquippedCard_obj is not None and PickupCard_obj.MyHUDOwner.ItemComparison[0] is not None and PickupCard_obj.MyHUDOwner.ItemComparison[1] is not None and "WillowWeapon" not in str(PickupCard_obj.MyHUDOwner.ItemComparison[0].Class):
        EquippedCard_obj.SingleArgInvokeS(hud_flash_path + "." + flash_element_techicon, GetElementIconForItem(PickupCard_obj.MyHUDOwner.ItemComparison[1]))


    if PickupCard_obj is not None and EquippedCard_obj is not None and PickupCard_obj.MyHUDOwner.ItemComparison[0] is not None and "WillowWeapon" in str(PickupCard_obj.MyHUDOwner.ItemComparison[0].Class):
        if CurrentWeapon is not None:
            EquippedCard_obj.SingleArgInvokeS(hud_flash_path + "." + flash_element_techicon, GetElementIconForItem(CurrentWeapon))

            EquippedCard_obj.SetVariableString(hud_flash_path + "." + flash_element_number, str(round(CurrentWeapon.ReloadTimeBaseValue, 1)))        

        



def EquippedCardWhileNotComparing_Text():
    global EquippedCard_obj
    global PickupCard_obj
    global DesiredWeapon

    #print("Change Color")
    #EquippedCard_obj.SingleArgInvokeS("p1.shield.color.gotoAndStop","yellow")
    #EquippedCard_obj.SingleArgInvokeS("p1.ring.shield.color.gotoAndStop","yellow")


    if PickupCard_obj is None or PickupCard_obj is not None and PickupCard_obj.MyHUDOwner.ItemComparison[0] is None:
        if EquippedCard_obj is not None and DesiredWeapon is not None:
            EquippedCard_obj.SetVariableString(hud_flash_path + "." + flash_element_number, str(round(DesiredWeapon.ReloadTimeBaseValue, 1)))
            EquippedCard_obj.SingleArgInvokeS(hud_flash_path + "." + flash_element_techicon, GetElementIconForItem(DesiredWeapon))



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
    global PickupCard_obj
    PickupCard_obj = obj
    PickupCard_CompareView(obj)
    EquippedCardWhileComparing_Text()


@hook(
    hook_func="WillowGame.WillowPawn:WeaponChanged",
    hook_type=Type.POST,
)
def WeaponChanged(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global PickupCard_obj
    if PickupCard_obj is not None:
        PickupCard_CompareView(PickupCard_obj, obj.Weapon)
        EquippedCardWhileComparing_Text()


@hook(
    hook_func="WillowGame.WillowHUDGFxMovie:extEquippedCardOpened",
    hook_type=Type.POST,
)
def extEquippedCardOpened(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global EquippedCard_obj
    EquippedCard_obj = obj
    EquippedCardWhileComparing_Text()
    EquippedCardWhileNotComparing_Text()

@hook(
    hook_func="Engine.InventoryManager:SetCurrentWeapon",
    hook_type=Type.POST,
)
def SetCurrentWeapon(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global DesiredWeapon
    DesiredWeapon = (__args.DesiredWeapon)


@hook(
    hook_func="Engine.WorldInfo:IsMenuLevel",
    hook_type=Type.PRE,
)
def HUDClearVars(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global PickupCard_obj
    global EquippedCard_obj
    global DesiredWeapon
    PickupCard_obj = None
    EquippedCard_obj = None
    DesiredWeapon = None


@hook(
    hook_func="WillowGame.WillowHUDGFxMovie:extEnemyRingFadeInFinished",
    hook_type=Type.POST,
)
def ArmorCheck(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    pc = get_pc()
    if pc is not None:
        if str(pc.pawn.Class.name) in "WillowVehicle_WheeledVehicle" and pc.pawn.lockedpawn is not None:
            ArmorHealth(obj, pc.pawn.lockedpawn)

        elif pc.AutoAimStrategy.InstantaneousTarget is not None:
            ArmorHealth(obj, pc.AutoAimStrategy.InstantaneousTarget)

        elif pc.AutoAimStrategy.LastInstantaneousTarget is not None:
            ArmorHealth(obj, pc.AutoAimStrategy.LastInstantaneousTarget)

