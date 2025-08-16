from mods_base import get_pc
from unrealsdk import find_object, make_struct, construct_object, load_package
from unrealsdk.unreal import UObject, WrappedStruct

def get_mission_status(mission_name:str) -> int:
    pc = get_pc()
    PlayThroughNumber = pc.GetCurrentPlaythrough()
    in_mission = find_object("MissionDefinition", mission_name)
    for mission in pc.MissionPlaythroughData[PlayThroughNumber].MissionList:
        if mission.MissionDef == in_mission:
            return mission.Status
    return -1

def make_new_link(link_op:UObject, index:int = 0) -> WrappedStruct:
    return make_struct("SeqOpOutputInputLink",
                        LinkedOp=link_op,
                        InputLinkIdx=index)

class Map:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Map.registry[cls.name] = cls#type:ignore

    def on_map_loaded(self):
        pass

class Intro(Map):
    name = "arid_intro_p"

    def on_map_loaded(self):
        #Skips Marcus intro
        LoadingMovie = find_object("SeqAct_LoadingMovie", "arid_intro_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_LoadingMovie_0")
        ToggleHidden = find_object("SeqAct_ToggleHidden", "arid_intro_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ToggleHidden_16")
        MarcusAudio = find_object("SeqAct_Interp", "arid_intro_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_14")
        LoadingMovie.OutputLinks[0].Links = [make_new_link(ToggleHidden, 1), make_new_link(MarcusAudio)]

        #Skips Angel cutscene
        SwitchByPlatform = find_object("WillowSeqCond_SwitchByPlatform", "arid_intro_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqCond_SwitchByPlatform_0")
        MapChange = find_object("WillowSeqAct_PrepareMapChangeFromDefinition", "arid_intro_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqAct_PrepareMapChangeFromDefinition_1")
        SwitchByPlatform.OutputLinks[0].Links = [make_new_link(MapChange)]

class AridBadlands(Map):
    name = "arid_p"

    def on_map_loaded(self):
        #Dr. Zed
        DrZed_starttrigger = find_object("object", "arid_firestone.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_Used_6")
        DrZed_starttrigger.OutputLinks.clear()

        #T.K. Baha
        TKBaha_starttrigger = find_object("object", "arid_p.TheWorld:PersistentLevel.Main_Sequence.TitleCards.SeqEvent_Touch_0")
        TKBaha_end = find_object("object", "arid_p.TheWorld:PersistentLevel.Main_Sequence.TitleCards.SeqAct_ApplyBehavior_0")
        TKBaha_starttrigger.OutputLinks[0].Links = [make_new_link(TKBaha_end)]

class SkagGully(Map):
    name = "Arid_SkagGully_P"

    def on_map_loaded(self):
        #Nine-Toes
        NineToes_starttrigger = find_object("object", "Arid_SkagGully_NineToes.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_Touch_1")
        NineToes_end_1 = find_object("object", "Arid_SkagGully_NineToes.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Toggle_0")
        NineToes_end_2 = find_object("object", "Arid_SkagGully_NineToes.TheWorld:PersistentLevel.Main_Sequence.WillowSeqAct_DisableCombatMusicLogic_0")
        NineToes_end_3 = find_object("object", "Arid_SkagGully_NineToes.TheWorld:PersistentLevel.Main_Sequence.SeqAct_PlayMusicTrack_0")
        NineToes_end_4 = find_object("object", "Arid_SkagGully_NineToes.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ToggleHidden_0")
        NineToes_starttrigger.OutputLinks[0].Links = [make_new_link(NineToes_end_1), make_new_link(NineToes_end_2), make_new_link(NineToes_end_3), make_new_link(NineToes_end_4)]

