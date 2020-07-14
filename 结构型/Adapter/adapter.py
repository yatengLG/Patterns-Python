# -*- coding: utf-8 -*-
# @Author  : LG


class CPU:
    def calculate(self):
        pass


class AMD(CPU):
    def calculate(self):
        print("AMD cpu 进行运算")


class INTER(CPU):
    def inter_calculate(self):
        print("Inter cpu 进行运算")


class Adapter(CPU):
    def __init__(self, adapted_methods):
        self.adapted_methods = adapted_methods

    def calculate(self):
        return self.adapted_methods.inter_calculate()


if __name__ == '__main__':
    amd_cpu = AMD()
    amd_cpu.calculate()

    intel_cpu = INTER()
    intel_cpu.inter_calculate()

    intel_cpu = Adapter(intel_cpu)
    intel_cpu.calculate()