"""write_db.py
pymysql 寫操作(inster update delete)
"""
import pymysql
import re

#連接數據庫
db = pymysql.connect(user='root',
                    passwd='123456',
                    database='dict',
                    charset='utf8')
sql = "insert into words (word, mean) values (%s,%s)"
# 獲取游標
cur = db.cursor()
t = open('dict.txt')
for line in t:
    temp = line.split(' ',1)
    word = temp[0]
    mean = temp[1].strip()
    # print(mean)
    cur.execute(sql, [word, mean])
try:
    # sql 語句值參量可以通過execute傳入
    db.commit()  # 同步到數據庫
except Exception:
    db.rollback()  # 回滾到沒有commit之前的狀態