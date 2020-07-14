# -*- coding: utf-8 -*-
# @Author  : LG


class Template:
    def process_data(self):
        print("处理数据")

    def build_model(self):
        raise NotImplementedError

    def define_lossfn(self):
        raise NotImplementedError

    def sgd_update(self):
        print("梯度下降算法更新模型")

    def train(self):
        self.process_data()
        self.build_model()
        self.define_lossfn()
        self.sgd_update()


class Cnn(Template):
    def build_model(self):
        print("搭建卷积神经网络")

    def define_lossfn(self):
        print("使用focal loss损失函数计算损失")


class Rnn(Template):
    def build_model(self):
        print("搭建循环神经网络")

    def define_lossfn(self):
        print("使用交叉熵计算损失")


if __name__ == '__main__':
    cnn = Cnn()
    cnn.train()

    rnn = Rnn()
    rnn.train()