class HeadStoneMines(Map):
    name = "Arid_Mine_P"

    def on_map_loaded(self):
        #Sledge
        Sledge_starttrigger = find_object("Object","Arid_Mine_Building.TheWorld:PersistentLevel.Main_Sequence.SeqCond_CompareBool_4")
        Sledge_end_1 = find_object("Object","Arid_Mine_Building.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_19")
        Sledge_end_2 = find_object("Object","Arid_Mine_Building.TheWorld:PersistentLevel.Main_Sequence.GearboxSeqAct_PopulationOpportunityLink_0")
        Sledge_end_3 = find_object("Object","Arid_Mine_Building.TheWorld:PersistentLevel.Main_Sequence.GearboxSeqAct_PopulationOpportunityLink_4")
        Sledge_starttrigger.OutputLinks[0].Links[0] = make_new_link(Sledge_end_1)
        Sledge_starttrigger.OutputLinks[0].Links.append(make_new_link(Sledge_end_2))
        Sledge_starttrigger.OutputLinks[0].Links.append(make_new_link(Sledge_end_3))

class KromsCanyon(Map):
    name = "Scrap_Canyon_P"

    def on_map_loaded(self):
        #Krom
        Krom_starttrigger = find_object("Object","Scrap_Canyon_P.TheWorld:PersistentLevel.Main_Sequence.Krom.SeqEvent_Touch_0")
        Krom_end = find_object("Object","Scrap_Canyon_P.TheWorld:PersistentLevel.Main_Sequence.Krom.SeqAct_Toggle_4")
        Krom_starttrigger.OutputLinks[0].Links = [make_new_link(Krom_end)]

class TrashCoast(Map):
    name = "scrap_trashcoast_p"

    def on_map_loaded(self):
        #Rakk Hive
        RakkHive_starttrigger = find_object("Object","Scrap_TrashCoast_P.TheWorld:PersistentLevel.Main_Sequence.RakkHive.SeqEvent_Touch_9")
        RakkHive_end_1 = find_object("Object","Scrap_TrashCoast_P.TheWorld:PersistentLevel.Main_Sequence.RakkHive.SeqAct_Interp_4")
        RakkHive_end_2 = find_object("Object","Scrap_TrashCoast_P.TheWorld:PersistentLevel.Main_Sequence.RakkHive.SeqAct_ActivateRemoteEvent_0")
        RakkHive_end_3 = find_object("Object","Scrap_TrashCoast_P.TheWorld:PersistentLevel.Main_Sequence.RakkHive.SeqAct_Toggle_10")
        RakkHive_end_4 = find_object("Object","Scrap_TrashCoast_P.TheWorld:PersistentLevel.Main_Sequence.RakkHive.SeqAct_ToggleHidden_2")
        RakkHive_starttrigger.OutputLinks[0].Links = [make_new_link(RakkHive_end_1), make_new_link(RakkHive_end_2), make_new_link(RakkHive_end_3), make_new_link(RakkHive_end_4)]

class SaltFlats(Map):
    name = "Interlude_2_P"

    def on_map_loaded(self):
        #Flynt
        Flynt_starttrigger = find_object("Object","Interlude_2_Digger.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionStatusChanged_0")
        Flynt_end_1 = find_object("Object","Interlude_2_Digger.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Toggle_13")
        Flynt_end_2 = find_object("Object","Interlude_2_Digger.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Toggle_10")
        Flynt_starttrigger.OutputLinks[1].Links = [make_new_link(Flynt_end_1, 1), make_new_link(Flynt_end_2)]
        Flynt_starttrigger.OutputLinks[2].Links = [make_new_link(Flynt_end_1, 1), make_new_link(Flynt_end_2)]

