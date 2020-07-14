# -*- coding: utf-8 -*-
# @Author  : LG

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        print("读取{}文件内容".format(filename))
        f = open(filename)
        self.__content = f.read()
        f.close()

    def get_content(self):
        return self.__content

    def set_content(self, content):
        f = open(self.filename, 'w')
        f.write(content)
        self.__content = content
        f.close()


# 远程代理
class ProxyA(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        return self.subj.set_content(content)


# 虚代理
class ProxyB(Subject):
    def __init__(self, filename, subject=None):
        self.filename = filename
        self.subj = subject

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()


# 保护代理
class ProxyC(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError

