# -*- coding: UTF-8 -*-
import random
import pymysql
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
    db = pymysql.Connect(host='localhost', user='root', password='password', port=3306, db='codes')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS codes(id VARCHAR(100) NOT NULL, code VARCHAR(255) NOT NULL, PRIMARY KEY (id))')
    for i in range(Num):
        code = create_key()
        sql = 'INSERT INTO codes(id, code) values(%s, %s)'
        try:
            cursor.execute(sql, (i+1, code))
            db.commit()
            print('Success!')
        except:
            db.rollback()
    db.close()

if __name__ == '__main__':
    db = pymysql.Connect(host='localhost', user='root', password='password', port=3306)
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE codes DEFAULT CHARACTER SET utf8')
    db.close()
    main()
