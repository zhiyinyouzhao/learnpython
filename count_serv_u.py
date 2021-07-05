# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def get_ser_u_info():
    '''
    爬取ser-U download版本信息
    '''
    version_list = []
    url = 'https://serv-u.soft32.com/old-version/'
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        items1 = soup.find_all(name="div", class_="left")
        item1 = items1[0].find(name='a')
        latest_version = item1.string.strip()
        version_list.append(latest_version)
        items2 = soup.find_all(name="ul", class_="links")
        items_p = items2[0].find_all(name="li")
        for i in items_p:
            old_version = i.a.string.strip()
            version_list.append(old_version)
        return version_list
    except Exception as e:
        print 'get request for version info has an error,error is:%s' %e
        return version_list



def handle_version_list(l):
    '''
    处理爬取的版本信息
    '''
    if l:
        new_l = [s.lower() for s in l if isinstance(s, unicode) == True]
        return new_l
    return []


def write_file(res):
    '''
    写入文件
    '''
    with open ('F:\\result.txt','w+') as f:
        print 'Begin writing...'
        for line in res:
            f.write(str(line))
            f.write('\n')
        print 'End writing...'


if __name__ == '__main__':
    l = get_ser_u_info()
    res = handle_version_list(l)
    write_file(res)