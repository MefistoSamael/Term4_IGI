

class ErrorHandler:

    @staticmethod
    def handle_empty_input():
        print("Error: empty string. Please, try again\n")

    @staticmethod
    def handle_invalid_command():
        print("Error: invalid command. Please try again\n")

    @staticmethod
    def handle_unexpected_error():
        print("Wow, smth went really bad. Idk what happened. Probably, my author, is dum..., I mean he tried his"
              "best, but he did some mistake\n")
