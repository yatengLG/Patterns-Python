# -*- coding: utf-8 -*-
# @Author  : LG

from collections import namedtuple
import random
import time


Monster = namedtuple('monster',['name', 'exp', 'gold'])

class Game:
    exp = 0
    gold = 0
    monsters = [
        Monster('狗头人', 25, 7),
        Monster('地穴狗头人', 25, 17),
        Monster('狗头人首领', 41, 31),
        Monster('豺狼刺客', 41, 26),
        Monster('树魔狂战士', 41, 22),
        Monster('树魔高级牧师', 41, 25),
        Monster('巨狼', 62, 27),
        Monster('食人魔拳手', 41, 23),
        Monster('食人魔魔法师', 62, 43),
        Monster('赛特斯魔法师', 41, 17),
        Monster('赛特斯灵魂盗贼', 83, 31),
        Monster('赛特斯地狱使者', 155, 107),
        Monster('半人马先行者', 41, 24)
    ]

    def save_status(self):
        status = Status(
            self.exp,
            self.gold
        )
        print("存档成功。")
        return status

    def read_status(self, status):
        self.exp = status.exp
        self.gold = status.gold
        print("载入存档成功，当前经验{}，当前金钱{}".format(self.exp, self.gold))

    def play(self, num):
        for i in range(num):
            monster = random.choice(self.monsters)
            print("第{}波，遭遇了[{}]".format(i,monster.name))
            self.exp += monster.exp
            self.gold += monster.gold
            print("     成功击败怪物，获得经验{}，获得金钱{}".format(monster.exp, monster.gold))
            print("     当前经验{}，当前金钱{}".format(self.exp, self.gold))
            time.sleep(1)


class Status:
    def __init__(self, exp, gold):
        self.exp = exp
        self.gold = gold


game = Game()
game.play(5)

status = game.save_status()

del game


game = Game()
game.read_status(status)
game.play(3)
