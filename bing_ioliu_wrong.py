# _*_ coding:utf-8 _*_
"""
以下代码作废
因为用正则简直太傻了，还是bs4好
"""

import requests
import re
from bs4 import BeautifulSoup


def get_html_text(url):
    """获取指定url的r.text"""

    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("get_html_text出现异常")


def get_pic_url(pic_list, html):
    """使用正则表达式获取图片的url"""
    try:
        # 写出正则表达式
        regex = re.compile(r'data-progressive="http://h1.ioliu.cn/bing/.+?.jpg')
        # 查找所有800x480的url
        ori_pls = regex.findall(html)
        for i in range(len(ori_pls)):
            pls = ori_pls[i].split("/")[-1]
            # 替换成1920x1080
            pls = re.sub("800x600", "1920x1080", pls)
            pls = 'http://h1.ioliu.cn/bing/' + pls
            pic_list.append(pls)
        return pic_list
    except:
        print("get_pic_url出现异常")

def save_pic(pls):
    """将图片保存"""
    pass


def get_pic_title(tls, html):
    """使用bs4方法获取图片标题"""
    pass


def save_title(tls):
    """将图片标题保存在txt文件中"""
    pass


def main():
    start_url = 'https://bing.ioliu.cn/ranking'
    depth = 3
    pic_list = []
    title_list = []
    for i in range(1, depth):
        url = start_url + '?p=' + str(i)
        html = get_html_text(url)
        get_pic_url(pic_list, html)
        save_pic(pic_list)
        get_pic_title(title_list, html)
        save_title(title_list)


if __name__ == '__main__':
    main()