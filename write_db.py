"""write_db.py
pymysql 寫操作(inster update delete)
"""
import pymysql

#連接數據庫
db = pymysql.connect(user='root',
                    passwd='123456',
                    database='stu',
                    charset='utf8')

cur = db.cursor()
# 執行sql語句
name = input('Name:')
age = input('Age:')
score = input('Score:')
try:
    # sql 語句值參量可以通過execute傳入
    sql = "insert into class (name, age, score) values (%s,%s,%s)"
    cur.execute(sql, [name,age,score])
    db.commit()  # 同步到數據庫
except Exception as e:
    print(e)
    db.rollback()  # 回滾到沒有commit之前的狀態