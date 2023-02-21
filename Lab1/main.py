import MyConstants


def task1():
    print(MyConstants.greetings_message)


def task2(number1, number2, operation):
    try:
        return eval(number1.__str__() + " " + operation + " " + number2.__str__())
    except ZeroDivisionError:
        return "Error: division by zero"


task1()
print(task2(5, 0, "/"))