class TheVault(Map):
    name = "Waste_Vault_P"

    def on_map_loaded(self):
        #Destroyer Intro
        DestroyerIntro_starttrigger = find_object("Object","Waste_Vault_Script.TheWorld:PersistentLevel.Main_Sequence.Intro.SeqAct_ApplyBehavior_2")
        DestroyerIntro_end_1 = find_object("Object","Waste_Vault_Script.TheWorld:PersistentLevel.Main_Sequence.Intro.SeqAct_ActivateRemoteEvent_1")
        DestroyerIntro_end_2 = find_object("Object","Waste_Vault_Script.TheWorld:PersistentLevel.Main_Sequence.Intro.SeqAct_SetSoundMode_1")
        DestroyerIntro_end_3 = find_object("Object","Waste_Vault_Script.TheWorld:PersistentLevel.Main_Sequence.Intro.WillowSeqAct_CompleteMission_1")
        DestroyerIntro_end_4 = find_object("Object","Waste_Vault_Script.TheWorld:PersistentLevel.Main_Sequence.Intro.SeqAct_Delay_0")
        DestroyerIntro_starttrigger.OutputLinks[0].Links = [make_new_link(DestroyerIntro_end_1), make_new_link(DestroyerIntro_end_2), make_new_link(DestroyerIntro_end_3), make_new_link(DestroyerIntro_end_4)]



        #Destroyer Outro and credits
        DestroyerOutro_starttrigger = find_object("Object","Waste_Vault_Script.TheWorld:PersistentLevel.Main_Sequence.Outro.WillowSeqAct_MarkPlaythroughCompleted_0")
        DestroyerOutro_end = find_object("Object","Waste_Vault_Script.TheWorld:PersistentLevel.Main_Sequence.Outro.SeqAct_SetSoundMode_1")
        DestroyerOutro_matinee = find_object("Object","Waste_Vault_Script.TheWorld:PersistentLevel.Main_Sequence.Outro.SeqAct_Interp_0")
        DestroyerOutro_starttrigger.OutputLinks[0].Links.pop(1)
        DestroyerOutro_matinee.OutputLinks[0].Links = [make_new_link(DestroyerOutro_end)]

        #Unlinks the camera actors
        DestroyerOutro_matinee.VariableLinks.pop(21)
        DestroyerOutro_matinee.VariableLinks.pop(20)
        DestroyerOutro_matinee.VariableLinks.pop(19)
        DestroyerOutro_matinee.VariableLinks.pop(18)
        DestroyerOutro_matinee.VariableLinks.pop(17)
        DestroyerOutro_matinee.VariableLinks.pop(16)

        #Remove slomo
        DestroyerOutro_matinee.VariableLinks[0].LinkedVariables[0].InterpGroups[33].InterpTracks.pop(2)


class JakobsCove(Map):
    name = "dlc1_island_p"

    def on_map_loaded(self):
        #DLC1 Intro
        DLC1_Intro_starttrigger = find_object("Object","dlc1_island_p.TheWorld:PersistentLevel.Main_Sequence.Transitions.SeqCond_CompareBool_1")
        DLC1_Intro_starttrigger.OutputLinks[0].Links.clear()

class HallowsEnd(Map):
    name = "dlc1_swamp_ned_p"

    def on_map_loaded(self):
        #Dr. Ned
        DLC1_Ned_starttrigger = find_object("Object","dlc1_swamp_ned_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MeetNed.WillowSeqEvent_MissionStatusChanged_0")
        DLC1_Ned_starttrigger.OutputLinks[1].Links.clear()
        DLC1_Ned_starttrigger.OutputLinks[2].Links.clear()

        #T.K. Baha
        DLC1_TKBaha_starttrigger = find_object("Object","dlc1_swamp_ned_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FindZombieTK.SeqAct_Toggle_0")
        DLC1_TKBaha_starttrigger.EventLinks.clear()

class GenerallyHospital(Map):
    name = "dlc1_monsterhouse_p"

    def on_map_loaded(self):
        #Wereskag
        DLC1_Wereskag_starttrigger = find_object("Object","dlc1_monsterhouse_Dynamic.TheWorld:PersistentLevel.Main_Sequence.WereskagTitleCard.WillowSeqEvent_MissionStatusChanged_0")
        DLC1_Wereskag_end_1 = find_object("Object","dlc1_monsterhouse_Dynamic.TheWorld:PersistentLevel.Main_Sequence.WereskagTitleCard.SeqAct_Toggle_0")
        DLC1_Wereskag_end_2 = find_object("Object","dlc1_monsterhouse_Dynamic.TheWorld:PersistentLevel.Main_Sequence.WereskagTitleCard.SeqAct_Toggle_1")
        DLC1_Wereskag_starttrigger.OutputLinks[1].Links = [make_new_link(DLC1_Wereskag_end_1, 1), make_new_link(DLC1_Wereskag_end_2)]

