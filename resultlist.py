#coding=utf-8
import method
import config


fh = open('url_list.txt','a')
start_page = config.page

count = 0
for page in range(start_page,100):

    group_url = 'http://www.guokr.com/group/48/?page='+str(page)
    html_soup = method.get_htmlsoup(group_url)
    links = html_soup.find_all(class_="title-link")

    page_url_list= []
    for i in links:
        url = i['href']
        if method.is_girl(url) != 0:
            page_url_list.append(url)
    
    for i in page_url_list:
        fh.write(i+'\n')
        count = count+1
    print '完成第'+str(page)+'页'
    (open('config.py','w')).write('page = '+str(page+1))
            
fh.close()

print '总计抓到'+str(count)+'人'