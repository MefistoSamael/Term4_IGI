import re
from json import load, dump
from re import match, compile
from Task2.Task2Constants import COMMANDS, CONTAINER, CONTAINER_OUTPUT, SAVE_DATA, COMMANDS_LIST


class MyContainer:
    def __init__(self, userName):
        self.userName = userName
        self.user_container = []
        self.file = {}

        self.load_file()

    # Add element or elements in the container
    # Takes string if adding one element
    # Takes list if adding multiply elements
    def add(self, arg):
        if not arg:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS

        # If got arg, as one element
        if type(arg) == type(''):
            if arg not in self.user_container:
                self.user_container.append(arg)
        # If got arg as list of elements
        else:
            # Adding elements to the container
            for element in arg:
                if element not in self.user_container:
                    self.user_container.append(element)

        return CONTAINER_OUTPUT.VALID

    # Removes element from the container
    def remove(self, element):
        # Gets first item from element, if there is any items
        if element:
            element = element[0]
        else:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS

        # Deleting part
        if element not in self.user_container:
            return CONTAINER_OUTPUT.NOTHING_TO_DELETE
        else:
            self.user_container.remove(element)
            return CONTAINER_OUTPUT.VALID

    # Finds elements or element in the container
    def find(self, arg):
        # Check block
        # Empty container check
        if not self.user_container:
            return CONTAINER_OUTPUT.EMPTY_CONTAINER
        # Empty argument check
        if not arg:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS

        # If got arg, as one element
        if type(arg) == type(''):
            if arg not in self.user_container:
                return CONTAINER_OUTPUT.NO_SUCH_ELEMENT
            else:
                print(arg)
                return CONTAINER_OUTPUT.VALID
        # If got arg as list of elements
        else:
            # Finding elements in the container
            # Variable to check if element where founded. It determines what method will return:
            # VALID, if element where founded or
            # NO_SUCH_ELEMENT, if no elements where founded in the container
            element_where_founded = 0
            for element in arg:
                if element in self.user_container:
                    print(element)
                    element_where_founded = 1

            if element_where_founded:
                return CONTAINER_OUTPUT.VALID
            else:
                return CONTAINER_OUTPUT.NO_SUCH_ELEMENT

    def list(self):
        print(self.user_container)

    def grep(self, reg):
        # Check block
        # Empty container check
        if not self.user_container:
            return CONTAINER_OUTPUT.EMPTY_CONTAINER
        # Empty argument check
        if not reg:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS
        else:
            # Getting first argument
            reg = reg[0]

        try:
            reg_match = [element for element in self.user_container if match(compile(reg), element)]
        except re.error:
            return CONTAINER_OUTPUT.INVALID_REGEX

        if reg_match:
            print("Matched elements: ")
            for elem in reg_match:
                print(elem)
            return CONTAINER_OUTPUT.VALID
        else:
            return CONTAINER_OUTPUT.NO_SUCH_ELEMENT


    # Saves all data in file
    def save(self):
        # Saving data in dictionary of all users and its containers
        self.file[self.userName] = self.user_container

        with open(CONTAINER + "data.json", 'w') as file:
            dump(self.file, file)

        return CONTAINER_OUTPUT.VALID

    # Loads all data from file to dictionary
    def load_file(self):
        with open(CONTAINER + "data.json", 'r') as file:
            self.file = load(file)

    # Loads container from the file and updates the file in class
    def load_data(self):
        # Saving the data from current container
        data = self.user_container
        # This load is needed to maintain actual data in dictionary
        self.load_file()

        # If user tries to load data from file, and there is no data in this file, connected to user
        if not self.file.get(self.userName):
            return CONTAINER_OUTPUT.EMPTY_CONTAINER

        # Loading data from loaded container
        self.add(self.file[self.userName])
        return CONTAINER_OUTPUT.VALID

    # Asks if user want to save some data, and saves it if user agrees
    def wanna_save(self):
        while True:
            command = input(f"{SAVE_DATA} ({COMMANDS.AGREE.value}/{COMMANDS.DISAGREE.value})")
            if command == COMMANDS.AGREE.value:
                self.save()
                return CONTAINER_OUTPUT.VALID

            elif command == COMMANDS.DISAGREE.value:
                return CONTAINER_OUTPUT.VALID

    # Switches user
    def switch(self, ListUserName):
        if not ListUserName:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS

        self.wanna_save()

        # Cleans up container of lust user
        self.user_container = []

        # This string is needed because when user inputs userName, after
        # switch command, it gives list in function
        true_user_name = ListUserName[0]

        self.userName = true_user_name
        if self.userName not in self.file:
            self.user_container = []

        return CONTAINER_OUTPUT.VALID

    def help(self):
        print(COMMANDS_LIST)
