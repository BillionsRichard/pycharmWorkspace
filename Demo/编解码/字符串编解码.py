#coding:utf-8
import chardet

en_str = "i love china"

#python3.x unicode字符串默认编码是utf16
zh_str = u'我爱中国'

print(type(en_str))
print(type(zh_str))

print(chardet.detect(en_str.encode('utf-8')))
print(chardet.detect(zh_str.encode('utf-16')))