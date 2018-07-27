# -*- coding: utf-8 -*-
"""
--------------------------------------------------------
File Name：     firstcrawler
Author :       Administrator
date：          2018/7/17 0017
Description :   第一个网站地图爬虫,依赖于网站地图
--------------------------------------------------------
Change Activity:2018/7/17 0017:
--------------------------------------------------------
"""
import re,time
from downPage import download
def crawl_sitemap(url):
    #下载网站地图文件
    sitemap = download(url)
    #提取网站地图文件链接
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    #下载每一个link
    for link in links:
        html = download(link)

if __name__ == '__main__':
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')