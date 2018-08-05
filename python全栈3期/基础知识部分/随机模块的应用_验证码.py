#coding:utf-8

import random
import string


def verify_code():
    codes = []
    for i in range(5):
        num_code = random.randint(0,9)
        chr_idx = random.randint(0, 25)
        chr_code = string.ascii_lowercase[chr_idx]
        sel_code = random.choice([str(num_code), chr_code])
        codes.append(sel_code)

    return ''.join(codes)

print(verify_code())
