from mods_base import get_pc, ENGINE
from unrealsdk import find_object, make_struct, construct_object, load_package, find_class
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


def add_echocall(object_to_connent_to:str, echo_call_definition:str, sequence:str, output_index:int = 0, delay:float = 0, return_object:bool = False):
    object_to_connent_to = find_object("object", sequence + "." + object_to_connent_to)
    sequence = find_object("Sequence", sequence)
    call_object = construct_object("SeqAct_ApplyBehavior", sequence)
    delay_object = construct_object("SeqAct_Delay", sequence)
    PlayerVar = construct_object("SeqVar_Player", sequence)

    call_behavior = construct_object("PlayerBehavior_PlayEchoCall", call_object)
    call_behavior.CallDef = ENGINE.DynamicLoadObject(echo_call_definition, find_class("EchoCallDefinition"), False)
    call_object.Behaviors.append(call_behavior)
    delay_object.Duration = delay
    call_object.VariableLinks[0].LinkedVariables = [PlayerVar]
    object_to_connent_to.OutputLinks[output_index].Links.append(make_new_link(delay_object))
    delay_object.OutputLinks[0].Links = [make_new_link(call_object)]

    if return_object is True:
        return call_object
    
def add_complete_and_give_mission(object_to_connent_to:str, sequence:str, give_mission:str = "None", complete_mission:str = "None", output_index:int = 0):
    object_to_connent_to = find_object("object", sequence + "." + object_to_connent_to)
    sequence = find_object("Sequence", sequence)
    complete = None
    give = None

    if complete_mission != "None":
        complete = construct_object("WillowSeqAct_CompleteMission", sequence)
        complete.AssociatedMission = ENGINE.DynamicLoadObject(complete_mission, find_class("MissionDefinition"), False)

    if give_mission != "None":
        give = construct_object("WillowSeqAct_GiveMission", sequence)
        give.AssociatedMission = ENGINE.DynamicLoadObject(give_mission, find_class("MissionDefinition"), False)

    if complete is not None:
        object_to_connent_to.Outputlinks[output_index].Links.append(make_new_link(complete))
        if give is not None:
            complete.Outputlinks[0].Links = [make_new_link(give)]
    else:
        object_to_connent_to.Outputlinks[output_index].Links.append(make_new_link(give))




class Map:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Map.registry[cls.name] = cls#type:ignore

    def on_map_loaded(self):
        pass

