from GlobalConstants import FILES_PATH
from enum import Enum

# Files

CONTAINER = FILES_PATH + "Container/"


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


# Output strings

INPUT_PROMPT = "Please enter"
INPUT_COMMAND = INPUT_PROMPT + " command: "
INPUT_USERNAME = INPUT_PROMPT + " username: "
LOAD_DATA = "Do you want to load data?"
SAVE_DATA = "Wanna save some data?"
COMMANDS_LIST = "commands list: \n\n" \
                f"{COMMANDS.DISAGREE.value} - disagree with smth\n\n" \
                f"{COMMANDS.AGREE.value} - agree with smth\n\n" \
                f"{COMMANDS.ADD.value} <key> [key, …] – add one or more elements to the container\n" \
                f"(if the element is already in there then don’t add)\n\n"\
                f"{COMMANDS.LIST.value} - print all elements of container\n\n" \
                f"{COMMANDS.REMOVE.value} <key> – delete key from container\n\n" \
                f"{COMMANDS.FIND.value}  <key> [key, …] – check if the element is presented in the\n" \
                f"container, print each found or “No such elements” if nothing is\n\n" \
                f"{COMMANDS.GREP.value}  <regex> – check the value in the container by regular expression,\n" \
                f"print each found or “No such elements” if nothing is\n\n" \
                f"{COMMANDS.SAVE.value}/{COMMANDS.LOAD.value} – save container to file/load container from file\n\n" \
                f"{COMMANDS.SWITCH.value} – switches to another user\n\n"


# Errors

class ERRORS(Enum):
    EMPTY_INPUT = 0
    VALID = 1
    INVALID_COMMAND = 2
    UNEXPECTED_ERROR = 3


class CONTAINER_OUTPUT(Enum):
    NOTHING_TO_DELETE = -1
    EMPTY_ARGUMENTS = 0
    VALID = 1
    NO_SUCH_ELEMENT = 2
    UNEXPECTED_ERROR = 3
    EMPTY_CONTAINER = 4
    INVALID_REGEX = 5
