# -*- coding: UTF-8 -*-

fl = open("./0004.txt")

#单词计数
num = 0
#状态码，1为单词中
a = 0

line = fl.read()
if line:
    for i in line:
        #若在单词中，遇到非字母置a=0
        if a :  
            if not str.isalpha(i):
                a = 0
        #若不在单词中，遇到字母num+=1，a置1
        else:
            if str.isalpha(i):
                a = 1
                num += 1

print(num)

fl.close()
            