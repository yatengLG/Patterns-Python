# -*- coding: utf-8 -*-
# @Author  : LG


class Information():
    def __init__(self, name, message, date):
        self.name = name
        self.message = message
        self.date = date

    def accept(self, visitor):
        raise NotImplementedError

    def __repr__(self):
        return "{} {} {}".format(self.name, self.message, self.date)


class Visitor():
    def __init__(self, name):
        self.name = name

    def visit(self, information):
        raise NotImplementedError


class News(Information):
    def accept(self, visitor):
        visitor.visit(self)

class Newspaper(Visitor):
    def visit(self, information):
        print('这里是{}, 即将刊登：{}， 内容：{}， 日期：{}'.format(self.name, information.name, information.message, information.date))

class Radio(Visitor):
    def visit(self, information):
        print('这里是{}, 即将播报：{}， 内容：{}， 日期：{}'.format(self.name, information.name, information.message, information.date))

class Media(Visitor):
    def visit(self, information):
        print('这里是{}, 即将发布：{}， 内容：{}， 日期：{}'.format(self.name, information.name, information.message, information.date))

if __name__ == '__main__':
    new1 = News(name='new1', message='我是新闻1', date='2020-1-1')
    new2 = News(name='new2', message='我是新闻2', date='2020-2-2')

    newspaper = Newspaper(name='报社')
    radio = Radio(name='电台')
    media = Media(name='自媒体')

    new1.accept(newspaper)
    new2.accept(media)

