# -*- coding: utf-8 -*-
# @Author  : LG


class MyRangeFn(object):
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        if self.start < self.stop:
            value = self.start
            self.start += self.step
            return value
        else:
            raise StopIteration()

    def __iter__(self):
        return self

    def __repr__(self):
        return "MyRange({}, {}, {})".format(self.start, self.stop, self.step)

if __name__ == '__main__':

    a = MyRangeFn(3, 11, 1)

    print(a)
    for i in a:
        print(i)

