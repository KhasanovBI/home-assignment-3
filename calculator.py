import math
from decimal import *


def round_result(function):
    def function_wrapper(*args):
        with localcontext(Context(10)):
            return float(round(function(*args), 10))

    return function_wrapper


class Calculator():
    @staticmethod
    @round_result
    def add(a, b):
        return Decimal(a) + Decimal(b)

    @staticmethod
    @round_result
    def subtract(a, b):
        return Decimal(a) - Decimal(b)

    @staticmethod
    @round_result
    def multiply(a, b):
        return Decimal(a) * Decimal(b)

    @staticmethod
    @round_result
    def divide(a, b):
        return Decimal(a) / Decimal(b)

    @staticmethod
    @round_result
    def sin(x):
        return Decimal(math.sin(x))