class TheMill(Map):
    name = "dlc1_mill_boss_p"

    def on_map_loaded(self):
        #Dr. Ned
        DLC1_DrNed_starttrigger = find_object("Object","dlc1_mill_boss_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionStatusChanged_2")
        DLC1_DrNed_starttrigger.OutputLinks[1].Links.clear()

        #Undead Ned
        DLC1_UndeadNed_starttrigger = find_object("Object","dlc1_mill_boss_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_SetBool_0")
        DLC1_UndeadNed_end_1 = find_object("Object","dlc1_mill_boss_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2")
        DLC1_UndeadNed_end_2 = find_object("Object","dlc1_mill_boss_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ToggleHidden_3")
        DLC1_UndeadNed_starttrigger.OutputLinks[0].Links = [make_new_link(DLC1_UndeadNed_end_1), make_new_link(DLC1_UndeadNed_end_2)]

        #Credits
        Credits_starttrigger = find_object("Object","dlc1_mill_boss_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqAct_CompleteMission_0")
        Credits_starttrigger.OutputLinks[0].Links.clear()

class UnderDome(Map):
    name = "dlc2_lobby_p"

    def on_map_loaded(self):
        #DLC2 Intro
        DLC2_Intro_starttrigger = find_object("Object","dlc2_lobby_p.TheWorld:PersistentLevel.Main_Sequence.SeqCond_CompareBool_2")
        DLC2_Intro_starttrigger.OutputLinks[1].Links.clear()

class TBoneJunction(Map):
    name = "dlc3_HUB_p"

    def on_map_loaded(self):
        #DLC3 Intro
        DLC3_Intro_starttrigger = find_object("Object","dlc3_HUB_p.TheWorld:PersistentLevel.Main_Sequence.Transitions.SeqCond_CompareBool_1")
        DLC3_MeetScooter = find_object("Object","dlc3_HUB_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MeetScooter.SeqAct_ApplyBehavior_0")
        DLC3_Intro_starttrigger.OutputLinks[0].Links.clear()
        DLC3_MeetScooter.InputLinks[0].ActivateDelay = 3

        #Scooter
        Scooter_starttrigger = find_object("Object","dlc3_HUB_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MeetScooter.SeqEvent_Touch_1")
        Scooter_end = find_object("Object","dlc3_HUB_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MeetScooter.SeqAct_ApplyBehavior_3")
        Scooter_starttrigger.OutputLinks[0].Links = [make_new_link(Scooter_end)]

class MoxxisRedLight(Map):
    name = "dlc3_moxxieplace_p"

    def on_map_loaded(self):
        #Moxxi
        Moxxi_starttrigger = find_object("Object","dlc3_moxxieplace_p.TheWorld:PersistentLevel.Main_Sequence.MeetMoxxi.WillowSeqEvent_MissionStatusChanged_1")
        Moxxi_starttrigger.OutputLinks[2].Links.clear()

class LockdownPalace(Map):
    name = "dlc3_prison_p"

    def on_map_loaded(self):
        #Mr. Shank
        MrShank_starttrigger = find_object("Object","dlc3_prison_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MrShankAndEscape.SeqAct_Switch_0")
        MrShank_end = find_object("Object","dlc3_prison_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MrShankAndEscape.SeqAct_Toggle_0")
        MrShank_starttrigger.OutputLinks[0].Links = [make_new_link(MrShank_end)]

        #Athena
        Athena_starttrigger = find_object("Object","dlc3_prison_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MrShankAndEscape.SeqEvent_Used_0")
        Athena_end = find_object("Object","dlc3_prison_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MrShankAndEscape.SeqAct_ApplyBehavior_3")
        Athena_starttrigger.OutputLinks[0].Links = [make_new_link(Athena_end)]

