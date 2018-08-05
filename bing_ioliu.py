# _*_ coding:utf-8 _*_

import requests
import re
import time
from bs4 import BeautifulSoup


def header(referer):
    headers = {
        'Host': 'bing.ioliu.cn',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers

def get_html_text(url):
    """获取指定url的r.text"""

    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("get_html_text出现异常")


def parse_html(pic_list, html):
    """使用bs4获取图片的url"""

    try:
        pls = ""
        soup = BeautifulSoup(html, "html.parser")
        for div in soup.find_all(class_="card progressive"):
            pls = div.img['src']
            pic_list.append(pls)           
        return pic_list
    except:
        print("parse_html出错")


def url_transfer(ori_url):
    """修改800x600的地址为1920x1080"""

    url = re.sub("400x240", "1920x1080", ori_url)
    return url


def get_pic_content(url):
    """获取图片内容"""
    try:
        r = requests.get(url, headers=header(url))
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except:
        print("get_html_text出现异常")


def save_pic(pls):
    """将图片保存在当前目录的pic文件夹内"""
    
    for ori_url in pls:
        # 修改url
        url = url_transfer(ori_url)
        print(url)
        '''get_pic_content(url)
        #获取文件名
        filename = url.split("/")[-1]
        path = "D:\\QMDownload\\bing\\pic\\{}".format(filename)
        with open(path, 'wb') as jpg:
            jpg.write(r.content)
            time.sleep(0.5)
        '''

def main():
    start_url = 'https://bing.ioliu.cn/ranking'
    depth = 3
    pic_list = []
    for i in range(1, depth):
        url = start_url + '?p=' + str(i)
        html = get_html_text(url)
        parse_html(pic_list, html)
        save_pic(pic_list)


if __name__ == '__main__':
    main()