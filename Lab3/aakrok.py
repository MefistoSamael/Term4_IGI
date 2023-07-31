import sys

from sir_Bychko_serializer import serialiser
from sir_Bychko_serializer import serializer_zavod

def my_func(a):
    return a+2

zavod = serializer_zavod.zavod.create_zavod('json')

zavod.dump(my_func, open('test2.json', 'w'))




#ser = serialize(my_func)

#deser = deserialize(ser)

#print(sys.version_info)

