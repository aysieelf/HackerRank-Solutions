"""
Task:
    For this challenge, you are given two complex numbers, and you have to print the result of their addition,
    subtraction, multiplication, division and modulus operations.
    The real and imaginary precision part should be correct up to two decimal places.
"""

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.complex = complex(self.real, self.imaginary)

    def __add__(self, no):
        result = self.complex + no.complex
        return Complex(result.real, result.imag)

    def __sub__(self, no):
        result = self.complex - no.complex
        return Complex(result.real, result.imag)

    def __mul__(self, no):
        result = self.complex * no.complex
        return Complex(result.real, result.imag)

    def __truediv__(self, no):
        result = self.complex / no.complex
        return Complex(result.real, result.imag)

    def mod(self):
        result = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(result, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')