class AridBadlands(Map):
    name = "arid_p"

    def on_map_loaded(self):
        claptrap_toggle_0 = find_object("object", "Arid_BusStop.TheWorld:PersistentLevel.Main_Sequence.Opening.SeqAct_Toggle_4")
        claptrap_NextStep_0 = find_object("object", "Arid_BusStop.TheWorld:PersistentLevel.Main_Sequence.Opening.Claptrap_Settings_4")
        claptrap_toggle_0.EventLinks.clear()
        claptrap_toggle_0.OutputLinks[0].Links = [make_new_link(claptrap_NextStep_0, 3)]

        claptrap_toggle_1 = find_object("object", "Arid_BusStop.TheWorld:PersistentLevel.Main_Sequence.Opening.SeqAct_Toggle_0")
        claptrap_NextStep_1 = find_object("object", "Arid_BusStop.TheWorld:PersistentLevel.Main_Sequence.Opening.SeqAct_Interp_3")
        claptrap_toggle_1.EventLinks.clear()
        claptrap_toggle_1.OutputLinks[0].Links = [make_new_link(claptrap_NextStep_1)]

        claptrap_toggle_2 = find_object("object", "Arid_BusStop.TheWorld:PersistentLevel.Main_Sequence.Opening.SeqAct_Toggle_6")
        claptrap_NextStep_2 = find_object("object", "Arid_BusStop.TheWorld:PersistentLevel.Main_Sequence.Opening.WillowSeqAct_RunCustomEvent_1")
        claptrap_toggle_2.EventLinks.clear()
        claptrap_toggle_2.OutputLinks[0].Links = [make_new_link(claptrap_NextStep_2)]
    
        claptrap_toggle_3 = find_object("object", "Arid_BusStop.TheWorld:PersistentLevel.Main_Sequence.Opening.SeqAct_Toggle_5")
        claptrap_NextStep_3 = find_object("object", "Arid_BusStop.TheWorld:PersistentLevel.Main_Sequence.Opening.Claptrap_Settings_7")
        claptrap_toggle_3.EventLinks.clear()
        claptrap_toggle_3.OutputLinks[0].Links = [make_new_link(claptrap_NextStep_3, 3)]

        claptrap_toggle_4 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_Toggle_7")
        claptrap_NextStep_4 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.Claptrap_Settings_11")
        claptrap_toggle_4.EventLinks.clear()
        claptrap_toggle_4.OutputLinks[0].Links = [make_new_link(claptrap_NextStep_4, 3)]

        claptrap_toggle_5 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_Toggle_13")
        claptrap_NextStep_5_1 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_Gate_5")
        claptrap_NextStep_5_2 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.Claptrap_Settings_12")
        claptrap_NextStep_5_3 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_AIMoveToActor_6")
        claptrap_toggle_5.EventLinks.clear()
        claptrap_toggle_5.OutputLinks[0].Links = [make_new_link(claptrap_NextStep_5_1, 2)]
        claptrap_toggle_5.OutputLinks[0].Links.append(make_new_link(claptrap_NextStep_5_2, 3))
        claptrap_toggle_5.OutputLinks[0].Links.append(make_new_link(claptrap_NextStep_5_3))

        claptrap_toggle_6 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_Toggle_3")
        claptrap_NextStep_6 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_PlaySound_11")
        claptrap_toggle_6.EventLinks.clear()
        claptrap_NextStep_6.OutputLinks.pop(0)
        claptrap_toggle_6.OutputLinks[0].Links = [make_new_link(claptrap_NextStep_6)]

        claptrap_toggle_7 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_Toggle_11")
        claptrap_NextStep_7_1 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_ToggleHidden_6")
        claptrap_NextStep_7_2 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.Claptrap_Settings_15")
        claptrap_toggle_7.EventLinks.clear()
        claptrap_toggle_7.OutputLinks[0].Links = [make_new_link(claptrap_NextStep_7_1, 1)]
        claptrap_toggle_7.OutputLinks[0].Links.append(make_new_link(claptrap_NextStep_7_2, 3))

        Chest_Training = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_Interp_17")
        Chest_Training.OutputLinks[0].Links.pop(1)

        WayPointTraining_1 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_PrimaryPlayerBusyDelay_5")
        WayPointTraining_2 = find_object("object", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_PrimaryPlayerBusyDelay_4")
        WayPointTraining_1.OutputLinks[0].Links = [make_new_link(WayPointTraining_2)]

        CatchARide = find_object("object", "Arid_P.TheWorld:PersistentLevel.Main_Sequence.Missions.SeqEvent_Touch_10")
        CatchARide.MaxTriggerCount = 0


        #Fix missing collision
        Main_Sequence = find_object("Sequence","arid_p.TheWorld:PersistentLevel.Main_Sequence")
        LevelStart = find_object("SeqEvent_LevelStartup","arid_p.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_LevelStartup_0")
        ApplyBehavior = construct_object("SeqAct_ApplyBehavior", Main_Sequence)
        SetCollision = construct_object("Behavior_ChangeCollision", ApplyBehavior)

        SetCollision.NewCollisionType = 2
        ApplyBehavior.Behaviors.append(SetCollision)

        Wall_0 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_0.ObjValue = find_object("StaticMeshActor","Arid_P.TheWorld:PersistentLevel.StaticMeshActor_2197")

        ApplyBehavior.VariableLinks[0].LinkedVariables = [Wall_0]
        LevelStart.OutputLinks[0].Links.append(make_new_link(ApplyBehavior))

        #Give echo missions automatically
        add_complete_and_give_mission("SeqAct_ApplyBehavior_14", "Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat", "Z0_Missions.Missions.M_RepairClapTrap_02")
        find_object("EchoCallDefinition", "Z0_Echos.VoG.Z0E_WellDone").Mission = None

        Zed_Let_Me_Out = find_object("SeqAct_ApplyBehavior","Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_ApplyBehavior_1")
        Zed_Let_Me_Out_Delay = find_object("SeqAct_Delay","Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat.SeqAct_Delay_0")
        Complete_FreshOffTheBus = construct_object("WillowSeqAct_CompleteMission", find_object("Sequence","Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat"))
        Give_TheDoctorIsIn = construct_object("WillowSeqAct_GiveMission", find_object("Sequence","Arid_Firestone.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Combat"))
        Zed_Let_Me_Out.Outputlinks[0].Links = [make_new_link(Complete_FreshOffTheBus)]
        Complete_FreshOffTheBus.Outputlinks[0].Links = [make_new_link(Give_TheDoctorIsIn)]
        Give_TheDoctorIsIn.Outputlinks[0].Links = [make_new_link(Zed_Let_Me_Out_Delay)]
        Complete_FreshOffTheBus.AssociatedMission = find_object("MissionDefinition", "Z0_Missions.Missions.M_IntroStateSaver")
        Give_TheDoctorIsIn.AssociatedMission = find_object("MissionDefinition", "Z0_Missions.Missions.M_AccessStores")
        find_object("EchoCallDefinition", "Z0_Echos.Zed.Z0E_LetMeOut").Mission = None
        find_object("EchoCallDefinition", "Z0_Echos.Zed.Z0E_LetMeOut").MissionToComplete = None


class HeadStoneMines(Map):
    name = "Arid_Mine_P"

    def on_map_loaded(self):
        add_echocall("SeqAct_ApplyBehavior_0", "Z0_Echos.Flynt.Z0E_KilledMyMan", "Arid_Mine_P.TheWorld:PersistentLevel.Main_Sequence.Echos", 0, 38)

class KromsCanyon(Map):
    name = "Scrap_Canyon_P"

    def on_map_loaded(self):
        add_echocall("SeqAct_ApplyBehavior_1", "Z1_Echos.Flynt.Z1E_YouMustBePunished", "Scrap_Canyon_P.TheWorld:PersistentLevel.Main_Sequence.Echos")

class RustCommonsWest(Map):
    name = "scrap_p"

    def on_map_loaded(self):
        tannis = find_object("WillowInteractiveNPC","scrap_p.TheWorld:PersistentLevel.WillowInteractiveNPC_7")
        NAR_Echo_Tannis_83Cue = ENGINE.DynamicLoadObject("VO_Narrative.Tannis.NAR_Echo_Tannis_83Cue", find_class("SoundCue"), False)
        NAR_Echo_Tannis_83Cue.VolumeMultiplier = 2
        tannis.MissionBeats.append(make_struct("MissionBeatData", BeatMission=ENGINE.DynamicLoadObject("Z2_Missions.Missions.M_ReturnKey", find_class("MissionDefinition"), False), BeatSound=NAR_Echo_Tannis_83Cue))

class RustCommonsEast(Map):
    name = "Trash_p"

    def on_map_loaded(self):
        add_echocall("WillowSeqEvent_MissionStatusChanged_2", "Z1_Echos.Flynt.Z1E_Taunt_01", "Trash_p.TheWorld:PersistentLevel.Main_Sequence.Echos", 3)

        #Give Another Piece Of The Puzzle automatically
        add_complete_and_give_mission("SeqAct_ApplyBehavior_3", "Trash_p.TheWorld:PersistentLevel.Main_Sequence.TransitionClaptrap", "Z1_Missions.Missions.M_AnotherLittleSuprise", "Z1_Missions.Missions.M_JaynisCleaningUp")
        find_object("EchoCallDefinition", "Z1_Echos.VoG.Z1E_AnotherSurprise").Mission = None
        find_object("EchoCallDefinition", "Z1_Echos.VoG.Z1E_AnotherSurprise").MissionToComplete = None



class TrashCoast(Map):
    name = "scrap_trashcoast_p"

    def on_map_loaded(self):
        add_echocall("SeqAct_ApplyBehavior_0", "Z1_Echos.Steele.Z1E_WhatAreYouUpToNow", "scrap_trashcoast_p.TheWorld:PersistentLevel.Main_Sequence.Echos", 0, 20)
        find_object("WillowAIPawn","Scrap_TrashCoast_P.TheWorld:PersistentLevel.WillowAIPawn_0").ActorSpawnCost = 0
        find_object("object","scrap_trashcoast_p.TheWorld:PersistentLevel.Main_Sequence.Echos.WillowSeqEvent_MissionStatusChanged_0").Outputlinks[1].ActivateDelay = 27

        rock_pile_02_fixed = ENGINE.DynamicLoadObject("MapTweaks.Mesh.rock_pile_02", find_class("StaticMesh"), False)
        
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_2454").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1387").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1566").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1491").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1511").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1442").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_782").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1444").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1421").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1459").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1460").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_835").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1694").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1361").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1390").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1391").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1462").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1330").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_930").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1464").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1297").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1615").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_949").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1290").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_730").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_731").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_732").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_962").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_687").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1820").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1635").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1636").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_2010").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_135").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1108").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1654").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_134").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_2011").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1019").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1791").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_552").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1799").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_976").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1804").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1808").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1895").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1821").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1824").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1825").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1822").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1823").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_72").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1862").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1867").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_613").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1789").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1662").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1913").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1790").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_126").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1826").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1695").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1671").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1702").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1833").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1912").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1835").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1841").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1834").StaticMeshComponent.StaticMesh = rock_pile_02_fixed
        find_object("StaticMeshActor","Scrap_TrashCoast_P.TheWorld:PersistentLevel.StaticMeshActor_1836").StaticMeshComponent.StaticMesh = rock_pile_02_fixed

