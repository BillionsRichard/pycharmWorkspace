# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/8 9:37 
"""


def get_remove_len(node_pth: list) -> int:
    reversed_pth = list(reversed(node_pth))
    pth_len = 0
    lst_node = reversed_pth[0]
    for node in reversed_pth[1:]:
        pth_len += (lst_node - node - 1)
        lst_node = node

    return pth_len


def remove_n_chars_to_be_sub_str(s, p):
    if p in s:
        return 0

    matrix = []
    s_len = len(s)
    for sub_chr in p:
        matrix.append([i for i in range(s_len) if s[i] == sub_chr])

    p_len = len(p)
    first_nodes = matrix[0]
    all_pths = []
    for f_node in first_nodes:
        pths = []
        cur_node = f_node
        pths.append(cur_node)
        for i in range(1, p_len):
            next_nodes = matrix[i]
            next_nodes = list(filter(lambda n: n > cur_node, next_nodes))
            if next_nodes:
                pths.append(next_nodes[0])
                cur_node = next_nodes[0]

        if len(pths) == p_len:
            all_pths.append(pths)

    all_pths.sort(key=get_remove_len)
    return get_remove_len(all_pths[0])


if __name__ == '__main__':
    s = 'facbacdefacbabdfcadef'
    p = 'fdef'
    print(remove_n_chars_to_be_sub_str(s, p))
