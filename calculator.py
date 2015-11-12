import math


class Calculator():
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return float(a) / b

    @staticmethod
    def sin(x):
        return math.sin(x)
