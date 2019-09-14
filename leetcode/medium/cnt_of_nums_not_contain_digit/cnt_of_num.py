# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/10 5:48 
"""
from pprint import pprint as pp

def get_cnt_of_nums_not_contain_digit(r:int, n:int)->int:
    cnt_sum = 0
    for i in range(1, r+1):
        if str(n) not in str(i):
            cnt_sum += 1

    return cnt_sum

if __name__ == '__main__':
    print(get_cnt_of_nums_not_contain_digit(20, 2))
    print(get_cnt_of_nums_not_contain_digit(2000000000, 2))
