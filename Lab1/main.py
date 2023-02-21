import MyConstants


# Just outputs greetings_message
# that located in MyConstants.py
def task1():
    print(MyConstants.greetings_message)


def task2(number1, number2, operation):
    try:
        return eval(number1.__str__() + " "
                    + operation + " "
                    + number2.__str__())
    except ZeroDivisionError:
        return "Error: division by zero"


def task3():
    arr = list(range(MyConstants.list_length))
    if arr:
        return arr[::2]


task1()
print(task2(5, 0, "/"))
print(task3())
