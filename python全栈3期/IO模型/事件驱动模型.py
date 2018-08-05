# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 事件驱动模型.py 
@time: 2018/6/2 10:43 
"""
from pprint import pprint as P

"""
协程：遇到IO操作就切换。
但什么时候切回去呢？ 怎么确定IO操作完成了？？

事件驱动编程思想：
    一种编程范式：
    
    事件队列:
    注册：

用户空间与内核空间：
    内核态：
    用户态：
    OS采用虚拟存储器，对32位OS，寻址空间为4G(2^32).
    OS的核心是内核，独立于普通的应用程序，可以访问受保护的内存空间，也有访问底层硬件设备的权限。
    
    为了保证用户进程不能直接操作内核（Kernel），保证内核的安全，OS将虚拟地址空间划分为两部分：
    一部分是内核空间；一部分是用户空间。
    
    
进程切换：

文件描述符

缓存IO

触发机制：
    1、水平触发。-----电平水位为高电位或地电位时持续发生某件事。
    2、边缘触发。-----电平水位变化时发生某件事。
    
IO多路复用：
1）select
2）poll
3）epoll
 
"""