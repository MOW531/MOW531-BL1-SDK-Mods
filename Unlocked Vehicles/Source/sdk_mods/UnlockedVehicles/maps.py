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


def fix_vehicles():
    dlc3_VSSMovieDefinition = ENGINE.DynamicLoadObject("dlc3_gd_vehiclespawnstation.Definitions.dlc3_VSSMovieDefinition", find_class("VehicleSpawnStationGFxDefinition"), False)
    base_VSSMovieDefinition = ENGINE.DynamicLoadObject("ui_vehicle_spawn_station.Definitions.VSSMovieDefinition", find_class("VehicleSpawnStationGFxDefinition"), False)
    new_material_list = base_VSSMovieDefinition.VehicleMaterials + dlc3_VSSMovieDefinition.VehicleMaterials
    new_vehicle_list = base_VSSMovieDefinition.VehicleTypes + dlc3_VSSMovieDefinition.VehicleTypes
    base_VSSMovieDefinition.VehicleMaterials = new_material_list
    dlc3_VSSMovieDefinition.VehicleMaterials = new_material_list
    base_VSSMovieDefinition.VehicleTypes = new_vehicle_list
    dlc3_VSSMovieDefinition.VehicleTypes = new_vehicle_list
    find_object("VehicleSpawnStationVehicleDefinition","dlc3_gd_vehiclespawnstation.Definitions.VSSVehicle_ChetaPaw").VehicleMaterialBankIndex = 1
    find_object("VehicleSpawnStationVehicleDefinition","dlc3_gd_vehiclespawnstation.Definitions.VSSVehicle_Racer").VehicleMaterialBankIndex = 2
    find_object("VehicleSpawnStationVehicleDefinition","dlc3_gd_vehiclespawnstation.Definitions.VSSVehicle_Lancer").VehicleMaterialBankIndex = 3
    find_object("VehicleSpawnStationVehicleDefinition","dlc3_gd_vehiclespawnstation.Definitions.VSSVehicle_ChetaPaw").VehicleUnlockClientFlag = "MonsterUnlocked"

def add_script(sequence:str, event_trigger:str, index:int = 0):
        event_trigger = find_object("object", sequence + "." + event_trigger)
        sequence = find_object("Sequence", sequence)

        unlock_monster = construct_object("WillowSeqAct_ClientFlagSet", sequence)
        unlock_monster.ClientFlagName = "MonsterUnlocked"

        unlock_racer = construct_object("WillowSeqAct_ClientFlagSet", sequence)
        unlock_racer.ClientFlagName = "RacerUnlocked"

        unlock_lancer = construct_object("WillowSeqAct_ClientFlagSet", sequence)
        unlock_lancer.ClientFlagName = "LancerUnlocked"

        if get_mission_status("dlc3_MainMissions.MainMissions.M_dlc3_BuildCar") == 4:
            event_trigger.Outputlinks[index].Links.append(make_new_link(unlock_monster))

        if get_mission_status("dlc3_MainMissions.MainMissions.M_dlc3_MeetMoxxi") == 4:
            event_trigger.Outputlinks[index].Links.append(make_new_link(unlock_racer))

        if get_mission_status("dlc3_SideMissions.SideMissions.M_dlc3_Digistruct") == 4:
            event_trigger.Outputlinks[index].Links.append(make_new_link(unlock_lancer))



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
        fix_vehicles()
        add_script("arid_p.TheWorld:PersistentLevel.Main_Sequence", "SeqEvent_LevelStartup_0")

class DahlHeadlands(Map):
    name = "interlude_1_p"

    def on_map_loaded(self):        
        fix_vehicles()
        add_script("interlude_1_p.TheWorld:PersistentLevel.Main_Sequence", "SeqEvent_LevelStartup_1")

class NewHaven(Map):
    name = "scrap_newhaven_p"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("scrap_newhaven_p.TheWorld:PersistentLevel.Main_Sequence", "SeqEvent_LevelStartup_0")

class RustCommonsWest(Map):
    name = "scrap_p"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("Scrap_p.TheWorld:PersistentLevel.Main_Sequence", "SeqEvent_LevelStartup_0")

class RustCommonsEast(Map):
    name = "Trash_p"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("Trash_p.TheWorld:PersistentLevel.Main_Sequence", "SeqEvent_LevelStartup_0")

class SaltFlats(Map):
    name = "Interlude_2_P"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("Interlude_2_P.TheWorld:PersistentLevel.Main_Sequence", "SeqEvent_LevelStartup_0")

class TBoneJunction(Map):
    name = "dlc3_HUB_p"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("dlc3_HUB_p.TheWorld:PersistentLevel.Main_Sequence.Transitions", "SeqEvent_LevelLoaded_0")
        buildcar_status_changed = find_object("object","dlc3_HUB_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BuildVehicle.WillowSeqEvent_MissionStatusChanged_5")
        unlock_monster = construct_object("WillowSeqAct_ClientFlagSet", find_object("Sequence","dlc3_HUB_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BuildVehicle"))
        unlock_monster.ClientFlagName = "MonsterUnlocked"
        buildcar_status_changed.Outputlinks[2].Links.append(make_new_link(unlock_monster))
        buildcar_status_changed.Outputlinks[3].Links.append(make_new_link(unlock_monster))

class TheRidgeway(Map):
    name = "dlc3_NLanceStrip_p"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("dlc3_NLanceStrip_p.TheWorld:PersistentLevel.Main_Sequence", "SeqEvent_LevelLoaded_0")

class DeepFathoms(Map):
    name = "dlc3_southlake_p"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("dlc3_southlake_p.TheWorld:PersistentLevel.Main_Sequence.Transitions", "SeqEvent_LevelStartup_0")

class RoadsEnd(Map):
    name = "dlc3_gondola_p"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("dlc3_gondola_p.TheWorld:PersistentLevel.Main_Sequence.Transitions", "SeqEvent_LevelStartup_0")

class CrimsonTollway(Map):
    name = "dlc3_SLanceStrip_p"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("dlc3_SLanceStrip_p.TheWorld:PersistentLevel.Main_Sequence", "SeqEvent_LevelLoaded_0")

class SunkenSea(Map):
    name = "dlc3_lakebed_p"

    def on_map_loaded(self):
        fix_vehicles()
        add_script("dlc3_lakebed_p.TheWorld:PersistentLevel.Main_Sequence.Transitions", "SeqEvent_LevelStartup_0")
