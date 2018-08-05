import re

"""
r'xxx'======>’xxx'是一个原生字符串（raw String)，不做任何转义。


元字符：
. 匹配非换行字符。


重复匹配：
1）* 重复0到无穷次
2) + 重复1到无穷次
3) ?  0次或者1次

4){} 
    {0,}    ==  *
    {1,}    ==  +
    {0,1}   ==  ?
    {6}

5) ?可以改变贪婪匹配符的属性（变成惰性匹配）

6) [] 字符集，其中只有三个特殊字符：
                （1）-
                （2）^
                 (3) \
    []中包含字符串， eg：a[x.y*.?] 
    []中包含中线字符，eg: a[A-Z6-9]  范围匹配
    []中包含^字符，eg: a[^A-Z6-9]  取反,必须放在首部，否则表示普通字符
    
注意：[]中的元字符视作普通字符匹配（丢失元字符属性）


转义字符：
1）\d == [0-9] 匹配任何十进制数字
2）\D == [^0-9] 匹配任何非十进制数字
3) \s 匹配任何空白字符
4）\S 匹配任何非空白字符
5）\w == [a-zA-Z1-9] 匹配任何字母数字字符
6) \W == [^a-zA-Z1-9] 匹配任何非字母数字字符
7）\b 字符边界

分组匹配：()
1) re.findall(r'www\.(baidu|163|qq)\.com', 'www.baidu.com')
    baidu
    
2) re.findall(r'www\.(?:baidu|163|qq)\.com', 'www.baidu.com')
    www.baidu.com
    


"""
print(re.findall('a..x$', 'adsxlfajsxijfiwjfasdx'))
print(re.findall('d*', 'adsxlfddddddddddajsxijfiwjfasdx'))
print(re.findall('d+', 'adsxlfddddddddddajsxijfiwjfasdx'))
print(re.findall('alex*', 'aled'))

print(re.findall('alex?', 'aledfsg'))
print(re.findall('alex?', 'alexxxxdfsg'))
print('贪婪匹配属性被？改变'.center(100, '-'))
print(re.findall('alex+?', 'alexxxxdfsg'))
print(re.findall('alex+', 'alexxxxdfsg'))


print(re.findall('a[xy]', 'axdfsaxysjfisay'))
print('元字符属性被[]改变'.center(100, '-'))
print(re.findall('a[z*y?]', 'abcdea*ybccazzbcaba?ccaz*y'))
print(re.findall('a[^A-Z6-9]', 'abcdea*aZjfisijfa5...a7'))
print(re.findall('a[A-Z^6-9]', 'abcdea*aZjfisijfa5...a7a^'))

print(re.findall('\([^()]*\)', '12*((3+4)-5)*(2+8)*9'))

print(re.findall('www\.', 'www.baidu.com www.sina.com'))

print('\\b的用法'.center(120, '-'))
print(re.findall('I\s+', 'I am LIST'))
print(re.findall('I\b', 'hello I am LIST'))
print(re.findall('I\\b', 'hello I am LIST'))
print(re.findall(r'\bI\b', 'hello I am LIST LI'))


print('转义\\的用法'.center(120, '-'))
print(re.findall('c\\\\la', 'c\laaac\\\\l'))
print(re.findall(r'c\\la', 'c\laaac\\\\l'))

print('转义\\的用法'.center(120, '-'))
print(re.findall(r'ka|b', 'kabbk|b'))
print(re.findall(r'ka|bc', 'kabbk|babc'))
print(re.findall(r'abc+', 'abcccabcab'))
print(re.findall(r'abc+', 'abcccabcab'))

print('分组"()"的用法'.center(120, '-'))
print(re.findall(r'(abc)+', 'abcabcabcdef'))
print(re.findall(r'(?:abc)+', 'abcabcabcdef'))
print(re.findall(r'(abc)*', 'abcabcabcdef'))
print(re.findall(r'(?:abc)*', 'abcabcabcdef'))

print('分组"()"命名<>的用法'.center(120, '-'))
print(re.search(r'(?P<name>[a-zA-Z]*)', 'alex3645sam123').group('name'))
print(re.search(r'(?P<name>[a-zA-Z]*)(?P<age>[0-9]*)', 'alex3645sam123').group('name'))
print(re.search(r'(?P<name>[a-zA-Z]*)(?P<age>[0-9]*)', 'alex3645sam123').group('age'))

print('分组"()"命名迭代的用法'.center(120, '-'))
itr = re.finditer(r'(?P<name>[a-zA-Z]*)(?P<age>[0-9]*)', 'alex3645sam123')
for i in itr :
    print('%s--->%s' %(i.group('name'), i.group('age')))

print('管道符"|"的用法'.center(120, '-'))
print(re.search(r'abc(sam|eva)', 'abcsam').group())
print(re.search(r'abc(sam|eva)', 'abceva').group())
print(re.search(r'abc(sam|eva)', 'abcsameva').group())

s = '12+(34*6+2-5*(2-1)+(4*4+4))'
print(re.findall(r'\([^()]+\)',s))