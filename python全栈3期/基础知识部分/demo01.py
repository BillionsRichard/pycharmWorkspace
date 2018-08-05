test='username\temail\tpassword\nlaiying\tying@qq.com\tlangying\nlaiying\tying@qq.com\tlaigood'

print(test.expandtabs(20))

print(len('username            '))
print(len('ying@qq.com         '))
print('1'.isnumeric())

print('  \t  '.isspace())

print('the old man and sea'.title())
print('the old man and sea'.istitle())

print('你是风儿我是沙')

test = 'aeiou'
val1 = '12345'

m = str.maketrans(test, val1)
print(m)
print('aabsijwiifjsiis'.translate(m))

#字符串的分割
s = 'partionstions'

print(s.partition('*'))

print(s.rpartition('on'))

print('def'.isidentifier())

import keyword
print('iskeyword?')
print(keyword.iskeyword('def'))