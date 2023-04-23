BASE_TYPES = {"str": str, "int": int, "bool": bool, "float": float, "complex": complex}

SIMILAR_COLLECTIONS = {"list": list, "tuple": tuple, "frozenset": frozenset, "set": set, "bytes": bytes,
                       "bytearray": bytearray}

BASE_COLLECTIONS = {"list": list, "tuple": tuple, "frozenset": frozenset, "set": set, "bytes": bytes,
                    "bytearray": bytearray, "dict": dict}

CODE_PROPERTIES = ("co_nlocals",
                   "co_argcount",
                   "co_varnames",
                   "co_names",
                   "co_cellvars",
                   "co_freevars",
                   "co_posonlyargcount",
                   "co_kwonlyargcount",
                   "co_firstlineno",
                   "co_lnotab",
                   "co_stacksize",
                   "co_code",
                   "co_consts",
                   "co_flags",
                   "co_filename")
