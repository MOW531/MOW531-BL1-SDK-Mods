import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type, remove_hook, add_hook
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, WrappedArray
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, command
from unrealsdk import logging
from unrealsdk.commands import has_command, add_command, remove_command

import re

from .functions import custom_set, clone_object, load_obj

bPatched = False

hotfix_clone_commands = []
hotfixes = {}

any_dlc1 = ['dlc1_island_p', 'dlc1_mill_boss_p', 'dlc1_mill_p', 'dlc1_monsterhouse_p', 'dlc1_swamp_ned_p', 'dlc1_zombiehaven_p']
any_dlc2 = ['dlc2_gully_p', 'dlc2_hellburb_p', 'dlc2_lobby_p', 'dlc2_ruins_p']
any_dlc3 = ['dlc3_uberboss_p', 'dlc3_circle_p', 'dlc3_gondola_p', 'dlc3_hub_p', 'dlc3_lakebed_p', 'dlc3_lancedepot_p', 'dlc3_nlancestrip_p', 'dlc3_prison_p', 'dlc3_slancestrip_p', 'dlc3_southlake_p']
any_dlc4 = ['dlc4_arid_badlands_p', 'dlc4_dividing_faults_p', 'dlc4_hyperion_dump_p', 'dlc4_sanders_gorge_p', 'dlc4_ss_canyon_p', 'dlc4_tartarus_station_p', 'dlc4_wayward_pass_p']


def FinalizedMapChange(obj: UObject, args: WrappedStruct, ret: any, func: BoundFunction) -> any:
    global hotfix_clone_commands
    global hotfixes
    map_name = args.NextMapName

    for command in hotfix_clone_commands:
        clone_object(command[0], command[1])

    for command, map in hotfixes.items():
        if map.lower() == map_name.lower() or map.lower() == "any" or map.lower() == "any_dlc1" and map.lower() in any_dlc1 or map.lower() == "any_dlc2" and map.lower() in any_dlc2 or map.lower() == "any_dlc3" and map.lower() in any_dlc3 or map.lower() == "any_dlc4" and map.lower() in any_dlc4:
            command = command.split(maxsplit=3)
            object_name = command[1]
            object_property = command[2]
            value = command[3]
            custom_set(object_name, object_property, value)


def process_custom_commands(line: str):
    global hotfix_clone_commands
    if line.startswith("clone"):
        if line.endswith("hotfix"):
            hotfix_clone_commands.append([line.split()[1], line.split()[2]])
        else:
            clone_object(line.split()[1], line.split()[2])


def process_set_command(line, cmd_len):
    global hotfixes
    # index = -1
    command = line.split(maxsplit=3)
    object_name = command[1]
    object_property = command[2].split("[")[0]
    value = command[3]
    # if command[2].endswith("]"):
    #    index = int(command[2].split("[")[1][:-1])

    if object_name == "Transient.GearboxAccountData_1" or object_name == "Transient.SparkServiceConfiguration_0":
        if object_property == "Values":

            BL1_commands = eval(value)[23:]
            for i in BL1_commands:
                command = str(i).split(",", maxsplit=4)
                result = "set " + str(command[2]) + " " + str(command[3]) + " " + str(command[4])
                hotfixes[result] = str(command[1])
        return

    custom_set(object_name, object_property, value)


def custom_exec(file_path, cmd_len=0):
    file_path = file_path[4:].strip()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("set "):
                    process_set_command(line.strip(), len(line.strip()))

                # and line.strip().endswith("</comment>"):
                elif line.strip().startswith("<comment>"):
                    process_custom_commands(line.strip()[9:-10])

    except FileNotFoundError:

        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:

        print(f"An error occurred: {e}")


def make_set_command(property_value: str, type: str):
    replacement_table = str.maketrans({"{": "(", "}": ")"})

    property_value = property_value.translate(replacement_table)

    property_value = property_value.replace("[(", "((").replace(")]", "))").replace(": ", "= ")
    
    property_value = re.sub(" '([\\s\\S]*?)'([\\s\\S]?)", r' "\1"\2', property_value)

    for i in re.findall("(<[\\w]*.[\\w]*= [\\d]>)", property_value):
        replacement = i.split(".")[1].split()[0].strip("=")
        property_value = property_value.replace(i, replacement, 1)

    if type == "WrappedArray" and property_value.startswith("((") is False:
        property_value = ("(" + property_value + ")")

    if type == "ObjectList":
        property_value = property_value.replace("[", "(").replace("]", ")")

    property_value = property_value.replace("[]", "()")

    return_value = property_value
    return return_value


def dump_property(line, cmd_len):
    object = load_obj(line.split()[1])
    property = line.split()[2]
    value = getattr(object, property)

    if type(value) is WrappedArray:
        if str(value._type).split("'")[0] in "ObjectProperty":
            value = make_set_command(str(value), "ObjectList")

        else:
            value = make_set_command(str(value), "WrappedArray")

    elif type(value) is WrappedStruct:
        value = make_set_command(str(value), "WrappedStruct")

    with open('dump property output.txt', 'w') as f:
        print("set", str(object).split("'")[1].strip(), property, str(value), file=f)


@hook(
    hook_func="Engine.WorldInfo:IsMenuLevel",
    hook_type=Type.PRE,
)
def Auto_Patcher(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched
    if bPatched is False:
        bPatched = True
        custom_exec("exec patch.txt")
        print("Patch.txt executed")


remove_command("set")
add_command("set", process_set_command)

remove_command("exec")
add_command("exec", custom_exec)

remove_command("dump_prop")
add_command("dump_prop", dump_property)


remove_hook("WillowGame.WillowGameInfo:PreCommitMapChange", Type.POST, "PreCommitMapChange")
add_hook("WillowGame.WillowGameInfo:PreCommitMapChange", Type.POST, "PreCommitMapChange", FinalizedMapChange)


build_mod()
