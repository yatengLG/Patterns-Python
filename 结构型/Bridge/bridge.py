# -*- coding: utf-8 -*-
# @Author  : LG


class Function:
    def run(self):
        pass


class FloatCalculate(Function):
    def run(self):
        print("单精度计算")


class DoubleCalculate(Function):
    def run(self):
        print("双精度计算")


class CPU:
    def __init__(self):
        self.function = dict()

    def set_function(self, function_name, function):
        self.function[function_name] = function

    def run(self,function_name):
        function = self.function.get(function_name)
        if function is None:
            raise ValueError("function {} is not in the function list:{}".format(function_name, list(self.function.keys())))
        else:
            function.run()


class AMD(CPU):
    pass


class INTEL(CPU):
    pass


if __name__ == '__main__':

    float_calculate = FloatCalculate()
    double_calculate = DoubleCalculate()

    amd_cpu = AMD()
    amd_cpu.set_function("float_cal", float_calculate)
    amd_cpu.set_function("double_cal", double_calculate)
    amd_cpu.run("float_cal")
    amd_cpu.run("double_cal")

    intel_cpu = INTEL()
    intel_cpu.set_function("float_cal", float_calculate)
    intel_cpu.run("float_cal")