class OldHaven(Map):
    name = "Scrap_OldHaven_P"

    def on_map_loaded(self):
        flareout = find_object("FlareOut","scrap_oldhaven_light.TheWorld:PersistentLevel.FlareOut_0")
        flareout.FlareTexture = ENGINE.DynamicLoadObject("fx_textures_general.Textures.Bullet_Impacts.tex_blueStar", find_class("Texture2D"), False)

class SaltFlats(Map):
    name = "Interlude_2_P"

    def on_map_loaded(self):
        #Restore cut audio
        final_artifact_mission_kismet = find_object("Object","Interlude_2_P.TheWorld:PersistentLevel.Main_Sequence.Echos.WillowSeqEvent_MissionStatusChanged_2")
        cut_vog = find_object("Object","Interlude_2_P.TheWorld:PersistentLevel.Main_Sequence.Echos.SeqAct_ApplyBehavior_12")
        final_artifact_mission_kismet.Outputlinks[3].Links = [make_new_link(cut_vog)]

        #Give Find Steele automatically
        add_complete_and_give_mission("SeqAct_ApplyBehavior_17", "Interlude_2_P.TheWorld:PersistentLevel.Main_Sequence.Echos", "Z2_Missions.Missions.M_FindSteele")
        find_object("EchoCallDefinition", "Z1_Echos.Tannis.Z1E_WhoBetrayedWhom").Mission = None

