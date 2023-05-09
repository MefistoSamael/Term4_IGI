import math
import re

example = "1v1"


def my_func(a):
    str = example + a
    reg = r"\d\w\d"
    return re.match(reg, str).group()


def my_decorator(func):
    print("hellp from decorator")

    def wrapper(*args, **kwargs):
        print("hello from wrapper")
        res = func(*args, **kwargs)
        print("Func end")
        return res

    return wrapper


@my_decorator
def for_dec():
    print("Hello from function!")


X = 12


class A:
    jivi = "esche hot'"

    @staticmethod
    def ret_jivi():
        return A.jivi

    def my_method(self, x):
        return x + 5


class B:
    @staticmethod
    @my_decorator
    def another_method(k):
        print("Hi:)")
        return math.sin(k * X)


class C(A, B):
    def __init__(self):
        self.chetvert = "veka"

    def sus(self, k):
        return k
