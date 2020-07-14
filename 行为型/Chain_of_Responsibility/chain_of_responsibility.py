# -*- coding: utf-8 -*-
# @Author  : LG

from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, days):
        pass


class Project_Director_Handler(Handler):
    def __init__(self):
        self.successor = Department_Manager_Handler()

    def handle_leave(self, days):
        if days <= 3:
            print("项目主管批准{}天假期".format(days))
            return True
        else:
            print("项目主管无权批假")
            return self.successor.handle_leave(days)


class Department_Manager_Handler(Handler):
    def __init__(self):
        self.successor = General_Manager_Handler()

    def handle_leave(self, day):
        if day <= 7:
            print("部门经理批准{}天假".format(day))
            return True
        else:
            print("部门经理无权准假")
            return self.successor.handle_leave(day)


class General_Manager_Handler(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理批准{}天假".format(day))
            return True
        else:
            print("总经理已批准你离职")
            return False


if __name__ == '__main__':

    days = 9
    handler = Project_Director_Handler()
    handler.handle_leave(days)