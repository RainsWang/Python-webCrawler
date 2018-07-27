# -*- coding: utf-8 -*-
"""
--------------------------------------------------------
File Name：     Linkcrawler
Author :       Administrator
date：          2018/7/18 0018
Description :链接爬虫，通过正则表达式确定哪些需要下载，目前没有出现下载成功的情况；考虑网络问题
--------------------------------------------------------
Change Activity:2018/7/18 0018:
--------------------------------------------------------
"""
import re,time
from downPage import download
def link_crawler(seed_url,link_regex):
    '''从给定的url中抓取与link_regex匹配的链接'''
    crawl_queue = [seed_url]
    #seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            print link
            if re.match(link_regex,link):
                crawl_queue.append(seed_url+link)
def get_links(html):
    '''Return a list of links from html'''
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)
if __name__ == '__main__':
    link_crawler('http://example.webscraping.com/','/(index|view)')
