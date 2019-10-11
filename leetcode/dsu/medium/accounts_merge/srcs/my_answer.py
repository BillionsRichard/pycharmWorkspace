# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/7 22:41 
"""

class Solution:

    def accountsMerge(self, accounts: list) -> list:
        ans = []
        import itertools

        for name, emails in itertools.groupby(accounts, key=lambda e: e[0]):
            # print('name->', name)
            emails = list(emails)
            merged = []
            for email_list1 in emails:
                for email_list2 in emails:
                    # print('email_list1', email_list1)
                    # print('email_list2', email_list2)
                    if email_list1[1:] != email_list2[1:] and set(
                            email_list1[1:]) & set(email_list2[1:])\
                            and email_list1 not in merged and email_list2 \
                            not in merged:
                        merged.append(email_list1)
                        merged.append(email_list2)
                        m = set(email_list1[1:]) | set(email_list2[1:])
                        m_l = list(m)
                        m_l.sort()
                        m_l.insert(0, name)
                        if m_l not in ans:
                            ans.append(m_l)

            for email_list in emails:
                if email_list not in merged:
                    name, emails = email_list[0], sorted(list(set(email_list[
                                                              1:])))
                    emails.insert(0, name)
                    if emails not in ans:
                        ans.append(emails)

            # print(ans)

        return ans





if __name__ == '__main__':
    from pprint import pprint as pp
    s = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]
    ans = s.accountsMerge(accounts)
    pp(ans)
    # s1 = set(['johnsmith@mail.com', 'john00@mail.com'])
    # s2 =  set(['johnsmith@mail.com', 'john_newyork@mail.com'])
    # print(s1 & s2)