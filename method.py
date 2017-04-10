#coding=utf-8
import urllib2
from bs4 import BeautifulSoup
import time
import user_agents
import random
import os
import sys

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

def is_girl(url):
    content_soup = get_htmlsoup(url)
    author = content_soup.find(id="articleAuthor")
    author_url = author['href']
    #点进每一条的作者页面查看性别
    author_page = get_htmlsoup(author_url)
    sex_type = author_page.find(class_="profile-info-detail")
    if 'class="icon-male"' in str(sex_type):
        return 0
        
def refresh(count_list,list_array,filename):
    tmp_list = count_list[list_array:]
    config=open(str(filename)+'.txt','w')
    config.write('')
    config=open(str(filename)+'.txt','a')
    for i in tmp_list:
        config.write(i)