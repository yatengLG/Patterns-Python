# -*- coding: utf-8 -*-
# @Author  : LG

from abc import ABCMeta, abstractmethod

class CPUBuilder(metaclass=ABCMeta):
    @abstractmethod
    def get_material(self):
        raise NotImplementedError

    @abstractmethod
    def create(self):
        raise NotImplementedError


class Inter_Cpu_Builder(CPUBuilder):
    def get_material(self):
        print("正在挖沙子，提取硅，做晶圆......，准备做cpu。")

    def create(self):
        print("正在加工 Inter CPU")

    def __repr__(self):
        return "This is a Inret cpu"


class Amd_Cpu_Builder(CPUBuilder):
    def get_material(self):
        print("正在挖沙子，提取硅，做晶圆......，准备做cpu。")

    def create(self):
        print("正在加工 Amd CPU")

    def __repr__(self):
        return "This is a Amd cpu"


class GPUBuilder(metaclass=ABCMeta):
    @abstractmethod
    def get_material(self):
        raise NotImplementedError

    @abstractmethod
    def create(self):
        raise NotImplementedError


class Inter_Gpu_Builder(GPUBuilder):
    def get_material(self):
        print("直接买晶圆......，准备做gpu。")

    def create(self):
        print("正在加工 Inret GPU")

    def __repr__(self):
        return "This is a Inret gpu"


class Amd_Gpu_Builder(GPUBuilder):
    def get_material(self):
        print("直接买晶圆......，准备做gpu。")

    def create(self):
        print("正在加工 Amd GPU")

    def __repr__(self):
        return "This is a Amd gpu"


class Director:
    def __init__(self, equipment):
        self.equipment = equipment

    def create(self):
        self.equipment.get_material()
        self.equipment.create()


if __name__ == '__main__':

    equipment = Inter_Cpu_Builder()
    director = Director(equipment)
    director.create()

    equipment = Inter_Gpu_Builder()
    director = Director(equipment)
    director.create()

    equipment = Amd_Cpu_Builder()
    director = Director(equipment)
    director.create()

    equipment = Amd_Gpu_Builder()
    director = Director(equipment)
    director.create()
