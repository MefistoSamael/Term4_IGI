BASE_TYPES = {"str": str, "int": int, "bool": bool, "float": float, "complex": complex}

SIMILAR_COLLECTIONS = {"list": list, "tuple": tuple, "frozenset": frozenset, "set": set, "bytes": bytes,
                       "bytearray": bytearray}

BASE_COLLECTIONS = {"list": list, "tuple": tuple, "frozenset": frozenset, "set": set, "bytes": bytes,
                    "bytearray": bytearray, "dict": dict}

CODE_PROPERTIES = ("co_argcount",
                   "co_posonlyargcount",
                   "co_kwonlyargcount",
                   "co_nlocals",
                   "co_stacksize",
                   "co_flags",
                   "co_code",
                   "co_consts",
                   "co_names",
                   "co_varnames",
                   "co_filename",
                   "co_name",
                   "co_firstlineno",
                   "co_linetable",
                   "co_freevars",
                   "co_cellvars")
