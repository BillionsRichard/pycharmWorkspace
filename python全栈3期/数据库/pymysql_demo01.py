# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: pymysql_demo01.py 
@time: 2018/6/17 22:48 
"""
from pprint import pprint as P
import pymysql

conn = pymysql.connect(host="127.0.0.1",
                       port=3306,
                       user='root',
                       passwd='admin',
                       db="lesson_54")

# curor = conn.cursor()
curor = conn.cursor(cursor=pymysql.cursors.DictCursor)

create_tbl_sql = """CREATE TABLE test(
id int ,
name varchar(20)
);"""

# curor.execute(create_tbl_sql)
sql1 = """insert into test (id, name) values
(1, "sam"),
(2, "eva"),
(3, "ada"); """

# curor.execute(sql1)

ret = curor.execute("SELECT * FROM test")
print(ret)
print('fetch one:', curor.fetchone())
curor.scroll(-1, mode='relative')
print('fetch many:', curor.fetchmany(2))

curor.scroll(-2, mode='relative')
print('fetch all:', curor.fetchall())

conn.commit()
conn.close()