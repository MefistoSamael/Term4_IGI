from GlobalConstants import FILES_PATH
from enum import Enum

# Output strings

INPUT_PROMPT = "Please enter"
INPUT_COMMAND = INPUT_PROMPT + " command: "
INPUT_USERNAME = INPUT_PROMPT + "username: "
LOAD_DATA = "Do you want to load data?"


# Commands

class COMMANDS(Enum):
    DISAGREE = 'net'
    AGREE = "y"
    ADD = "add"
    LIST = "list"
    REMOVE = "remove"
    FIND = "find"
    GREP = "grep"
    SAVE = "save"
    LOAD = "load"
    SWITCH = "switch"
    EXIT = "exit"
    HELP = "help"

    @staticmethod
    def CONTAINS(item):
        for member in COMMANDS.__members__.items():
            if item == member[1].value:
                return True
        return False

    @staticmethod
    def GETITEM(obj):
        for member in COMMANDS.__members__.items():
            if obj == member[1].value:
                return member[1]

        raise Exception("Index error")




# Files

CONTAINER = FILES_PATH + "Container/"


# Errors

class ERRORS(Enum):
    VALID = 0
    EMPTY_INPUT = 1
    INVALID_COMMAND = 2
    UNEXPECTED_ERROR = 3
