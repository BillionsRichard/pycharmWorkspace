# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/3 20:27 
"""
from pprint import pprint as pp

"""
题解：https://leetcode-cn.com/problems/partition-num_array-for-maximum-sum/comments/

对于数组求 最大  最小问题 一般为 动态规划问题

建立一位数组res res[i] 表示：从 0 到 位置 i 子数组的最大和

    对于每一个位置 都可能有 k 种情况：
         ①：只使用它自己位置的数字
         ②：让他保持和前面 1 个数字相同
         ........
         ⑩：让他保持和前面 k - 1 个数字相同
         
    转移方程：
         ①：domainMax = Math.max(domainMax, A[i - j + 1]);
            作用：求它和前面 j - 1 个数字的最大值 为保持相同的数字
            
         ②：res[i] = Math.max(res[i], ((i - j < 0)? 0 : res[i - j])
                                        + j * domainMax);
            作用：求位置 i 的时候 k 种情况 的最大值
            
    边界条件：
         ①：i - j + 1 >= 0
            作用：保证它的前面有 j - 1 个元素
            
         ②：i - j < 0？
            作用：判断 当 前面恰有 j - 1 个元素 且 第 i 个位置 保持和
            前面 j - 1 个数字相同
            
            """


class Solution:
    def maxSumAfterPartitioning(self, A: list, K: int) -> int:
        a_len = len(A)
        res = [0] * a_len

        for i in range(a_len):
            j = 1

            # (i-j + 1 > = 0 保证 A[i] 左边 至少有 j (1 <= j <= K) 个元素
            # A[i-j] A[i-j+1] A[i-j+2]     ...        A[i]
            #        |<----[i-(i-j+1) + 1) = j] 个元素--->|
            while j <= K and i - j + 1 >= 0:
                # 从 A[i] 向左（包含 A[i] ）的连续 j 个元素
                j_left_array = A[i - j + 1:i + 1]

                """
                DP 关键点： 如何从 res[i-j] 到 res[i]
                
                对于 j=1,2,...K 的 K 种方案，分别使用了不同的 res[i-j] 值。
                 
                res[0] ... res[i-j], res[i-j+1] ... res[i]
                                     |<-------j个元素---->|
                """

                domain_max = max(j_left_array)  # j 个元素的最大值
                res_i_minus_j = 0 if i < j else res[i - j]
                cur_res_i = j * domain_max + res_i_minus_j

                if res[i] < cur_res_i:
                    res[i] = cur_res_i

                j += 1

        return res[-1]
