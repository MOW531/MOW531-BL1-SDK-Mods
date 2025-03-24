import unrealsdk#type: ignore
from pathlib import Path#type: ignore
from unrealsdk.hooks import Type, add_hook, remove_hook, Block#type: ignore
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction#type: ignore
from mods_base import hook, get_pc #type: ignore
from mods_base.options import BaseOption, BoolOption#type: ignore
from mods_base import SETTINGS_DIR, SliderOption#type: ignore
from mods_base import build_mod#type: ignore
from unrealsdk import logging, find_object#type: ignore

bPrepWorkDone = False

GameStage: SliderOption = SliderOption("Playthrough 3 Base Level",
            1.0,
            -15.0,
            15.0,
            1.0,
            False,
            description="The base level for enemies and missions will be set to character level plus this number.",
            on_change = lambda _, 
            new_value: SetGlobalGameStage(_, new_value))



GlobalsDef = None
DLC1Globals = None
DLC2Globals = None
DLC3Globals = None
DLC4Globals = None
GlobalGameStage = None
GlobalGameStageSetting = None
ResetPlaythrough = None
BadlandsLoaded = None
WillowGFxLobbySinglePlayer = None
Intro = None
DocIsIn = None
SkagsAtGate = None
IntroStruct = None
DocIsInStruct = None
PT3ResetData = None




