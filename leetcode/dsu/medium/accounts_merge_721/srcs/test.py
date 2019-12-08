# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/12/7 16:06
"""
from pprint import pprint as pp

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]

from collections import defaultdict

name_dict = defaultdict(int)
name_emails_dict = defaultdict(set)

for name, *emails in accounts:
    if name not in name_emails_dict:
        name_emails_dict[name] = set(emails)
        name_dict[name] += 1
    else:
        if name_emails_dict[name] & set(emails):
            name_emails_dict[name] = name_emails_dict[name] | set(emails)
        else:
            same_name_key = '%s_%d' % (name, name_dict[name])
            name_emails_dict[same_name_key] = set(emails)
            name_dict[name] += 1

print('name_dict')
pp(name_dict)
print('name_emails_dict')
pp(name_emails_dict)

ans = []
for name in name_emails_dict:
    record = [name.split('_')[0]]
    emails = list(name_emails_dict.get(name))
    emails.sort()
    record.extend(emails)
    ans.append(record)

pp(ans)

