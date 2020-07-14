# -*- coding: utf-8 -*-
# @Author  : LG

from abc import ABCMeta, abstractmethod

class CPU(metaclass=ABCMeta):   # 创建cpu抽象类
    @abstractmethod
    def calcute(self):          # 实现抽象方法,接口
        pass

class Inter(CPU):
    def __repr__(self):
        return "This is a Inret cpu"

    def calcute(self):
        print("Inter cpu calculation")

class Amd(CPU):
    def __repr__(self):
        return "This is a Amd cpu"

    def calcute(self):
        print("Amd cpu calculation")

class SimpleFactory:
    """
    简单工厂.工厂根据不同条件生产不同功能的类.
    """
    @staticmethod
    def product_cpu(name):
        if name == 'Inter':
            return Inter()
        elif name == 'Amd':
            return Amd()
        else:
            raise ValueError("{} not in cpu list".format(name))


if __name__ == '__main__':
    factory = SimpleFactory()
    cpu1 = factory.product_cpu('Inter')
    cpu2 = factory.product_cpu('Amd')

    print(cpu1)
    print(cpu2)