@hook(
    hook_func="WillowGame.WillowGFxMoviePressStart:extContinue",
    hook_type=Type.POST,
)
def PressStart(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    global bPrepWorkDone

    global GlobalsDef
    global DLC1Globals
    global DLC2Globals
    global DLC3Globals
    global DLC4Globals
    global GlobalGameStage
    global GlobalGameStageSetting
    global ResetPlaythrough
    global BadlandsLoaded
    global WillowGFxLobbySinglePlayer
    global Intro
    global DocIsIn
    global SkagsAtGate
    global IntroStruct
    global DocIsInStruct
    global PT3ResetData

    if bPrepWorkDone is False:
        bPrepWorkDone = True

        unrealsdk.load_package("gd_Balance_Enemies_Humans")
        unrealsdk.load_package("gd_Balance_HealthAndDamage")
        unrealsdk.load_package("gd_GameStages_PT3")

        unrealsdk.load_package("gd_Balance_Enemies_Humans.Bandits.Common.Pawn_Balance_Grunt_00_Intro")
        unrealsdk.load_package("gd_Balance_Enemies_Humans.Bandits.Common.Pawn_Balance_Elite_00_Intro")
        unrealsdk.load_package("gd_Balance_HealthAndDamage.HealthMultipliers.Enemy_Health_ByPlaythrough")
        unrealsdk.load_package("gd_Balance_HealthAndDamage.DamageMultipliers.Enemy_Damage_ByPlaythrough")
        unrealsdk.load_package("gd_Balance_HealthAndDamage.HealthMultipliers.Guardian_Shield_ByPlaythrough")

        unrealsdk.load_package("gd_GameStages_PT3.Attribute.GlobalGameStage")
        unrealsdk.load_package("gd_GameStages_PT3.Balance.Balance_P1_Arid")
        unrealsdk.load_package("gd_GameStages_PT3.Balance.Balance_P1_Headlands")
        unrealsdk.load_package("gd_GameStages_PT3.Balance.Balance_P1_Scrap")
        unrealsdk.load_package("gd_GameStages_PT3.Balance.Balance_P1_Thor")
        unrealsdk.load_package("gd_GameStages_PT3.DLC1.Balance.Balance_P1_DLC1")
        unrealsdk.load_package("gd_GameStages_PT3.DLC2.Balance.Balance_P1_DLC2")
        unrealsdk.load_package("gd_GameStages_PT3.DLC3.Balance.Balance_P1_DLC3")
        unrealsdk.load_package("gd_GameStages_PT3.DLC4.Balance.Balance_P1_DLC4")

        unrealsdk.load_package("gd_globals.General.Globals")
        unrealsdk.load_package("dlc1_PackageDefinition.CustomGlobals")
        unrealsdk.load_package("dlc2_packagedefinition.CustomGlobals")
        unrealsdk.load_package("dlc3_PackageDefinition.CustomGlobals")
        unrealsdk.load_package("dlc4_PackageDefinition.CustomGlobals")

        unrealsdk.load_package("gd_RegistrationStationList.Lookups.RegistrationStationLookup")
        unrealsdk.load_package("Z0_Missions.Missions.M_BuyGrenades")
        unrealsdk.load_package("Z0_Missions.Missions.M_JumpTheGap")



        FastTravelList = find_object("EmergencyTeleportOutpostLookup","gd_RegistrationStationList.Lookups.RegistrationStationLookup")
        FastTravelList.ObjectFlags |= 0x4000

        GlobalsDef = find_object("GlobalsDefinition","gd_globals.General.Globals")
        GlobalsDef.ObjectFlags |= 0x4000

        DLC1Globals = find_object("GlobalsDefinition","dlc1_PackageDefinition.CustomGlobals")
        DLC1Globals.ObjectFlags |= 0x4000

        DLC2Globals = find_object("GlobalsDefinition","dlc2_packagedefinition.CustomGlobals")
        DLC2Globals.ObjectFlags |= 0x4000

        DLC3Globals = find_object("GlobalsDefinition","dlc3_PackageDefinition.CustomGlobals")
        DLC3Globals.ObjectFlags |= 0x4000

        DLC4Globals = find_object("GlobalsDefinition","dlc4_PackageDefinition.CustomGlobals")
        DLC4Globals.ObjectFlags |= 0x4000

        GlobalGameStage = find_object("AttributeDefinition","gd_GameStages_PT3.Attribute.GlobalGameStage")
        GlobalGameStage.ObjectFlags |= 0x4000
        GlobalGameStageSetting = GameStage.value

        EnemyHealth = find_object("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthMultipliers.Enemy_Health_ByPlaythrough")
        EnemyHealth.ConditionalInitialization.ConditionalExpressionList.append(EnemyHealth.ConditionalInitialization.ConditionalExpressionList[1])
        EnemyHealth.ConditionalInitialization.ConditionalExpressionList[2].Expressions[0].ConstantOperand2 = 3

        EnemyDamage = find_object("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.DamageMultipliers.Enemy_Damage_ByPlaythrough")
        EnemyDamage.ConditionalInitialization.ConditionalExpressionList.append(EnemyDamage.ConditionalInitialization.ConditionalExpressionList[1])
        EnemyDamage.ConditionalInitialization.ConditionalExpressionList[2].Expressions[0].ConstantOperand2 = 3

        GuardianShield = find_object("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthMultipliers.Guardian_Shield_ByPlaythrough")
        GuardianShield.ConditionalInitialization.ConditionalExpressionList.append(GuardianShield.ConditionalInitialization.ConditionalExpressionList[1])
        GuardianShield.ConditionalInitialization.ConditionalExpressionList[2].Expressions[0].ConstantOperand2 = 3

        BaseGameBalanceStruct = unrealsdk.make_struct("PlayThroughData",PlayThroughNumber=3)
        BaseGameBalanceStruct.BalanceDefinitions.append(find_object("GameBalanceDefinition","gd_gamestages_vs.Balance.Balance_Arena"))
        BaseGameBalanceStruct.BalanceDefinitions.append(find_object("GameBalanceDefinition","gd_GameStages_PT3.Balance.Balance_P1_Arid"))
        BaseGameBalanceStruct.BalanceDefinitions.append(find_object("GameBalanceDefinition","gd_GameStages_PT3.Balance.Balance_P1_Headlands"))
        BaseGameBalanceStruct.BalanceDefinitions.append(find_object("GameBalanceDefinition","gd_GameStages_PT3.Balance.Balance_P1_Scrap"))
        BaseGameBalanceStruct.BalanceDefinitions.append(find_object("GameBalanceDefinition","gd_GameStages_PT3.Balance.Balance_P1_Thor"))
        GlobalsDef.RegionBalanceData.append(BaseGameBalanceStruct)
        GlobalsDef.MaxAllowedPlayThroughs = 3

        DLC1BalanceStruct = unrealsdk.make_struct("PlayThroughData",PlayThroughNumber=3)
        DLC1BalanceStruct.BalanceDefinitions.append(find_object("GameBalanceDefinition","gd_GameStages_PT3.DLC1.Balance.Balance_P1_DLC1"))
        DLC1Globals.RegionBalanceData.append(DLC1BalanceStruct)

        DLC2BalanceStruct = unrealsdk.make_struct("PlayThroughData",PlayThroughNumber=3)
        DLC2BalanceStruct.BalanceDefinitions.append(find_object("GameBalanceDefinition","gd_GameStages_PT3.DLC2.Balance.Balance_P1_DLC2"))
        DLC2Globals.RegionBalanceData.append(DLC2BalanceStruct)

        DLC3BalanceStruct = unrealsdk.make_struct("PlayThroughData",PlayThroughNumber=3)
        DLC3BalanceStruct.BalanceDefinitions.append(find_object("GameBalanceDefinition","gd_GameStages_PT3.DLC3.Balance.Balance_P1_DLC3"))
        DLC3Globals.RegionBalanceData.append(DLC3BalanceStruct)

        DLC4BalanceStruct = unrealsdk.make_struct("PlayThroughData",PlayThroughNumber=3)
        DLC4BalanceStruct.BalanceDefinitions.append(find_object("GameBalanceDefinition","gd_GameStages_PT3.DLC4.Balance.Balance_P1_DLC4"))
        DLC4Globals.RegionBalanceData.append(DLC4BalanceStruct)

        Grunts =find_object("AIPawnBalanceDefinition","gd_Balance_Enemies_Humans.Bandits.Common.Pawn_Balance_Grunt_00_Intro")
        Grunts.ObjectFlags |= 0x4000
        Grunts.Grades[2].GameStageRequirement.MaxGameStage = 100
        Elites = find_object("AIPawnBalanceDefinition","gd_Balance_Enemies_Humans.Bandits.Common.Pawn_Balance_Elite_00_Intro")
        Elites.ObjectFlags |= 0x4000
        Elites.Grades[2].GameStageRequirement.MaxGameStage = 100

        ResetPlaythrough = False
        BadlandsLoaded = False

        WillowGFxLobbySinglePlayer = None

        Intro = unrealsdk.find_object("MissionDefinition","Z0_Missions.Missions.M_IntroStateSaver")
        DocIsIn = unrealsdk.find_object("MissionDefinition","Z0_Missions.Missions.M_AccessStores")
        SkagsAtGate = unrealsdk.find_object("MissionDefinition","Z0_Missions.Missions.M_KillSkags_Zed")

        IntroStruct =unrealsdk.make_struct("MissionStatus",
                                            MissionDef=Intro,
                                            Status=4,
                                            Objectives=[],
                                            )
        DocIsInStruct =unrealsdk.make_struct("MissionStatus",
                                            MissionDef=DocIsIn,
                                            Status=4,
                                            Objectives=[],
                                            )

        PT3ResetData = unrealsdk.make_struct("MissionPlaythroughInfo",
                                            MissionList=[IntroStruct, DocIsInStruct],
                                            UnloadableDlcMissionList=[],
                                            ActiveMission=SkagsAtGate,
                                            PlayThroughNumber=2)
        

        FastTravelList.OutpostLookupList[3].MissionDependencies[0].MissionDefinition = find_object("MissionDefinition","Z0_Missions.Missions.M_BuyGrenades")
        FastTravelList.OutpostLookupList[26].MissionDependencies[0].MissionDefinition = find_object("MissionDefinition","Z0_Missions.Missions.M_JumpTheGap")


        get_pc().WorldInfo.ForceGarbageCollection()

def BuildResetMenu():
    global WillowGFxLobbySinglePlayer
    Dlg = WillowGFxLobbySinglePlayer.GetWillowOwner().GFxUIManager.ShowDialog()
    Message = "Are you sure you want to reset your Playthrough 3?"
    Dlg.AppendButton('ConfirmReset', 'Reset Playthrough 3', Message, Dlg.OnButtonClicked)
    Dlg.AppendButton('CancelReset', 'Cancel', Message, Dlg.OnButtonClicked)
    Dlg.ApplyLayout()
    return

def SetGlobalGameStage(_: SliderOption, new_value: float):
    global GlobalGameStage, GlobalGameStageSetting
    if get_pc().Pawn:
        PlayerLevel = get_pc().Pawn.GetExpLevel()
        GlobalGameStage.ValueResolverChain[0].ConstantValue = PlayerLevel + new_value
    GlobalGameStageSetting = new_value
    return

@hook(
    hook_func="WillowGame.WillowGFxLobbySinglePlayer:FinishLoadGame",
    hook_type=Type.PRE,
)
def FinishLoadGame(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    global WillowGFxLobbySinglePlayer
    global ResetPlaythrough
    WillowGFxLobbySinglePlayer = obj
    Profile = None
    Dlg = None
    ResetPlaythrough = False

    Profile = get_pc().GetWillowGlobals().GetWillowSaveGameManager().GetCachedPlayerProfile(obj.GetControllerId())

    if Profile != None and Profile.SaveGameId != -1:
        if Profile.PlaythroughsCompleted == 1:
            Dlg = obj.GetWillowOwner().GFxUIManager.ShowDialog()
            Dlg.AutoLocEnable("WillowMenu", "dlgDifficultySelect")

            Dlg.AppendButton('Dif2', 'Playthrough 2', "", obj.OnChooseDifficulty_Click)
            Dlg.AppendButton('Dif1', 'Playthrough 1', "", obj.OnChooseDifficulty_Click)
            Dlg.AutoAppendButton('Cancel')
            Dlg.ApplyLayout()
            Dlg.SetDefaultButton('Dif2', False)

        elif Profile.PlaythroughsCompleted > 1:
            Dlg = obj.GetWillowOwner().GFxUIManager.ShowDialog()
            Dlg.AutoLocEnable("WillowMenu", "dlgDifficultySelect")

            Dlg.AppendButton('Dif3', 'Playthrough 3', "(Press R to Reset)", Dlg.OnButtonClicked)
            Dlg.AppendButton('Dif2', 'Playthrough 2', "", obj.OnChooseDifficulty_Click)
            Dlg.AppendButton('Dif1', 'Playthrough 1', "", obj.OnChooseDifficulty_Click)

            Dlg.AutoAppendButton('Cancel')
            Dlg.ApplyLayout()
            Dlg.SetDefaultButton('Dif2', False)            
        else:
            obj.LaunchSaveGame(Profile.PlaythroughsCompleted)

    else:
        obj.LaunchNewGame()
    return Block

@hook(
    hook_func="WillowGame.WillowPlayerController:OnExpLevelChange",
    hook_type=Type.POST,
)
def OnExpLevelChange(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    if obj.WorldInfo.NetMode == 3:
        return
    global GlobalGameStage, GlobalGameStageSetting
    BodyInterface = obj.Pawn.QueryInterface(unrealsdk.find_class('IBodyPawn'))
    if BodyInterface:
        WPawn = BodyInterface.GetAWillowPawn()

    if obj.GetCurrentPlaythrough() == 2 and WPawn:
        GlobalGameStage.ValueResolverChain[0].ConstantValue = WPawn.GetExpLevel() + GlobalGameStageSetting

@hook(
    hook_func="WillowGame.WillowGFxDialogBox:OnButtonClicked",
    hook_type=Type.POST,
)
def OnButtonClicked(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    global WillowGFxLobbySinglePlayer, ResetPlaythrough, GlobalsDef, SkagsAtGate, GlobalGameStage, GlobalGameStageSetting
    
    if obj.DialogResult == 'Dif3':
        PlayerLevel = get_pc().GetWillowGlobals().GetWillowSaveGameManager().GetCachedPlayerProfile(obj.GetControllerId()).ExpLevel
        GlobalGameStage.ValueResolverChain[0].ConstantValue = PlayerLevel + GlobalGameStageSetting
        GlobalsDef.FastTravelMission = SkagsAtGate
        WillowGFxLobbySinglePlayer.LaunchSaveGame(2)

    elif obj.DialogResult == 'ConfirmReset':
        ResetPlaythrough = True
        PlayerLevel =  get_pc().GetWillowGlobals().GetWillowSaveGameManager().GetCachedPlayerProfile(obj.GetControllerId()).ExpLevel
        GlobalGameStage.ValueResolverChain[0].ConstantValue = PlayerLevel + GlobalGameStageSetting
        add_hook("WillowGame.WillowPlayerController:TeleportPlayerToHoldingCell", Type.POST, "ResetLoad", on_player_loaded)
        GlobalsDef.FastTravelMission = SkagsAtGate
        WillowGFxLobbySinglePlayer.LaunchSaveGame(2)

    elif obj.DialogResult == 'Dif1' or obj.DialogResult == 'Dif2':
        unrealsdk.load_package('I1_Missions.Missions.M_Powerlines')
        GlobalsDef.FastTravelMission = unrealsdk.find_object('MissionDefinition','I1_Missions.Missions.M_Powerlines')
    return

@hook(
    hook_func="WillowGame.WillowGFxDialogBox:HandleInputKey",
    hook_type=Type.PRE,
)
def HandleInputKey(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction):
    if args.ukey == "R" and obj.Buttons and obj.Buttons[0].Tag == 'Dif3':
        if obj.CurrentSelection == 0:
            BuildResetMenu()


def on_player_loaded(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global ResetPlaythrough, BadlandsLoaded, PT3ResetData
    PC = obj
    if ResetPlaythrough is True and BadlandsLoaded is True:
        ResetPlaythrough = False
        BadlandsLoaded = False
        unrealsdk.find_all("MissionTracker")[1].MissionList.clear()
        PC.MissionPlaythroughData[2] = PT3ResetData
        KillSkags = unrealsdk.find_object("MissionDefinition","Z0_Missions.Missions.M_KillSkags_Zed")
        PC.AddMissionToTrack(KillSkags)
        PC.SetMissionStatus(PC.GetMissionIndexForMission(KillSkags), 1)
        PC.EchoPlaythroughData[2].echolist.clear()
        unrealsdk.find_all("EchoTracker")[1].EchoCallList.clear()
        PC.ServerTeleportPlayerToOutpost("Fyrestone")
        remove_hook("WillowGame.WillowPlayerController:TeleportPlayerToHoldingCell", Type.POST, "ResetLoad")
    
    if ResetPlaythrough is True and BadlandsLoaded is False:
        if not PC.WorldInfo.GetMapName() == "Arid_Arena_Coliseum_P":
            PC.ServerTeleportPlayerToOutpost("PitArena")
        else:
            PC.ServerTeleportPlayerToOutpost("RuinsArena")
        BadlandsLoaded = True    

__version__: str
__version_info__: tuple[int, ...]

build_mod(
    hooks=[OnButtonClicked, FinishLoadGame, HandleInputKey, OnExpLevelChange, PressStart],
    options=[GameStage],
    settings_file=Path(f"{SETTINGS_DIR}/PT3.json"),
)

logging.info(f"Playthrough 3 Loaded: {__version__}, {__version_info__}")
