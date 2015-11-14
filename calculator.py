import math
from decimal import *


def round_result(function):
    def function_wrapper(*args):
        with localcontext(Context(10)):
            return round(function(*map(lambda x: Decimal(str(x)), args)), 10)

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
    @round_result
    def sin(x):
        return math.sin(x)
