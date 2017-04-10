#coding=utf-8
import urllib2
from bs4 import BeautifulSoup
import time
import user_agents
import random
import os
import sys

content_soup = get_htmlsoup(url)
author = content_soup.find(id="articleAuthor")
author_url = author['href']
#点进每一条的作者页面查看性别
author_page = get_htmlsoup(author_url)
sex_type = author_page.find(class_="profile-info-detail")
if 'class="icon-female"' in str(sex_type):
    girl_count = girl_count+1
    usr = author_page.find(class_="profile-user-name")
    usr = usr.get_text()

    pic_list = content_soup.find(class_="post-detail gbbcode-content")
    pic_list = pic_list.find_all('noscript')

    count = 1
    #print len(pic_list)
    if len(pic_list) == 0:
        continue
    else:
        for pic in pic_list:

            pic_url = pic['data-image']
            #print pic_url
            picture = url_open(pic_url)
            
            fh = open('result/'+usr+str(count)+'.jpg','w')
            fh.write(picture)
            fh.close()
            
            count = count+1
        sys.stdout.write('     又抓到一个妹子了~，总计抓到'+str(girl_count)+'个'+'\r')
        sys.stdout.flush()








    