class DahlHeadlands(Map):
    name = "interlude_1_p"

    def on_map_loaded(self):
        #Fix missing collision
        Main_Sequence = find_object("Sequence","interlude_1_p.TheWorld:PersistentLevel.Main_Sequence")
        LevelStart = find_object("SeqEvent_LevelStartup","interlude_1_p.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_LevelStartup_1")
        ApplyBehavior = construct_object("SeqAct_ApplyBehavior", Main_Sequence)
        SetCollision = construct_object("Behavior_ChangeCollision", ApplyBehavior)

        SetCollision.NewCollisionType = 2
        ApplyBehavior.Behaviors.append(SetCollision)

        Wall_0 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_0.ObjValue = find_object("StaticMeshActor","Interlude_1_Env.TheWorld:PersistentLevel.StaticMeshActor_1570")
        Wall_1 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_1.ObjValue = find_object("StaticMeshActor","Interlude_1_Env.TheWorld:PersistentLevel.StaticMeshActor_194")

        ApplyBehavior.VariableLinks[0].LinkedVariables = [Wall_0, Wall_1]

        LevelStart.OutputLinks[0].Links.append(make_new_link(ApplyBehavior))

class CrimsonFastness(Map):
    name = "Waste_CrimsonBunker_P"

    def on_map_loaded(self):
        add_complete_and_give_mission("SeqAct_ApplyBehavior_2", "Waste_CrimsonBunker_P.TheWorld:PersistentLevel.Main_Sequence.Echos", "Z2_Missions.Missions.M_FindSteele")
        find_object("EchoCallDefinition", "Z1_Echos.Tannis.Z1E_WhoBetrayedWhom").Mission = None


