# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: hmm_seg.py 
@time: 2019/1/1 9:23 
"""
from pprint import pprint as pp
from hmm_train import get_word_ch

mod_path = './data/model_file.txt'

# . 1. 加载模型参数
#  1.1 用来存储模型参数
STATUS_NUM = 4

# 初始概率
pi = [0.0 for col in range(STATUS_NUM)]

A = [[0.0 for col in range(STATUS_NUM)] for row in range(STATUS_NUM)]


f = open(mod_path, 'r', encoding="utf8")
# 读取文件第一行作为初始概率
pi_tokens = f.readline().split()
for i in range(STATUS_NUM):
    pi[i] = float(pi_tokens[i])

# pp(pi)

# 继续读取下4行作为状态转移概率
for i in range(STATUS_NUM):
    A_i_tokens = f.readline().split()
    for j in range(STATUS_NUM):
        A[i][j] = float(A_i_tokens[j])
# pp(A)

# 读取后四行，填充矩阵B（发射矩阵B）S（BMES）->O（中文每个字）
B = [dict() for col in range(STATUS_NUM)]
for i in range(STATUS_NUM):
    B_i_tokens = f.readline().split()
    token_num = len(B_i_tokens)
    j = 0
    while j + 1 < token_num:
        B[i][B_i_tokens[j]] = float(B_i_tokens[j + 1])
        j += 2
f.close()

# pp(B)
# 2. 实现维特比算法（预测最优路径）
ch_num = 10
# init
status_matrix = [[(0.0, 0) for col in range(ch_num)]
                 for st in range(STATUS_NUM)]
ch = "我在八斗学习大数据"
ch_list = get_word_ch(ch)
pp(ch_list)

for i in ch_list:
    if ch_list[0] in B[i]:
        cur_B = B[i][ch_list[0]]
    else:
        cur_B = -1000000.0

    if pi[i] == 0.0:
        cur_pi = -1000000.0
    else:
        cur_pi = pi[i]

    status_matrix[i][0][0] = cur_pi + cur_B
    status_matrix[i][0][1] = i

# pp(status_matrix)

for i in range(0, ch_num):
    for j in range(STATUS_NUM):
        max_p = None
        max_status = None
        for k in range(STATUS_NUM):
            cur_A = A[k][j]
            if cur_A == 0.0:
                cur_A = -1000000.0
            cur_p = status_matrix[k][i - 1][0] + cur_A
            if max_p is None or max_p < cur_p:
                max_p = cur_p
                max_status = k
        if ch_list[i] in B[j]:
            cur_B = B[j][ch_list[i]]
        else:
            cur_B = -1000000.0

        status_matrix[j][i][0] = max_p + cur_B
        status_matrix[j][i][1] = max_status

# get max p path
max_end_p = None
max_end_status = None

for i in range(STATUS_NUM):
    if max_end_p is None or status_matrix[i][i][ch_num - 1][0] > max_end_p:
        max_end_p = status_matrix[i][ch_num - 1][0]
        max_end_status = i

best_status_lst = [0 for ch in range(ch_num)]
best_status_lst[ch_num - 1] = max_end_status

c = ch_num - 1
cur_best_status = max_end_status
while c > 0:
    pre_best_status = status_matrix[cur_best_status][c][1]
    best_status_lst[c - 1] = pre_best_status
    cur_best_status = pre_best_status

    c -= 1

print(ch)
print(best_status_lst)
