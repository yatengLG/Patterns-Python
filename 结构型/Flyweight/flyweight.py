# -*- coding: utf-8 -*-
# @Author  : LG


class CPU:
    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return "This is a {} cpu.".format(self.brand)


class Factory:
    def __init__(self):
        self.registed = dict()

    def register_cpu(self, brand):
        if not brand in self.registed:
            self.registed[brand] = CPU(brand)
        return self.registed[brand]


if __name__ == '__main__':
    factory = Factory()
    cpu1 = factory.register_cpu("AMD")
    print(cpu1)

    cpu2 = factory.register_cpu("AMD")
    print(cpu2)

    cpu3 = factory.register_cpu("Intel")
    print(cpu3)

    cpu4 = factory.register_cpu("AMD")
    print(cpu4)

    print(id(cpu1), id(cpu2), id(cpu3), id(cpu4))