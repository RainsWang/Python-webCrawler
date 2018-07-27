# -*- coding: utf-8 -*-
"""
--------------------------------------------------------
File Name：     Idcrawler
Author :       Administrator
date：          2018/7/17 0017
Description :   依据id来进行遍历
--------------------------------------------------------
Change Activity:2018/7/17 0017:
--------------------------------------------------------
"""
import itertools
from downPage import download
#itertools.count生成一个迭代器，步长为1
#该函数如果碰到id不连续的网站则会出问题
'''
for page in itertools.count(1):
    url = 'http://example.webscraping.com/places/default/view/-%d'% page
    html = download(url)
    if html is None:
        break
    else:
        pass
'''
max_errors = 5
num_errors = 0
for page in itertools.count(1):
    url = 'http://example.webscraping.com/places/default/view/-%d' % page
    html = download(url)
    if html is None:
        num_errors+=1
        if num_errors == max_errors:
            break
    else:
        num_errors = 0