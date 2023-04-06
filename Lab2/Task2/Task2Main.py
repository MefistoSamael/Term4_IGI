from Task2.Task2Constants import COMMANDS, ERRORS, CONTAINER_OUTPUT
from Task2.Task2Constants import LOAD_DATA, INPUT_COMMAND, INPUT_USERNAME
from Task2.Task2Container import MyContainer
from Task2.Task2ErrorHandler import ErrorHandler
from Task2.Task2ContainerOutputHandler import ContainerOutputHandler


def task2_main():
    # Username input part
    container = handle_username_input()

    # Load data part
    handle_data_load(container)

    # Users command computing part
    handle_command_input(container)


# Handles username input
def handle_username_input():
    while True:
        username = input_username()

        # If any name where entered, then its valid
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
        # Loads data and proceeds value that returns method load_data
        check_state = ContainerOutputHandler.HandleContainerOutput(load_data(container))

        # If everything where good
        if check_state == ERRORS.VALID:
            return


def handle_command_input(container):
    while True:
        # Command enter
        commandExpression = input_command(container)

        # If error occurred - handle error
        if type(commandExpression) == type(ERRORS.EMPTY_INPUT):
            match commandExpression:
                case ERRORS.EMPTY_INPUT:
                    ErrorHandler.handle_empty_input()
                case ERRORS.UNEXPECTED_ERROR:
                    ErrorHandler.handle_unexpected_error()
                case ERRORS.INVALID_COMMAND:
                    ErrorHandler.handle_invalid_command()
        # If everything is good - beginning to handle command
        else:
            # Gets command itself
            command = commandExpression[0]
            # Gets arguments of command
            args = commandExpression[1][0:]
            # To see how I work with command input check method input_command

            match command:
                case COMMANDS.ADD:
                    ContainerOutputHandler.HandleContainerOutput(container.add(args))

                case COMMANDS.REMOVE:
                    ContainerOutputHandler.HandleContainerOutput(container.remove(args))

                # Empty arguments must be proceeded
                case COMMANDS.FIND:
                    ContainerOutputHandler.HandleContainerOutput(container.find(args))

                case COMMANDS.LIST:
                    container.list()

                case COMMANDS.GREP:
                    ContainerOutputHandler.HandleContainerOutput(container.grep(args))

                case COMMANDS.SAVE:
                    ContainerOutputHandler.HandleContainerOutput(container.save())

                case COMMANDS.LOAD:
                    ContainerOutputHandler.HandleContainerOutput(container.load_data())

                case COMMANDS.EXIT:
                    ContainerOutputHandler.HandleContainerOutput(container.wanna_save())
                    return

                case COMMANDS.SWITCH:
                    ContainerOutputHandler.HandleContainerOutput(container.switch(args))

                case COMMANDS.HELP:
                    container.help()

                case _:
                    ErrorHandler.handle_invalid_command()


# Gets command from input.
# If command not empty and contains in COMMANDS
# method returns tuple of corresponding command(enum) and its arguments
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

    # variable command - contains of command itself and its arguments,
    #  for example: 'add a, b, c'. So I divided it,  and command[0] will return command itself
    command = command.split()
    if COMMANDS.CONTAINS(command[0]):
        # Gets corresponding enum from COMMANDS, adds to it arguments of command and return it as tuple
        return COMMANDS.GETITEM(command[0]), command[1:]
    else:
        return ERRORS.INVALID_COMMAND


# Inputs username
def input_username():
    username = input(INPUT_USERNAME)

    check_state = is_empty_input(username)
    if check_state == ERRORS.VALID:
        return username
    else:
        # Returns the certain ERROR
        return check_state


# Loads data
def load_data(container):
    answer = input(f"{LOAD_DATA} ({COMMANDS.AGREE.value}/{COMMANDS.DISAGREE.value}) ")

    match answer:
        # If person agrees to load data
        case COMMANDS.AGREE.value:
            return container.load_data()

        # If person disagrees to load data
        case COMMANDS.DISAGREE.value:
            return CONTAINER_OUTPUT.VALID

        # If something went wrong
        case _:
            return CONTAINER_OUTPUT.UNEXPECTED_ERROR


# Checks, if username is valid returns ERRORS.VALID
# else returns ERRORS.EMPTY_INPUT
def is_empty_input(input_line):
    if not input_line:
        return ERRORS.EMPTY_INPUT
    else:
        return ERRORS.VALID
