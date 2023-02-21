import MyConstants


# Just outputs greetings_message
# that located in MyConstants.py
def task1():
    print(MyConstants.greetings_message)


# Evaluates expression, that consists of
# number1 operation number2
def task21(number1, number2, operation):
    try:
        number1 = float(number1)
        number2 = float(number2)
    except:
        return "Error: invalid input"

    try:
        return eval(number1.__str__() + " "
                    + operation + " "
                    + number2.__str__())
    except ZeroDivisionError:
        return "Error: division by zero"
    except:
        return "Error: invalid operation"


# Another variation of task2
def task22(number1, number2, operation):
    if operation == "add":
        return number1 + number2
    elif operation == "sub":
        return number1 - number2
    elif operation == "mult":
        return number1 * number2
    elif operation == "div":

        if number2:
            return number1 / number2
        else:
            return "Error: division by zero"

    else:
        return "Error: invalid operation"


# Returns list of even number
def task3(arr: list[int]):
    try:
        return [i for i in arr if not (i % 2)]
    except TypeError:
        return "Error: invalid list"