class Descent(Map):
    name = "Waste_Descent_P"

    def on_map_loaded(self):
        add_echocall("SeqAct_ApplyBehavior_0", "Z2_Echos.Tannis.Z2E_BewareGuardians", "Waste_Descent_P.TheWorld:PersistentLevel.Main_Sequence.echo", delay = 11)

class TheMill(Map):
    name = "dlc1_mill_boss_p"

    def on_map_loaded(self):
        find_object("bodyclassdefinition","dlc1_gd_NedEnemy.Character.BodyClass_NedEnemy").BodySkins.clear()

class JakobsCove(Map):
    name = "dlc1_island_p"

    def on_map_loaded(self):
        #Fix drop pod material
        drop_pod = find_object("StaticMeshComponent", "dlc1_island_p.TheWorld:PersistentLevel.InterpActor_18.StaticMeshComponent_65")
        drop_pod.Materials.append(ENGINE.DynamicLoadObject("dlc1_props.drop_pod.drop_pod_matdrop_pod_interior_mat", find_class("Material"), False))
        drop_pod.Materials.append(ENGINE.DynamicLoadObject("dlc1_props.drop_pod.drop_pod_matdrop_pod_interior_mat_INST", find_class("MaterialInstanceConstant"), False))

        #Remove the invisible wall stopping you from continuing while claptrap talks
        defendtown_status_changed = find_object("Object","dlc1_island_p.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Setup_Based_On_Missions.WillowSeqEvent_MissionStatusChanged_1")
        remove_collision = find_object("Object","dlc1_island_p.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Setup_Based_On_Missions.SeqAct_ChangeCollision_0")
        defendtown_status_changed.Outputlinks[0].Links.append(make_new_link(remove_collision))

class RoadsEnd(Map):
    name = "dlc3_gondola_p"

    def on_map_loaded(self):
        #Fix missing collision
        Main_Sequence = find_object("Sequence","dlc3_gondola_p.TheWorld:PersistentLevel.Main_Sequence.Transitions")
        LevelStart = find_object("SeqEvent_LevelLoaded","dlc3_gondola_p.TheWorld:PersistentLevel.Main_Sequence.Transitions.SeqEvent_LevelLoaded_0")
        ApplyBehavior = construct_object("SeqAct_ApplyBehavior", Main_Sequence)
        SetCollision = construct_object("Behavior_ChangeCollision", ApplyBehavior)

        SetCollision.NewCollisionType = 2
        ApplyBehavior.Behaviors.append(SetCollision)

        Wall_0 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_0.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_3770")
        Wall_1 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_1.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_417")
        Wall_2 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_2.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_3875")
        Wall_3 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_3.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_4599")
        Wall_4 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_4.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_242")
        Wall_5 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_5.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_3730")
        Wall_6 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_6.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_250")
        Wall_7 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_7.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_4297")
        Wall_8 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_8.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_255")
        Wall_9 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_9.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_2598")
        Wall_10 = construct_object("SeqVar_Object", Main_Sequence)
        Wall_10.ObjValue = find_object("StaticMeshActor","dlc3_gondola_p.TheWorld:PersistentLevel.StaticMeshActor_1139")


        ApplyBehavior.VariableLinks[0].LinkedVariables = [Wall_0, Wall_1, Wall_2, Wall_3, Wall_4, Wall_5, Wall_6, Wall_7, Wall_8, Wall_9, Wall_10]

        LevelStart.OutputLinks[0].Links.append(make_new_link(ApplyBehavior))

