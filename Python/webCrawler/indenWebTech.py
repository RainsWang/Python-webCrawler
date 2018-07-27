# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     indenwebtech
   Description :    识别网站技术，builtwith识别网站部署技术，whois查找域名相关信息
   Author :       Administrator
   date：          2018/7/17 0017
-------------------------------------------------
   Change Activity:
                   2018/7/17 0017:
-------------------------------------------------
"""
import builtwith
print builtwith.parse('http://192.168.0.141:8080/eagle2/coc/application/controller/frame/LoginUI.action')
import whois
print whois.whois('appspot.com')