# -*- coding: UTF-8 -*-

import random

def _key():
    key = ""
    for i in range(8):
        x = random.randint(0,61)
        if x < 10:
            x = x + 48
        elif x < 36:
            x = x + 55
        else:
            x = x + 61
        key = key + chr(x)
    return key

key_list = []

for i in range(10):
    key_list.append(_key())