class CrimsonArmory(Map):
    name = "dlc3_lancedepot_p"

    def on_map_loaded(self):
        #General Knoxx
        GeneralKnoxx_starttrigger = find_object("Object","dlc3_lancedepot_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionStatusChanged_0")
        GeneralKnoxx_starttrigger.OutputLinks[1].Links.clear()

        #Credits
        Credits_starttrigger = find_object("Object","dlc3_lancedepot_Dynamic.TheWorld:PersistentLevel.Main_Sequence.GrabLootMissions.SeqAct_ApplyBehavior_17")
        Credits_end_1 = find_object("Object","dlc3_lancedepot_Dynamic.TheWorld:PersistentLevel.Main_Sequence.GrabLootMissions.SeqAct_ActivateRemoteEvent_1")
        Credits_end_2 = find_object("Object","dlc3_lancedepot_Dynamic.TheWorld:PersistentLevel.Main_Sequence.GrabLootMissions.SeqAct_Interp_3")
        Credits_end_3 = find_object("Object","dlc3_lancedepot_Dynamic.TheWorld:PersistentLevel.Main_Sequence.GrabLootMissions.SeqAct_ActivateRemoteEvent_8")
        Credits_end_4 = find_object("Object","dlc3_lancedepot_Dynamic.TheWorld:PersistentLevel.Main_Sequence.GrabLootMissions.SeqAct_UnlockAchievement_1")
        Credits_starttrigger.OutputLinks[0].Links = [make_new_link(Credits_end_1), make_new_link(Credits_end_2), make_new_link(Credits_end_3), make_new_link(Credits_end_4)]

class TartarusStation(Map):
    name = "DLC4_Tartarus_Station_p"

    def on_map_loaded(self):
        #DLC4 Intro
        DLC4_Intro_starttrigger = find_object("Object","DLC4_Tartarus_Station_p.TheWorld:PersistentLevel.Main_Sequence.SeqCond_CompareBool_5")
        DLC4_Intro_starttrigger.OutputLinks[0].Links.clear()

        #Tannis
        Tannis_starttrigger = find_object("Object","DLC4_Tartarus_Station_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionStatusChanged_5")
        Tannis_end = find_object("Object","DLC4_Tartarus_Station_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ToggleHidden_9")
        Tannis_starttrigger.OutputLinks[0].Links = [make_new_link(Tannis_end, 1)]

        #Blake
        Blake_starttrigger = find_object("Object","DLC4_Tartarus_Station_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionStatusChanged_25")
        Blake_end_1 = find_object("Object","DLC4_Tartarus_Station_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ToggleHidden_16")
        Blake_end_2 = find_object("Object","DLC4_Tartarus_Station_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Toggle_4")
        Blake_starttrigger.OutputLinks[1].Links = [make_new_link(Blake_end_1, 1), make_new_link(Blake_end_2, 1)]
        Blake_starttrigger.OutputLinks[2].Links = [make_new_link(Blake_end_1, 1), make_new_link(Blake_end_2, 1)]

        #Marcus
        Marcus_starttrigger = find_object("Object","DLC4_Tartarus_Station_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionStatusChanged_0")
        Marcus_end_1 = find_object("Object","DLC4_Tartarus_Station_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ToggleHidden_14")
        Marcus_end_2 = find_object("Object","DLC4_Tartarus_Station_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Toggle_36")
        Marcus_starttrigger.OutputLinks[0].Links = [make_new_link(Marcus_end_1, 1), make_new_link(Marcus_end_2, 1)]

class HyperionDump(Map):
    name = "DLC4_Hyperion_Dump_p"

    def on_map_loaded(self):
        #SuperBad
        SuperBad_starttrigger = find_object("Object","DLC4_Hyperion_Dump_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionStatusChanged_2")
        SuperBad_starttrigger.OutputLinks[1].Links.clear()

class DividingFaults(Map):
    name = "DLC4_Dividing_Faults_p"

    def on_map_loaded(self):
        #D-Fault
        DFault_starttrigger = find_object("Object","DLC4_Dividing_Faults_p.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_MissionStatusChanged_3")
        DFault_end_1 = find_object("Object","DLC4_Dividing_Faults_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Toggle_0")
        DFault_end_2 = find_object("Object","DLC4_Dividing_Faults_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2")
        DFault_starttrigger.OutputLinks[1].Links = [make_new_link(DFault_end_1), make_new_link(DFault_end_2)]
        DFault_starttrigger.OutputLinks[2].Links = [make_new_link(DFault_end_1), make_new_link(DFault_end_2)]

        #Dr. Ned
        DrNed_starttrigger = find_object("Object","DLC4_Dividing_Faults_p.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_PopulatedActor_5")
        DrNed_end_1 = find_object("Object","DLC4_Dividing_Faults_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_19")
        DrNed_end_2 = find_object("Object","DLC4_Dividing_Faults_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ActivateRemoteEvent_3")
        DrNed_starttrigger.OutputLinks[0].Links = [make_new_link(DrNed_end_1), make_new_link(DrNed_end_2)]