class SLanceStrip(Map):
    name = "dlc3_SLanceStrip_p"

    def on_map_loaded(self):
        SRoadBlockTurnIn = find_object("WillowInteractiveObject","dlc3_SLanceStrip_dynamic.TheWorld:PersistentLevel.WillowInteractiveObject_11")
        SRoadBlockTurnIn.MissionDirectives.clear()
        SRoadBlockTurnIn.InteractiveObjectDefinition = None

        add_complete_and_give_mission("SeqAct_Interp_0", "dlc3_SLanceStrip_dynamic.TheWorld:PersistentLevel.Main_Sequence.RoadBlocks1", "dlc3_MainMissions.MainMissions.M_dlc3_MeetMoxxi", "dlc3_MainMissions.MainMissions.M_dlc3_Roadblocks1")

class NLanceStrip(Map):
    name = "dlc3_NLanceStrip_p"

    def on_map_loaded(self):
        NRoadBlockTurnIn = find_object("WillowInteractiveObject","dlc3_NLanceStrip_dynamic.TheWorld:PersistentLevel.WillowInteractiveObject_52")
        NRoadBlockTurnIn.MissionDirectives.clear()
        NRoadBlockTurnIn.InteractiveObjectDefinition = None

        add_complete_and_give_mission("SeqAct_Interp_0", "dlc3_NLanceStrip_dynamic.TheWorld:PersistentLevel.Main_Sequence.RoadBlocks2", "dlc3_MainMissions.MainMissions.M_dlc3_PrisonInfiltrate", "dlc3_MainMissions.MainMissions.M_dlc3_Roadblocks2")

class SunkenSea(Map):
    name = "dlc3_lakebed_p"

    def on_map_loaded(self):
        find_object("object","dlc3_lakebed_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dry_Well.SeqEvent_Touch_1").MaxTriggerCount = 0

class LockdownPalace(Map):
    name = "dlc3_prison_p"

    def on_map_loaded(self):
        #Auto complete mission
        old_turn_in = find_object("WillowInteractiveObject","dlc3_prison_Dynamic.TheWorld:PersistentLevel.WillowInteractiveObject_153")
        old_turn_in.MissionDirectives.clear()
        old_turn_in.InteractiveObjectDefinition = None

        add_complete_and_give_mission("SeqAct_Interp_1", "dlc3_prison_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MrShankAndEscape", "dlc3_MainMissions.MainMissions.M_dlc3_MeetInformant", "dlc3_MainMissions.MainMissions.M_dlc3_PrisonMrShank")

class DeepFathoms(Map):
    name = "dlc3_southlake_p"

    def on_map_loaded(self):
        #Auto complete mission
        old_turn_in = find_object("WillowInteractiveObject", "dlc3_SOUTHLAKE_dynamic.TheWorld:PersistentLevel.WillowInteractiveObject_1")
        old_turn_in.MissionDirectives.clear()
        old_turn_in.InteractiveObjectDefinition = None

        add_complete_and_give_mission("SeqAct_ActivateRemoteEvent_0", "dlc3_SOUTHLAKE_dynamic.TheWorld:PersistentLevel.Main_Sequence.ACtivateBridge", "dlc3_MainMissions.MainMissions.M_dlc3_DestroyDepot", "dlc3_MainMissions.MainMissions.M_dlc3_ActivateBridge")
