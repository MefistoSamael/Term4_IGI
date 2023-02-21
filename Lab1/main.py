import MyConstants


def task1():
    print(MyConstants.greetings_message)


def task2(number1, number2, operation):
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


task1()
print(task2(5, 0, "div"))
