# -*- coding: utf-8 -*-
# @Author  : LG


class Calculate:
    def float_calculate(self):
        print("单精度计算")

    def double_calculate(self):
        print("双精度计算")


class CPU:
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def float_calculate(self):
        print("cpu 单精度计算")

    def __getattr__(self, name):
        return getattr(self._decoratee, name)


if __name__ == '__main__':

    calculate = Calculate()
    cpu = CPU(calculate)
    cpu.float_calculate()
    cpu.double_calculate()