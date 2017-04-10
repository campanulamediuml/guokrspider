#coding=utf-8
import urllib2
from bs4 import BeautifulSoup
import time
import user_agents
import random
import os

def get_htmlsoup(site):

    site_page = url_open(site)
    soup = BeautifulSoup(site_page, 'html.parser')
    return soup
#获取经过beautifusoup处理过后的结果
def url_open(site):
    randomarry = random.choice(user_agents.user_agent_list)
#随机挑选一个user_agent文件头
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':randomarry
    }
#手动添加完整一套文件头，假装是不同的浏览器进行访问
    data = None

    requests = urllib2.Request(site,data,headers)
    response = urllib2.urlopen(requests)
    site_page = response.read()
    return site_page

try:
    os.mkdir('result')
except:
    print 'dir exists... begin to scrap'

girl_count = 0
page = 1
while True:

    group_url = 'http://www.guokr.com/group/48/?page='+str(page)
    html_soup = get_htmlsoup(group_url)
    links = html_soup.find_all(class_="title-link")

    page_url_list= []
    for i in links:
        url = i['href']#逐条帖子访问
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
            for pic in pic_list:
                pic_url = pic['data-image']
                picture = url_open(pic_url)
                try:
                    os.makedirs('result/'+usr)
                except:
                    fh = open('result/'+usr+'/'+str(count)+'.jpg','w')
                    fh.write(picture)
                    fh.close()
                count = count+1
            print '     又抓到一个妹子了~，总计抓到'+str(girl_count)+'个'+'\r'


        else:
            continue


    page = page+1





    

