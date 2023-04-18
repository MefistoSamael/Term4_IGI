from Task2.Task2Constants import CONTAINER_OUTPUT, ERRORS


# Handles output of the container
class ContainerOutputHandler:

    @staticmethod
    def HandleContainerOutput(output):
        match output:
            case CONTAINER_OUTPUT.EMPTY_CONTAINER:
                return ContainerOutputHandler.__handle_empty_container()
            case CONTAINER_OUTPUT.VALID:
                return ContainerOutputHandler.__handle_valid()
            case CONTAINER_OUTPUT.NO_SUCH_ELEMENT:
                return ContainerOutputHandler.__handle_no_such_element()
            case CONTAINER_OUTPUT.EMPTY_ARGUMENTS:
                return ContainerOutputHandler.__handle_empty_arguments()
            case CONTAINER_OUTPUT.NOTHING_TO_DELETE:
                return ContainerOutputHandler.__handle_nothing_to_delete()
            case CONTAINER_OUTPUT.INVALID_REGEX:
                return ContainerOutputHandler.__handle_invalid_regex()

    @staticmethod
    def __handle_empty_container():
        print("Container is empty\n")

    @staticmethod
    def __handle_valid():
        print("Operation executed successfully\n")
        return ERRORS.VALID

    @staticmethod
    def __handle_no_such_element():
        print("No such element\n")

    @staticmethod
    def __handle_empty_arguments():
        print("Empty arguments\n")

    @staticmethod
    def __handle_nothing_to_delete():
        print("Nothing to delete\n")

    @staticmethod
    def __handle_invalid_regex():
        print("U entered invalid regex(exception has been thrown)\n")
