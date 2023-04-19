import re


def serialise(obj):
    def get_obj_type():
        return re.search(r"\'(\w+)\'", str(type(obj)))[1]

    srz = dict()

    # Serialising of base types
    if isinstance(obj, (str, int, bool, float, complex)):
        srz["type"] = get_obj_type()
        srz["value"] = obj

    elif not obj:
        srz["type"] = "NoneType"
        srz["value"] = None

    elif isinstance(obj, (list, tuple, frozenset, set, bytes, bytearray)):
        srz["type"] = get_obj_type()
        srz["value"] = [serialise(item) for item in obj]
        
    elif isinstance(obj, dict):
        srz["type"] = get_obj_type()
        srz["value"] = [[serialise(key), serialise(value)] for (key, value) in obj.items()]

    return srz


def MiniMain():
    print(serialise({"a":5, "5":"7"}))


MiniMain()
