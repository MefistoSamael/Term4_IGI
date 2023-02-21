import MyConstants


# Just outputs greetings_message
# that located in MyConstants.py
def task1():
    print(MyConstants.greetings_message)


# Evaluates expression, that consists of
# number1 operation number2
def task2(number1, number2, operation):
    try:
        return eval(number1.__str__() + " "
                    + operation + " "
                    + number2.__str__())
    except ZeroDivisionError:
        return "Error: division by zero"


# Returns list of even number
def task3():
    arr = list(range(MyConstants.list_length))

    if arr:
        return arr[::2]
