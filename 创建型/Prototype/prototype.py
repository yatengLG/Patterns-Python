# -*- coding: utf-8 -*-
# @Author  : LG

import copy


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, name, obj):
        self.objects[name] = obj

    def clone(self, name, **attrs):
        obj = self.objects.get(name)
        if obj is None:
            raise ValueError("{} not in Prototype.".format(name))
        obj = copy.deepcopy(obj)
        obj.__dict__.update(attrs)
        return obj


class CPU:
    def __init__(self, brand, model, core, thread):
        self.brand = brand
        self.model = model
        self.core = core
        self.thread = thread

    def __repr__(self):
        return "This is a {} CPU: {} \n{} core {} thread.\n------".format(self.brand, self.model, self.core, self.thread)


if __name__ == '__main__':

    cpu1 = CPU(brand="AMD", model="Ryzen9 3900X", core=12, thread=24)
    print(cpu1)

    prototype = Prototype()
    prototype.register("cpu", cpu1)

    cpu2 = prototype.clone("cpu", brand="AMD", model="Ryzen5 3600", core=6, thread=12)
    print(cpu2)

    cpu3 = prototype.clone("cpu", brand="Inter", model="i9 9900K", core=8, thread=16)
    print(cpu3)
