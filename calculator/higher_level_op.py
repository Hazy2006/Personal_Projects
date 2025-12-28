import math

class AdvancedCalculator:
    @staticmethod
    def square_root(value):
        if value < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        return math.sqrt(value)

    @staticmethod
    def logarithm(value, base=10):
        if value <= 0:
            raise ValueError("Logarithm is undefined for non-positive values.")
        return math.log(value, base)

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Factorial is undefined for negative numbers.")
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers.")
        return math.factorial(n)

class TrigonometricOperations:
    @staticmethod
    def sine(angle_rad):
        return math.sin(angle_rad)

    @staticmethod
    def cosine(angle_rad):
        return math.cos(angle_rad)

    @staticmethod
    def tangent(angle_rad):
        return math.tan(angle_rad)

    @staticmethod
    def cotangent(angle_rad):
        tan_value = math.tan(angle_rad)
        if tan_value == 0:
            raise ValueError("Cotangent is undefined for this angle.")
        return 1 / tan_value

    @staticmethod
    def asin(angle_rad):
        if angle_rad < -1 or angle_rad > 1:
            raise ValueError("Input for arcsine must be in the range [-1, 1].")
        return math.asin(angle_rad)

    @staticmethod
    def acos(angle_rad):
        if angle_rad < -1 or angle_rad > 1:
            raise ValueError("Input for arccosine must be in the range [-1, 1].")
        return math.acos(angle_rad)

    @staticmethod
    def atan(angle_rad):
        return math.atan(angle_rad)