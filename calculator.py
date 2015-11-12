import math
from decimal import *


def round_result_of_binary_operation(function):
    def function_wrapper(a, b):
        with localcontext(Context(8)):
            return float(function(a, b))

    return function_wrapper


class Calculator():
    @staticmethod
    @round_result_of_binary_operation
    def add(a, b):
        return Decimal(a) + Decimal(b)

    @staticmethod
    @round_result_of_binary_operation
    def subtract(a, b):
        return Decimal(a) - Decimal(b)

    @staticmethod
    @round_result_of_binary_operation
    def multiply(a, b):
        return Decimal(a) * Decimal(b)

    @staticmethod
    @round_result_of_binary_operation
    def divide(a, b):
        return Decimal(a) / Decimal(b)

    @staticmethod
    def sin(x):
        return math.sin(x)
