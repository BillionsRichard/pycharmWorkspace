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

    时间复杂度为 Cn2 = N^2 * logN
    """

    def threeSum(self, nums: list) -> list:
        from collections import defaultdict
        num_len = len(nums)
        if num_len < 3 or num_len == 3 and sum(nums) != 0:
            return []

        if num_len == 3 and sum(nums) == 0:
            return [nums]

        sum_dict = defaultdict(list)
        for i in range(num_len):
            sum_dict[nums[i]].append(i)

        ans = []
        set_list = []
        for i in range(num_len-3):
            for j in range(i+1, num_len):
                c = -(nums[i] + nums[j])
                if c in sum_dict:
                    ks = sum_dict.get(c)
                    ks = list(filter(lambda k : k >j, ks))
                    if ks:
                        t = sorted([nums[i], nums[j], nums[ks[0]]])

                        if set(t) not in set_list:

                            ans.append(t)
                            set_list.append(set(t))

        return ans

