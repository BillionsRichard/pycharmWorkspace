# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/19 22:50 
"""
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from utils.bsearch.bisearch import bsearch


class Solution:
    """a+b+c = 0
    -(a+b) = c

    超时的解题思路：
    1、将原数组排序：
    2、使用 itertools.combinations(l, 2) 然后用二分查找法查找 c.

    时间复杂度为 Cn2 = N^2 * logN==>超时
    """

    def threeSum(self, nums: list) -> list:
        num_len = len(nums)
        if num_len < 3 or num_len == 3 and sum(nums) != 0:
            return []

        if num_len == 3 and sum(nums) == 0:
            return [nums]

        ans = []
        import itertools
        """
        one) c = -(a + b) 不在 nums 中：
          a +b + c = 0
          1) 如果 a + b == 0 ===> c = 0
                i)  a == 0, b == 0  c== 0 nums.count(0) >=3 才行
                ii) a = -b !=0  c== 0
                
          2) 如果 a+b != 0 ===> c =-(a+b) != 0
            
        two):
            c = -(a + b) 在 nums 中：
            pass
            
        """
        new_list = sorted(nums)
        inds = list(range(len(new_list)))
        taken_tuple_set = set()
        Z = None
        for i in inds:
            if new_list[i] >= 0:
                Z = i
                break

        print('Z===>', Z)
        for i, j in itertools.combinations(inds, 2):
            # i < j
            c = -(new_list[i] + new_list[j])
            if c >= 0:
                k = bsearch(c, new_list[Z:])
            else:
                k = bsearch(c, new_list[:Z])

            if k == -1:
                continue
            else:
                # ans.append((i,j,k))
                if k > j and (new_list[i], new_list[j], new_list[k]) not in \
                        taken_tuple_set:
                    ans.append([new_list[i], new_list[j], new_list[k]])
                    taken_tuple_set.add(
                        (new_list[i], new_list[j], new_list[k]))
                elif k < i and (new_list[k], new_list[i], new_list[j]) not \
                        in taken_tuple_set:
                    ans.append([new_list[k], new_list[i], new_list[j]])
                    taken_tuple_set.add((new_list[k], new_list[i], new_list[
                        j]))
                elif i < k < j and (new_list[i], new_list[k], new_list[j]) \
                        not in taken_tuple_set:
                    ans.append([new_list[i], new_list[k], new_list[j]])
                    taken_tuple_set.add(
                        (new_list[i], new_list[k], new_list[j]))
                elif k == i:
                    if new_list[i+1] == new_list[i] and i+1 != j:
                        t = new_list[i], new_list[i+1], new_list[j]
                        if t not in taken_tuple_set:
                            ans.append(list(t))
                            taken_tuple_set.add(t)
                    if new_list[i-1] == new_list[i]:
                        t = new_list[i-1], new_list[i], new_list[j]
                        if t not in taken_tuple_set:
                            ans.append(list(t))

        return ans
