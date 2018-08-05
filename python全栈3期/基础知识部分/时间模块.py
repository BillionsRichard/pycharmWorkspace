import time

print(time.time())

# 结构化时间1（本时区的结构化时间）
# time.localtime() <====> time.localtime(time.time())
cur_time = time.localtime() #默认参数是time.time()

# 格林尼治时间（结构和时间）
gmt_time = time.gmtime()

print('cur_time:%s' % str(cur_time))
print('gmt_time:%s' % str(gmt_time))

print("%s年%s月%s日 星期%s %s时%s分%s秒"
      % (cur_time.tm_year,
         cur_time.tm_mon,
         cur_time.tm_mday,
         cur_time.tm_wday+1,
         cur_time.tm_hour,
         cur_time.tm_min,
         cur_time.tm_sec))


#结构化时间转化为时间戳
print(time.mktime(time.localtime()))

print('结构化时间转换成字符串时间'.center(80, '-'))
print(time.strftime("%Y-%m-%d %X"))
print(time.strftime("%Y-%m-%d %X", time.localtime()))


print('字符串时间转换成结构化时间'.center(80, '-'))
print(time.strptime("2016:12:24:17:50:36", "%Y:%m:%d:%X"))

print(time.asctime())
print(time.ctime())
