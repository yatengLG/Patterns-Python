# -*- coding: utf-8 -*-
# @Author  : LG

from abc import ABCMeta

class CPU(metaclass=ABCMeta):
    pass


class Inter(CPU):
    def __repr__(self):
        return "This is a Inret cpu"


class Amd(CPU):
    def __repr__(self):
        return "This is a Amd cpu"


class Factory:
    """
    工厂基类
    """
    def product_cpu(self):
        raise NotImplementedError


class AmdFactory(Factory):
    def product_cpu(self):
        return Amd()


class InterFactory(Factory):
    def product_cpu(self):
        return Inter()


if __name__ == '__main__':

    inter_factory = InterFactory()
    amd_factory = AmdFactory()

    cpu1 = inter_factory.product_cpu()
    cpu2 = amd_factory.product_cpu()

    print(cpu1)
    print(cpu2)
