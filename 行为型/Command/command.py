# -*- coding: utf-8 -*-
# @Author  : LG

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):        # 命令抽象类
    @abstractmethod
    def execute(self):
        pass


class Receiver(metaclass=ABCMeta):       # 执行者抽象类
    pass


class Writer(Receiver):
    def translate(self):
        print("正在翻译")

    def write(self):
        print("正在写文档")


class Programmer(Receiver):
    def code(self):
        print("正在码代码")

    def test(self):
        print("正在测试")


class Code_Command(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        if not hasattr(self.receiver, 'code'):
            raise ValueError("他似乎不会敲代码")

    def execute(self):
        self.receiver.code()


class Test_Command(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        if not hasattr(self.receiver, 'test'):
            raise ValueError("他似乎不会测试")

    def execute(self):
        self.receiver.test()


class Write_Command(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        if not hasattr(self.receiver, 'write'):
            raise ValueError("他似乎不会写文档")

    def execute(self):
        self.receiver.write()


class Translate_Command(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        if not hasattr(self.receiver, 'translate'):
            raise ValueError("他似乎不会翻译")

    def execute(self):
        self.receiver.translate()


class Client(object):
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()

if __name__ == '__main__':
    # 作家 与 程序员， 命令的具体执行者
    writer = Writer()
    programmer = Programmer()

    # 写作命令与码代码命令. 命令与执行者 是绑定的.
    write_command = Write_Command(writer)
    code_command = Code_Command(programmer)

    # 委托人, 发布执行命令
    client = Client(write_command)
    client.execute()