# -*- coding: UTF-8 -*-

import random
"""
num     48-57
upperC  65-90
lowerC  97-112
"""
Length = 10
Num = 5
def create_key():
    key = ""
    for i in range(Length):
        x = random.randint(0,61)
        if x < 10:
            x = x + 48
        elif x < 36:
            x = x + 55
        else:
            x = x + 61
        key = key + chr(x)
    return key
def main():
    key_list = []
    for i in range(Num):
        key_list.append(create_key())
    print(key_list)

main()