import math
from decimal import *


def round_result(function):
    def function_wrapper(*args):
        with localcontext(Context(10)):
            return float(function(*map(lambda x: Decimal(str(x)), args)))

    return function_wrapper


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    @round_result
    def add(a, b):
        return a + b

    @staticmethod
    @round_result
    def subtract(a, b):
        return a - b

    @staticmethod
    @round_result
    def multiply(a, b):
        return a * b

    @staticmethod
    @round_result
    def divide(a, b):
        return a / b

    @staticmethod
    def sin(x):
        return round(math.sin(x), 10)
