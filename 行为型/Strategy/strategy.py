# -*- coding: utf-8 -*-
# @Author  : LG

from abc import ABCMeta, abstractmethod

class Calculation(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self, *input):
        pass


class Add(Calculation):
    def calculate(self, *input):
        output = 0
        print(output, end='')

        for i in input:
            output += i
            print('+{}'.format(i),end='')
        print('={}'.format(output))
        return output


class Mul(Calculation):
    def calculate(self, *input):
        output = 1
        print(output, end='')

        for i in input:
            output *= i
            print('x{}'.format(i), end='')
        print('={}'.format(output))
        return output


class Calculator:
    def __init__(self):
        self.calculation = None

    def set_calculation(self, calculation):
        self.calculation = calculation

    def calculate(self, *input):
        return self.calculation.calculate(*input)


if __name__ == '__main__':
    add = Add()
    mul = Mul()

    calculator = Calculator()
    calculator.set_calculation(add)
    output = calculator.calculate(1,2,3,4,5,6)

    calculator.set_calculation(mul)
    output = calculator.calculate(1,2,3,4,5,6)
