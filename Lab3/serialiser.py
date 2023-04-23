import inspect
import re
import types

from constants import BASE_TYPES, SIMILAR_COLLECTIONS, CODE_PROPERTIES, BASE_COLLECTIONS


def serialize(obj):
    # Serialising of base types
    if isinstance(obj, tuple(BASE_TYPES.values())):
        return serialize_base_types(obj)

    # Serializing none-type
    elif not obj:
        return serialize_none_type

    # Serializing list, tuple, frozenset, set, bytes, bytearray
    elif isinstance(obj, tuple(SIMILAR_COLLECTIONS.values())):
        return serialize_similar_collections(obj)

    # Serializing dict
    elif isinstance(obj, dict):
        return serialize_dict(obj)

    elif inspect.isfunction(obj):
        return serialize_function(obj)


def get_obj_type(obj):
    return re.search(r"\'(\w+)\'", str(type(obj)))[1]


def serialize_base_types(obj):
    srz = dict()

    srz["type"] = get_obj_type(obj)
    srz["value"] = obj
    return srz


def serialize_similar_collections(obj):
    srz = dict()

    srz["type"] = get_obj_type(obj)
    srz["value"] = [serialize(item) for item in obj]
    return srz


def serialize_none_type():
    srz = dict()

    srz["type"] = "NoneType"
    srz["value"] = None
    return srz


def serialize_dict(obj):
    srz = dict()

    srz["type"] = get_obj_type(obj)
    srz["value"] = [[serialize(key), serialize(value)] for (key, value) in obj.items()]
    return srz


def serialize_function(obj):
    srz = dict()
    srz["type"] = "function"

    srz["value"] = full_function_serialize(obj)


def full_function_serialize(obj):
    value = dict()

    value["__name__"] = obj.__name__
    value["__globals__"] = get_globals(obj)

    arguments = {key: serialize(value) for key, value in inspect.getmembers(serialize_function.__code__)
                 if key in CODE_PROPERTIES}

    value["__code__"] = arguments

    return value


def get_globals(obj):
    glo_balls = dict()

    for glo_ball_variable in obj.__code__.co_names:

        if glo_ball_variable in obj.__globals__:

            if isinstance(obj.__globals__[glo_ball_variable], types.ModuleType):
                glo_balls[glo_ball_variable] = serialize(obj.__globals__[glo_ball_variable].__name__)

            elif glo_ball_variable != obj.__code__.co_name:
                glo_balls[glo_ball_variable] = serialize(obj.__globals__[glo_ball_variable])

            else:
                glo_balls[glo_ball_variable] = serialize(obj.__name__)

    return glo_balls


def deserialize(obj):
    if obj["type"] in str(BASE_TYPES):
        return deserialize_base_type(obj)

    elif obj["type"] in str(BASE_COLLECTIONS):
        return deserialize_base_collections(obj)


def deserialize_base_type(obj):
    return BASE_TYPES[obj["type"]](obj["value"])


def deserialize_base_collections(obj):
    # Getting type of collection
    collection_type = obj["type"]

    if collection_type in SIMILAR_COLLECTIONS.keys():
        # type cast to certain collection from deserialized objects
        return SIMILAR_COLLECTIONS[collection_type](deserialize(item) for item in obj["value"])

    # tbh deserializes dictionary. Probably BASE_COLLECTION could be replaced by dict but fig s nim
    elif collection_type in BASE_COLLECTIONS.keys():
        return BASE_COLLECTIONS[collection_type]({deserialize(item[0]): deserialize(item[1]) for item in obj["value"]})


def MiniMain():
    # print(inspect.getmembers(serialize_function.__code__))

    args = dict()

    args = {key: value for key, value in inspect.getmembers(serialize_function.__code__) if key in CODE_PROPERTIES}
    print(args)
    a = serialize({1: 2, 3: 4, (5, 6, 7): 6})
    print(deserialize(a))


MiniMain()
