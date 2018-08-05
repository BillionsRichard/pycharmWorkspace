# coding utf-8
import hashlib
import os
from pprint import pprint as pp

QIAN_FENG_ARGS = {
    '千锋python入门教程：': '',
    '千锋python视频教程：': '',
    '千锋python教程入门到精通：': '',
    '千锋python编程教程：': '',
    '千锋python视频教程：': '',
    '千锋Python教程：': '',
    '千锋Python教程视频：': '',
    '千锋Python开发教程：': '',
    '千锋Python开发视频教程：': '',
    '千锋Python零基础入门教程：': '',
    '千锋Python爬虫入门教程：': '',
    '千锋python全栈开发视频教程：': '',
    '千锋Python入门教程：': '',
    '千锋Python实战视频教程：': '',
    '千锋Python编程入门教程：': '',
    '千锋Python基础教程：': '',
    '千锋Python基础视频教程：': '',
    '千锋Python视频教程：': '',
    '千锋Python编程视频教程：': '',
    '千锋Python项目实战教程：': '',
    '千锋python小项目实战教程：': '',
    '千锋Python自学视频教程：': '',
    '千锋python免费视频教程：': '',
    '千锋python前端教程：': '',
    '千锋python前端视频教程：': '',
    '千锋python入门教程视频：': '',
    '千锋python视频教程：': '',
    '千锋python教程：': '',

}

PYTHON_QUAN_ZHAN_ARGS = {
     'python全栈s3':'',
    'python s3 ':'',
    '.ev4.mp4':'.ev4',
    '.mp4': '.ev4',
    'fullstack': '',
    'python全栈3 ': '',
}

QIAN_FENG_DIRS = []


def batch_rename_files(dir, kwargs):
    os.chdir(dir)
    sub_dirs = []
    files = os.listdir(dir)
    for f in files:
        if not os.path.isfile(f):
            sub_dirs.append(os.path.join(dir, f))
            continue

        old_name = f
        new_name = f
        replaced = False
        for kw in kwargs:
            new_str = kwargs.get(kw, '')
            if kw in f:
                replaced = True
                new_name = new_name.replace(kw, new_str)
            elif '：' in f:
                fstSpaceIdx = f.find('：')
                new_name = f[fstSpaceIdx + 1:].strip()
                replaced = True

        if replaced:
            try:
                os.rename(old_name, new_name)
            except:
                pass
            else:
                print('rename [%s] to [%s] success.' % (old_name, new_name))

    for sub_dir in sub_dirs:
        batch_rename_files(sub_dir, kwargs)


def silent_remove(file):
    try:
        os.remove(file)
    except:
        print('cudir:%s, remove target file:%s' % (os.getcwd(), file))
        pass


def remove_dup_file(dir):
    """删除指定目录下的重复文件（递归删除）

    :param dir:
    :return:
    """
    items = os.listdir(dir)
    file_map = dict()

    os.chdir(dir)

    dirs = []
    for f in items:
        if os.path.isfile(f):
            md5_digest, _ = hash_file(f)
            file_map.setdefault(md5_digest, [])
            file_map[md5_digest].append(f)
        else:
            dirs.append(os.path.join(dir, f))

    for md5_digest in file_map:
        fs = file_map.get(md5_digest)
        if len(fs) > 1:
            fs.sort(key=len)

            for f in fs[1:]:
                print('removing.....%s ' % os.path.join(os.getcwd(), f))
                silent_remove(f)

    for sub_dir in dirs:
        remove_dup_file(sub_dir)


def hash_file(file):
    """计算文件的hash值

    :param file:
    :return:md5digest, sha1digest
    """

    if not os.path.isfile(file):
        return '', ''

    # BUF_SIZE is totally arbitrary, change for your app!
    BUF_SIZE = 1024 * 1024  # lets read stuff in 1MB chunks!
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)

    # print('%s--%s---%s' % (file, md5.hexdigest(), sha1.hexdigest()))
    return md5.hexdigest(), sha1.hexdigest()


if __name__ == '__main__':
    top_dir = 'D:\Python\LNH-视频python全栈3期104天视频'
    # dirs = os.listdir('.')
    #
    #
    # for tmpDir in dirs:
    #     if not os.path.isdir(tmpDir):
    #         continue
    #
    #     os.chdir(tmpDir)
    batch_rename_files(top_dir, PYTHON_QUAN_ZHAN_ARGS)
    #     os.chdir('..')
    # path = r'F:\月入30K的Python大牛教你如何学习Python'
    # remove_dup_file(path)
