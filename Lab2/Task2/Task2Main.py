from Task2.Task2Constants import COMMANDS, ERRORS
from Task2.Task2Constants import LOAD_DATA, INPUT_COMMAND, INPUT_USERNAME
from Task2.Task2Container import MyContainer
from Task2.Task2ErrorHandler import ErrorHandler


def task2_main():
    while True:
        container = handle_username_input()

        handle_data_load(container)

        while True:
            command = input(INPUT_COMMAND)
            if command.startswith(COMMANDS.ADD):
                args = command.split()[1:]
                container.add(args)

            elif command.startswith(COMMANDS.REMOVE):
                args = command.split()[1:]
                container.remove(args)

            elif command.startswith(COMMANDS.FIND):
                args = command.split()[1:]
                container.find(args)

            elif command.startswith(COMMANDS.LIST):
                container.list()

            elif command.startswith(COMMANDS.SAVE):
                container.save()

            elif command.startswith(COMMANDS.LOAD):
                container.load_data()

            elif command.startswith(COMMANDS.EXIT):
                container.wanna_save()
                return

            elif command.startswith(COMMANDS.SWITCH):
                args = command.split()[1:]
                container.switch(args)

            elif command.startswith(COMMANDS.HELP):
                container.help()


def handle_username_input():
    while True:
        username = input_username()

        if type(username) == type(""):
            return MyContainer(username)
        else:
            match username:
                case ERRORS.EMPTY_INPUT:
                    ErrorHandler.handle_empty_input()

                case _:
                    ErrorHandler.handle_unexpected_error()


def handle_data_load(container):
    while True:
        check_state = load_data(container)

        match check_state:
            case ERRORS.VALID:
                return

            case ERRORS.INVALID_COMMAND:
                ErrorHandler.handle_invalid_command()

            case _:
                ErrorHandler.handle_unexpected_error()


def handle_command_input(container):
    pass


# Gets command from input.
# If command not empty and contains in COMMANDS
# method returns corresponding command
def input_command(container):
    command = input(INPUT_COMMAND)

    check_state = is_empty_input(command)

    # First check - check for empty input
    match check_state:
        case ERRORS.EMPTY_INPUT:
            return ERRORS.EMPTY_INPUT

        case ERRORS.VALID:
            pass

        case _:
            return ERRORS.UNEXPECTED_ERROR

    # If input isn't empty - main check:
    # Commands check

    if COMMANDS.CONTAINS(command):
        return command
    else:
        return ERRORS.INVALID_COMMAND


# Inputs username
def input_username():
    username = input(INPUT_USERNAME)

    check_state = is_empty_input(username)
    if check_state == ERRORS.VALID:
        return username
    else:
        return check_state


# Loads data
def load_data(container):
    answer = input(f"{LOAD_DATA} ({COMMANDS.AGREE}/{COMMANDS.DISAGREE}) ")

    match answer:

        case COMMANDS.AGREE.value:
            return ERRORS.VALID

        case COMMANDS.DISAGREE.value:
            container.clear_data()
            return ERRORS.VALID

        case _:
            return ERRORS.INVALID_COMMAND


# Checks, if username is valid returns ERRORS.VALID
# else returns ERRORS.EMPTY_INPUT
def is_empty_input(input_line):
    if not input_line:
        return ERRORS.EMPTY_INPUT
    else:
        return ERRORS.VALID
