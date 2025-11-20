import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type, remove_hook, add_hook
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, WrappedArray
from mods_base import hook, get_pc, ENGINE, SETTINGS_DIR, build_mod, command
from unrealsdk import logging
from unrealsdk.commands import has_command, add_command, remove_command
import re
import ast


def load_obj(object: str, definition: str = "object"):
    try:
        result = unrealsdk.find_object(definition, object)
        return result
    except:
        object_class = unrealsdk.find_class(definition)
        return ENGINE.DynamicLoadObject(object, object_class, False)


def format_load_obj(object_to_load: str):
    return load_obj(object_to_load.split("'")[1].strip(), object_to_load.split("'")[0].strip())


def clone_object(base, clone):
    base = load_obj(base)
    new_base = re.findall("^(.*)[.:]", clone)[0]
    name = re.findall("[:.]([\\w\\d]*)$", clone)[0]
    unrealsdk.construct_object(base.Class, load_obj(new_base), name=name, template_obj=base)


def object_list(string_list):
    list = []

    string_list = string_list.strip("()")
    for i in string_list.split(","):
        list.append(format_load_obj(i))

    return list


def array_to_dict(input_array: str):

    def _find_matching_paren(s, i, braces=None):  # By ggorlen on Stack Overflow https://stackoverflow.com/questions/63382152/find-the-matching-opening-closing-brace-index-in-a-string
        openers = braces or {"(": ")"}
        closers = {v: k for k, v in openers.items()}
        stack = []
        result = []

        if s[i] not in openers:
            raise ValueError(f"char at index {i} was not an opening brace")

        for ii in range(i, len(s)):
            c = s[ii]

            if c in openers:
                stack.append([c, ii])
            elif c in closers:
                if not stack:
                    raise ValueError(f"tried to close brace without an open at position {i}")

                pair, idx = stack.pop()

                if pair != closers[c]:
                    raise ValueError(f"mismatched brace at position {i}")

                if idx == i:
                    return ii

        if stack:
            raise ValueError(f"no closing brace at position {i}")

        return result

    def _array_to_dict(input_array):

        while input_array.startswith("(("):
            input_array = input_array[1:-1]

        pattern = r"\b([A-Za-z_]+)'([\w\.:]+)'"
        replacement = '"' + r"\1'\2'" + '"'

        pattern2 = r"(\w+)="
        replacement2 = r'"\1":'

        pattern3 = """((?<=:)(?![ '("])[^",}]*?(?=[,)}\\n]))"""
        replacement3 = r'"\1"'

        input_array = re.sub(pattern, replacement, input_array)
        input_array = re.sub(pattern2, replacement2, input_array)
        input_array = re.sub(pattern3, replacement3, input_array)
        input_array = input_array.replace("(", "{").replace(")", "}")

        if input_array.find(":{{") > -1:
            pos = -1
            while True:
                pos = input_array.find(":{{", pos + 1)
                if pos == -1:
                    break

                matching_bracket = _find_matching_paren(input_array, pos + 1, {"{": "}"})

                input_array = (input_array[: matching_bracket + 0] + "]" + input_array[matching_bracket + 1:])

                input_array = (input_array[: pos + 1] + "[" + input_array[pos + 2:])  # Put nested items in a list

        if len(re.findall(r"\{([^:{}]+)\}", input_array)) > 0:

            tuple_found = re.findall(
                r"\{([^:{}]+)\}", input_array)[0].split(",")
            tuple_replacement = []
            for i in tuple_found:
                tuple_replacement.append(i.strip())
            input_array = re.sub(
                r"\{([^:{}]+)\}", f"({tuple_replacement})", input_array
            )

        result = ast.literal_eval(input_array)
        if type(result) == dict:
            result = (result,)
        return result

    return _array_to_dict(input_array)


def string_to_tuple(input: str):
    result = []
    if type(input) is str:
        for i in input.strip("()").split(","):
            result.append(i.strip())
    elif type(input) is list:
        for i in input:
            result.append(i.strip())
    return tuple(result)


def set_value(base, property, value):
    property_type = type(getattr(base, property))

    if property_type is int:
        setattr(base, property, int(value))

    elif property_type is float:
        setattr(base, property, float(value))

    elif property_type is str:
        setattr(base, property, value)

    elif property_type is bool:
        setattr(base, property, value == "True")

    elif str(property_type) in "<class 'unrealsdk.unreal.UClass'>":
        setattr(base, property, unrealsdk.find_class(value.strip('"')))

    elif property_type is tuple:

        new_tuple = []
        index = -1
        for i in string_to_tuple(value):
            index += 1
            property_type = type(getattr(base, property)[index])

            if str(getattr(base, property)[index].__class__.__class__) == "<class 'enum.EnumType'>":
                new_tuple.append(getattr(base, property)[index]._member_map_.get(i))

            elif property_type is UObject or property_type is type(None):
                if i == "None":
                    new_tuple.append(None)
                else:
                    new_tuple.append(format_load_obj(i))

            elif property_type is int:
                new_tuple.append(int(i))

            elif property_type is float:
                new_tuple.append(float(i))

            elif property_type is bool:
                new_tuple.append(bool(i))

            elif property_type is str:
                new_tuple.append(i)

        setattr(base, property, tuple(new_tuple))

    elif property_type is UObject or property_type is type(None):

        if value == "None":
            setattr(base, property, None)
        else:
            setattr(base, property, format_load_obj(value))

    elif str(getattr(base, property).__class__.__class__) == "<class 'enum.EnumType'>":
        enum_int = getattr(base, property)._member_map_.get(value)
        setattr(base, property, enum_int)

    else:
        print("Text Mod Error: set_value error: Unkown property type", property_type)


def set_array_value(array, dict):

    for k, v in dict.items():
        k = k.strip(",")

        property_type = type(getattr(array, k))

        if property_type is WrappedStruct:
            set_array_value(getattr(array, k), v)

        elif property_type is WrappedArray:

            getattr(array, k).clear()
            if type(v) is list:
                for i in v:

                    getattr(array, k).emplace_struct()
                    index = len(getattr(array, k)) - 1
                    set_array_value(getattr(array, k)[index], i)

            elif type(v) is set:
                for i in v:
                    getattr(array, k).append(format_load_obj(i))

        else:
            set_value(array, k, v)


def custom_set(object_name, object_property, value):

    object_found = load_obj(object_name)

    if object_found is None:
        print("Text Mod Error:", object_name, "not found")
        return

    property_type = type(getattr(object_found, object_property))

    if property_type is WrappedArray:

        if (
            str(getattr(object_found, object_property)._type).split("'")[0]
            in "ObjectProperty"
        ):
            if value == "()":
                setattr(object_found, object_property, [])
            else:
                setattr(object_found, object_property, object_list(value))

        else:

            getattr(object_found, object_property).clear()
            for i in array_to_dict(value):

                getattr(object_found, object_property).emplace_struct()
                index = len(getattr(object_found, object_property)) - 1
                set_array_value(
                    getattr(object_found, object_property)[index], i)

    elif property_type is WrappedStruct:

        if type(getattr(object_found, object_property)) == tuple:

            index = 0
            for i in array_to_dict(value):
                print("Tuple", i)
                index += 1

                set_array_value(
                    getattr(object_found, object_property)[index - 1], i)

            return

        for i in array_to_dict(value):

            set_array_value(getattr(object_found, object_property), i)

    else:
        set_value(object_found, object_property, value)
