# -*- coding: utf-8 -*-
# @Author  : LG


class Component:
    def __init__(self, name):
        self.name = name
        self.component = []

    def add(self, component):
        self.component.append(component)

    def display(self, level=0):
        print('————'*level+self.name)
        components = self.component
        level = level+1
        for component in components:
            component.display(level)


if __name__ == '__main__':
    Computer = Component('Computer')
    Cpu = Component('Cpu')
    Gpu = Component('Gpu')

    Cpu_Component1 = Component('Cpu_Component1')
    Cpu_Component2 = Component('Cpu_Component2')

    Gpu_Component = Component('Gpu_Component')

    Cpu_Component1_Component1 = Component('Cpu_Component1_Component1')

    Computer.add(Cpu)
    Computer.add(Gpu)
    Cpu.add(Cpu_Component1)
    Cpu_Component1.add(Cpu_Component1_Component1)
    Cpu.add(Cpu_Component2)
    Gpu.add(Gpu_Component)

    Computer.display()

