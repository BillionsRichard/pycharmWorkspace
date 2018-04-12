from bs4 import BeautifulSoup
import requests
import csv
from pprint import pprint as pp

def get_all_ver_urls():
    index_url = 'http://support.huawei.com/enterprise/zh/cloud-storage/oceanstor-toolkit-pid-8576706/software'
    response = requests.get(index_url)
    response = requests.get(index_url)

    # print(response.text)
    bs = BeautifulSoup(response.text, 'lxml')
    pp(response.text)
    # attr = {'class':'vrCommonPatchBody',
    #         'id':'vrCommonPatchBody',
    # }
    #
    # ver_list_tag = bs.find_all('div', attrs=attr)[0]
    # pp(dir(ver_list_tag))
    #
    # vers = ver_list_tag.children
    #
    # pp(vers)
    # pp('*'*100)
    # for ver in vers:
    #     pp(ver)
    # all_ver_urls = []

def parse_one_version(ver_url):
    ver_url = 'http://support.huawei.com/enterprise/zh/cloud-storage/oceanstor-toolkit-pid-8576706/' \
              'software/22800652/?idAbsPath=fixnode01%7C7919749%7C7941815%7C9523109%7C8576706'

    response = requests.get(ver_url)

    bs = BeautifulSoup(response.text, 'lxml')
    version = bs.find('title', attrs={}).text.split()[3].strip()

    print('version=', version)
    software_content = bs.find('tbody', attrs={'id':'softListDiv'}).text

    ver_csv_name = version + '.csv'
    csv_file = open(ver_csv_name, 'a', newline='')
    csv_writer = csv.writer(csv_file)
    headers = ['Tool_name_en', 'Tool_name_zh', 'size', 'release_date', 'download']
    csv_writer.writerow(headers)

    nonblank_line_cnt = 0

    for line in software_content.splitlines():
        line = line.strip()
        if not line:
            continue

        nonblank_line_cnt += 1
        if nonblank_line_cnt % 5 == 1:
            new_rec = [line]
        if nonblank_line_cnt % 5 == 2:
            new_rec.append(line)
        if nonblank_line_cnt % 5 == 3:
            new_rec.append(line)
        if nonblank_line_cnt % 5 == 4:
            new_rec.append(line)
        if nonblank_line_cnt % 5 == 0:
            new_rec.append(line)

        if len(new_rec) == 5:
            csv_writer.writerow(new_rec)
            new_rec.clear()

    csv_file.close()


if __name__ == '__main__':
    # parse_one_version(None)
    get_all_ver_urls()