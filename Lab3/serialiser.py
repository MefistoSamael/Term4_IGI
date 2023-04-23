import re
from constants import *


def get_obj_type(obj):
    return re.search(r"\'(\w+)\'", str(type(obj)))[1]


def serialize_base_types(obj):
    srz = dict()

    srz["type"] = get_obj_type(obj)
    srz["value"] = obj
    return srz


def serialize_none_type():
    srz = dict()

    srz["type"] = "NoneType"
    srz["value"] = None
    return srz


def serialize_similar_collections(obj):
    srz = dict()

    srz["type"] = get_obj_type(obj)
    srz["value"] = [serialize(item) for item in obj]
    return srz


def serialize_dict(obj):
    srz = dict()

    srz["type"] = get_obj_type(obj)
    srz["value"] = [[serialize(key), serialize(value)] for (key, value) in obj.items()]
    return srz


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


def deserialize(obj):
    if obj["type"] in str(BASE_TYPES):
        return deserialize_base_type(obj)

    elif obj["type"] in str(BASE_COLLECTIONS):
        return deserialize_base_collections(obj)


def MiniMain():
    a = serialize({1: 2, 3: 4, (5, 6, 7): 6})
    print(deserialize(a))


MiniMain()
