from json import load, dump
from re import match, compile
from constants import AGREE, DISAGREE, PATH, CONTAINER, ADD, \
    LIST, REMOVE, FIND, GREP, SAVE, LOAD, \
    SWITCH, EXIT, HELP


class MyContainer:
    def __init__(self, userName):
        self.userName = userName
        self.container = {}

        self.load_container()
        if self.userName not in self.container:
            self.container[self.userName] = []

    def add(self, *args):
        for element in args:
            if element not in self.container[self.userName]:
                self.container[self.userName].append(element)

    def remove(self, element):
        if self.userName not in self.container or element not in self.container[self.userName]:
            print("nothing to delete")
            return
        else:
            self.container[self.userName].remove(element)

    def find(self):
        pass

    def list(self):
        print(self.container[self.userName])

    def grep(self):
        pass

    def save(self):
        if self.userName not in self.container:
            self.container[self.userName] = []

        with open(PATH + CONTAINER + "data.json", 'w') as file:
            dump(self.container, file)

    def load_container(self):
        with open(PATH + CONTAINER + "data.json", 'r') as file:
            self.container = load(file)

    def clear_data(self):
        if self.userName in self.container:
            self.container[self.userName] = []

    def load_data(self):
        data = self.container[self.userName]
        self.load_container()
        for element in data:
            if element not in self.container[self.userName]:
                self.container[self.userName].append(element)

    def wanna_save(self):
        while True:
            command = input(f"wanna save some data ({AGREE}/{DISAGREE})")
            if command == AGREE:
                self.save()
                break
            elif command == DISAGREE:
                break

    def switch(self, userName):
        self.wanna_save()
        self.userName = userName
        if self.userName not in self.container:
            self.userName = []

    def help(self):
        print(f"commands list:"
              f"{ADD}\n{REMOVE}\n{FIND}\n{LIST}\n{GREP}\n{SAVE}\n{LOAD}\n{SWITCH}")
