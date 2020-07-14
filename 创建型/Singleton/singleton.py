# -*- coding: utf-8 -*-
# @Author  : LG


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):   # 这里用来判断是否存在该类的实例.
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


class MyClass1(Singleton):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':

    c = MyClass1('c_name')  # 可通过子类进行扩展
    print(c.name)

    a = MyClass('a_name')   # 只能存在一个实例
    print(a.name)

    b = MyClass('b_name')
    print(a.name)           # a.name 也会更改，因为是单例模式.
    print(b.name)
    print(c.name)

    b.name = '更改后_name'
    print(a.name)
    print(b.name)
    print(c.name)

    """
    可以看出，同单例子例，只存在一个实例（a,b为MyClass实例，且为同一个实例），
    单例可通过子类进行扩展（c为MyClass1实例，与a、b不同）
    """