class SandersGorge(Map):
    name = "DLC4_Sanders_Gorge_p"

    def on_map_loaded(self):
        #Knoxx-Trap
        KnoxxTrap_starttrigger = find_object("Object","DLC4_Sanders_Gorge_p.TheWorld:PersistentLevel.Main_Sequence.knoxx_fight.SeqEvent_Touch_2")
        KnoxxTrap_end_1 = find_object("Object","DLC4_Sanders_Gorge_p.TheWorld:PersistentLevel.Main_Sequence.knoxx_fight.SeqAct_ApplyBehavior_1")
        KnoxxTrap_end_2 = find_object("Object","DLC4_Sanders_Gorge_p.TheWorld:PersistentLevel.Main_Sequence.knoxx_fight.SeqAct_Toggle_3")
        KnoxxTrap_end_3 = find_object("Object","DLC4_Sanders_Gorge_p.TheWorld:PersistentLevel.Main_Sequence.knoxx_fight.SeqAct_Toggle_1")
        KnoxxTrap_starttrigger.OutputLinks[0].Links = [make_new_link(KnoxxTrap_end_1), make_new_link(KnoxxTrap_end_2), make_new_link(KnoxxTrap_end_3, 1)]

        #Cluck-Trap
        CluckTrap_starttrigger = find_object("Object","DLC4_Sanders_Gorge_p.TheWorld:PersistentLevel.Main_Sequence.Missions.SeqEvent_Touch_2")
        CluckTrap_end_1 = find_object("Object","DLC4_Sanders_Gorge_p.TheWorld:PersistentLevel.Main_Sequence.Missions.SeqAct_Toggle_3")
        CluckTrap_end_2 = find_object("Object","DLC4_Sanders_Gorge_p.TheWorld:PersistentLevel.Main_Sequence.Missions.SeqAct_Toggle_1")
        CluckTrap_end_3 = find_object("Object","DLC4_Sanders_Gorge_p.TheWorld:PersistentLevel.Main_Sequence.Missions.SeqAct_ActivateRemoteEvent_1")
        CluckTrap_starttrigger.OutputLinks[0].Links = [make_new_link(CluckTrap_end_1), make_new_link(CluckTrap_end_2, 1), make_new_link(CluckTrap_end_3)]

class SSCanyon(Map):
    name = "DLC4_SS_Canyon_p"

    def on_map_loaded(self):
        #Steele-Trap
        SteeleTrap_starttrigger = find_object("Object","DLC4_SS_Canyon_p.TheWorld:PersistentLevel.Main_Sequence.Steele_Fight.New_Steele_Logic.SeqCond_CompareBool_0")
        SteeleTrap_end = find_object("Object","DLC4_SS_Canyon_p.TheWorld:PersistentLevel.Main_Sequence.Steele_Fight.New_Steele_Logic.SeqAct_ActivateRemoteEvent_5")
        SteeleTrap_starttrigger.OutputLinks[1].Links = [make_new_link(SteeleTrap_end)]

class DLC4AridBadlands(Map):
    name = "DLC4_Arid_Badlands_p"

    def on_map_loaded(self):
        #Credits
        Credits_starttrigger = find_object("Object", "DLC4_Arid_Badlands_p.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_Death_0")
        Credits_end_1 = find_object("Object", "DLC4_Arid_Badlands_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Destroy_1")
        Credits_end_2 = find_object("Object", "DLC4_Arid_Badlands_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ActivateRemoteEvent_3")
        Credits_end_3 = find_object("Object", "DLC4_Arid_Badlands_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ToggleHidden_4")
        Credits_end_4 = find_object("Object", "DLC4_Arid_Badlands_p.TheWorld:PersistentLevel.Main_Sequence.SeqAct_PlaySound_15")
        Credits_starttrigger.OutputLinks[0].Links = [make_new_link(Credits_end_1), make_new_link(Credits_end_2), make_new_link(Credits_end_3, 1), make_new_link(Credits_end_4)]