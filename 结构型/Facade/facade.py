# -*- coding: utf-8 -*-
# @Author  : LG


class CPU:
    def float_calculate(self):
        pass

    def double_calculate(self):
        pass


class AMD(CPU):
    def float_calculate(self):
        print("Amd cpu 单精度计算")

    def double_calculate(self):
        print("Amd cpu 双精度计算")


class INTEL(CPU):
    def float_calculate(self):
        print("Intel cpu 单精度计算")

    def double_calculate(self):
        print("Intel cpu 双精度计算")


class Facade:
    def __init__(self):
        self.amd = AMD()
        self.intel = INTEL()

    def float_calculate(self):
        self.amd.float_calculate()
        self.intel.float_calculate()

    def double_calculate(self):
        self.amd.double_calculate()
        self.intel.double_calculate()


if __name__ == '__main__':

    facade = Facade()
    facade.float_calculate()