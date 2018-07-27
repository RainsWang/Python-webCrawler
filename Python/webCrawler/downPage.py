# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     downpage
   Description :    下载页面，如果出现错误判断错误类型，并重新下载
   Author :       Administrator
   date：          2018/7/17 0017
-------------------------------------------------
   Change Activity:
                   2018/7/17 0017:
-------------------------------------------------
"""
import urllib2
'''
#下载页面html，如果碰到5xx错误重新尝试
def download(url,num_retries = 2):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 当错误为5xx时重新尝试下载
                return download(url, num_retries - 1)
    return html
'''
#给请求添加用户代理
def download(url,user_agent = 'wswp',num_retries = 2):
    print 'Downloading:',url
    headers = {'User-agent':user_agent}
    request = urllib2.Request(url,headers = headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code <600:
                #当错误为5xx时重新尝试下载
                return download(url,user_agent, num_retries - 1)
    return html

if __name__ == "__main__":
    #download('http://httpstat.us/500')
    download('http://www.meetup.com')