#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: William

import os
import sys

import re
import json

import urllib
import urllib2
import cookielib

#from lib.logger_service import logger

class RenRenCrawler(object):
    def __init__(self):
        pass

    def set_cookie(self):
        # 设置cookie
        cookie=cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
        

    def login(self,user,password):
        headers = {
            'Host': 'www.renren.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:10.0.2) Gecko/20100101 Firefox/10.0.2',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-cn,zh;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://www.renren.com/SysHome.do',
            
            #'Cookie': '	anonymid=h6isozwvuzc23e; _r01_=1; depovince=GW; jebecookies=62dbf8ee-61d3-4cb0-a601-471d56b3fedf|||||; JSESSIONID=abc7tS1wmJFuI7tgzNRQt; ick_login=8c605d57-4eb4-4c68-bb84-43021439b654; _de=6BAABC88179758FB4807771A9D9B388C8998821C7EC5F4E2; p=e8e694762f1cee3855fd1dd9f40e01fc1; ap=229731951; t=a8aec455bcd9914e186192384e3e68111; societyguester=a8aec455bcd9914e186192384e3e68111; id=229731951; xnsid=5430b18b; loginfrom=null; feedType=229731951_hot; XNESSESSIONID=abco7ZNraAjiL-rp1ZRQt', # USELESS
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
    
        param = {
            'email': user,
            'password': password,
            'icode': '',
            'origURL': 'http://www.renren.com/home',
            'domain': 'renren.com',
            'key_id': '1',
            '_rtk': 'c59b27d3',
        }
    
        url = 'http://renren.com/ajaxLogin/login' 
        
        postdata=urllib.urlencode(param)
        req = urllib2.Request(url, postdata, headers)
        login_response= urllib2.urlopen(req)

        
        ret =login_response.read()    
        pass

    def get_photo_list(self):
        urls = []

        req=urllib2.urlopen('http://photo.renren.com/photo/238044510/album-830515823?ref=hotnewsfeed&sfet=701&fin=12&fid=20044281766&ff_id=238044510#229731951')
        html =req.read()
        u = re.findall('data-photo="(.*)"',html)
        for url in u:
            urls.append(re.compile("'(.*?)'").findall(url)[1])
        print urls
       

def main():

    if len(sys.argv) != 3:
        sys.exit(1)

    print "start"
    user = sys.argv[1]
    password = sys.argv[2]

    renren = RenRenCrawler()

    # 设置cookie启用
    renren.set_cookie()

    # 登陆人人
    renren.login(user, password)

    ## 获取照片列表
    renren.get_photo_list()

    pass

if __name__ == '__main__':
    main()
