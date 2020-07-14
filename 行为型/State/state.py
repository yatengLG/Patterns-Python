# -*- coding: utf-8 -*-
# @Author  : LG

from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

class opening(State):
    def run(self):
        print("电梯门正在开启中，禁止运行，运行命令无效")
        return self

    def stop(self):
        print("电梯门正在开启中，电梯已处于停止状态，停止命令无效")
        return self

    def open(self):
        print("电梯门已处于开启状态，开门命令无效")
        return self

    def close(self):
        print("电梯门关闭")
        return closing()

    def __repr__(self):
        return '[开门]'


class closing(State):
    def run(self):
        print("电梯运行")
        return runing()

    def stop(self):
        print("电梯停止")
        return stopping()

    def open(self):
        print("电梯门开启")
        return opening()

    def close(self):
        print("电梯门已关闭，关门命令无效")
        return self

    def __repr__(self):
        return '[关门]'


class runing(State):
    def run(self):
        print("电梯正在运行，运行命令无效")
        return self

    def stop(self):
        print("电梯停止")
        return stopping()

    def open(self):
        print("电梯正在运行, 开门命令无效")
        return self

    def close(self):
        print("电梯正在运行，电梯门已关闭，关门命令无效")
        return self

    def __repr__(self):
        return '[运行]'


class stopping(State):
    def run(self):
        print("电梯运行")
        return runing()

    def stop(self):
        print("电梯已经停止，停止命令无效")
        return self

    def open(self):
        print("电梯门开启")
        return opening()

    def close(self):
        print("电梯门关闭")
        return closing()

    def __repr__(self):
        return '[停止]'


class Elevator(object):
    def __init__(self):
        self.state = stopping()

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def run(self):
        print('--run')
        self.state = self.state.run()

    def stop(self):
        print('--stop')
        self.state = self.state.stop()

    def open(self):
        print('--open')
        self.state = self.state.open()

    def close(self):
        print('--close')
        self.state = self.state.close()


if __name__ == '__main__':

    elevator = Elevator()

    elevator.run()
    print(elevator.state)

    elevator.run()
    print(elevator.state)

    elevator.open()
    print(elevator.state)

    elevator.stop()
    print(elevator.state)

    elevator.open()
    print(elevator.state)

    elevator.open()
    print(elevator.state)

    elevator.open()
    print(elevator.state)

    elevator.run()
    print(elevator.state)

    elevator.close()
    print(elevator.state)

    elevator.run()
    print(elevator.state)