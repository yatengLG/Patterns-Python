# -*- coding: utf-8 -*-
# @Author  : LG


class Expression(object):

    def interpret(self, context):
        if not len(context)%8 == 0:
            raise ValueError("context 必须被8整除")
        nums = len(context)//8
        string = "".join([chr(int(context[i*8:(i+1)*8],2)) for i in range(nums)])
        return string

if __name__ == '__main__':

    context = "010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001"
    expression = Expression()
    string = expression.interpret(context)
    print(string)
