# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/27 8:52 
"""
"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解题思路：
1）划分后字节数：4 Byte
2）每byte 0~255
3）第1 byte 不能为 0 ---> 不用考虑

/2 5 /5 2 5 /5 /1 1 1 /3 5

2 5 5/ 2 5 5 /1 1 1 /3 5

分割点：不能是0 或者 大于3 的点。


IP地址字符串最短：4位
            最长：12位 4*3
            
字节范围：0~255


"""
from pprint import pprint as pp


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 3 or n > 12:
            return []
        from collections import OrderedDict
        ans = []
        cuted = OrderedDict({i: False for i in range(0, n + 1)})

        def seg(cur):
            """切分函数， cur是当前指针位置。s[:cur]表示已经切分了。

            :param cur:
            :return:
            """
            if cur >= n:
                cuted[cur] = True
                if list(cuted.values()).count(True) == 5:
                    ips = []
                    cuted_index = list(
                        filter(lambda k: cuted[k], cuted.keys()))
                    lst_index = 0
                    for cut_index in cuted_index[1:]:
                        if cuted.get(cut_index):
                            byte = s[lst_index:cut_index]
                            if len(byte) >= 2 and byte.startswith('0'):
                                return
                            ips.append(byte)
                            lst_index = cut_index
                    if all(map(lambda byte: byte <= 255, map(int, ips))):
                        ans.append('.'.join(ips))
                return

            for i in range(cur + 1, cur + 4):
                if i <= n:
                    cur_bytes = int(s[cur:i])
                    if cur_bytes > 255:
                        break

                    cuted[i] = True

                    seg(i)

                    cuted[i] = False

        cuted[0] = True
        seg(0)
        return ans
