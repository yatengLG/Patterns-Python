# -*- coding: utf-8 -*-
# @Author  : LG


class CPU:
    pass


class Inter_Cpu(CPU):
    def __repr__(self):
        return "This is a Inret cpu"


class Amd_Cpu(CPU):
    def __repr__(self):
        return "This is a Amd cpu"


class GPU:
    pass


class Inter_Gpu(GPU):
    def __repr__(self):
        return "This is a Inret gpu"


class Amd_Gpu(GPU):
    def __repr__(self):
        return "This is a Amd gpu"


class Factory:
    """
    工厂基类
    """
    def product_cpu(self):
        raise NotImplementedError

    def product_gpu(self):
        raise NotImplementedError


class AmdFactory(Factory):
    def product_cpu(self):
        return Amd_Cpu()

    def product_gpu(self):
        return Amd_Gpu()


class InterFactory(Factory):
    def product_cpu(self):
        return Inter_Cpu()

    def product_gpu(self):
        return Inter_Gpu()


if __name__ == '__main__':
    inter_factory = InterFactory()
    amd_factory = AmdFactory()

    cpu1 = inter_factory.product_cpu()
    cpu2 = amd_factory.product_cpu()

    gpu1 = inter_factory.product_gpu()
    gpu2 = amd_factory.product_gpu()

    print(cpu1)
    print(cpu2)
    print(gpu1)
    print(gpu2)