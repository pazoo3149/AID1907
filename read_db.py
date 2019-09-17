"""read_db.py
pymysql 讀操作演示(select)
"""
import pymysql

#連接數據庫
db = pymysql.connect(user='root',
                    passwd='123456',
                    database='stu',
                    charset='utf8')
# 獲取游標
cur = db.cursor()

# 獲取數據
sql = "select name,hobby from interest where hobby = 'draw';"

cur.execute(sql)
# # 可以直接遍歷游標
# for i in cur:
#     print(i)

# # 獲取所有查詢結果
# all_row = cur.fetchall()
# print(all_row)  # 查詢不到 返回空元祖

# 獲取多個查詢結果
many_row = cur.fetchmany(1)
print(many_row)

# 獲取一個查詢結果
one_row = cur.fetchone()
print(one_row)

cur.close()
db.close()