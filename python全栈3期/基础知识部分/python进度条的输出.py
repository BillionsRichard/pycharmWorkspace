import time
import sys

"""
第0次输出：#%1
第1次输出：##%2      退: len("%1")格
第2次输出：###%3     退：len("%2")格
...

每次退格数目：len((%%%s) % (i+1)) * 'b'

"""
def left_progess_bar():
    for i in range(100):
        heading = (i + 1) * '#'
        sys.stdout.write('\r%s%%%s' % (heading, (i + 1))) # 输出：#%1
        sys.stdout.flush()
        time.sleep(0.5)


def center_progress_bar():
    for i in range(100):
        heading = (i + 1) * '#'
        progress_percent = '%%%s' %(i+1)
        progress_bar = progress_percent.center(len(progress_percent) + (i+1), '#')
        sys.stdout.write('\r%s' % progress_bar) # 输出：#%1
        sys.stdout.flush()
        time.sleep(0.5)


left_progess_bar()
