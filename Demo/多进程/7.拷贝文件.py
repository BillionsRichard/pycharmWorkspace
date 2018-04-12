#coding:utf-8

from multiprocessing import Pool
import os
import time

def copyFile(srcFile, dstFile):
    with open(srcFile, 'rb' ) as rf:
        with open(dstFile, 'wb') as wf:
            content = rf.read()
            wf.write(content)


def clearDir(dir):
    if os.path.exists(dir) and os.path.isdir(dir):
        for fname in os.listdir(dir):
            os.remove(os.path.join(dir, fname))

        os.rmdir(dir)

def copyFileOneByOne(srcDir, dstDir):
    clearDir(dstDir)

    if not os.path.exists(dstDir):
        os.makedirs(dstDir)

    for fname in os.listdir(srcDir):
        srcFile = os.path.join(srcDir, fname)
        dstFile = os.path.join(dstDir, fname)
        if os.path.isfile(srcFile):
            copyFile(srcFile, dstFile)
        # else:
        #     copyFileOneByOne(srcFile, dstFile)

def copyFileWithProcess(srcDir, dstDir):
    clearDir(dstDir)

    if not os.path.exists(dstDir):
        os.makedirs(dstDir)

    pp = Pool(8)
    for fname in os.listdir(srcDir):
        srcFile = os.path.join(srcDir, fname)
        dstFile = os.path.join(dstDir, fname)
        if os.path.isfile(srcFile):
            # copyFile(srcFile, dstFile)
            # pp.apply(copyFile, args=(srcFile, dstFile))
            pp.apply_async(copyFile, args=(srcFile, dstFile))

    pp.close()
    pp.join()

if __name__ == '__main__':
    start = time.time()
    srcDir = r'D:\Python\pycharmWorkspace\Demo'
    dstDir = r'D:\Python\pycharmWorkspace\toDemo'

    # copyFileOneByOne(srcDir, dstDir)
    copyFileWithProcess(srcDir, dstDir)
    end = time.time()
    print('copy files finished, time elapsed:%.2f' %(end-start))
