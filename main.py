# coding=gbk
# Ŀ�꣺���ظ�Ŀ¼�ı�ֽ����ͼ��
import urllib2
import urllib
import re
import os

# ������ֽ�����ļ���
path = 'd:\\�˰���ֽ'
if not os.path.isdir(path):
    os.makedirs(path)
# Ŀ¼
big_title = []

# ��ҳ��
url = 'http://www.netbian.com/'
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

# ��ҳĿ¼Դ�����ȡ
pat_menu = re.compile('<ul class="menu">(.*?)</a></div>', re.S)
code_menu = re.search(pat_menu, response.read())

# Ŀ¼����
pat_menu_title = re.compile('<a href=".*?" title="(.*?)">', re.S)
menu_title = re.findall(pat_menu_title, code_menu.group(1))
for a_item in menu_title:
    big_title.append(a_item)
    print a_item

# Ŀ¼����
pat_menu_link = re.compile('<a href="(.*?)" title=".*?">', re.S)
menu_link = re.findall(pat_menu_link, code_menu.group(1))

# ����Ŀ¼
j = 0
menu_link=[]
menu_link.append('dongwu')
menu_link.append('meinv')
for b_item in menu_link:
    url_menu = 'http://www.netbian.com/' + b_item
    request_son = urllib2.Request(url_menu, headers=headers)
    response_son = urllib2.urlopen(request_son)
    # ���ÿ��Ŀ¼��ͼƬ���⣬����

    # �����Ŀ¼����
    title_son = []
    pat_title_son = re.compile('<img src=".*?" data-src=".*?" alt="(.*?)"/>', re.S)
    res_title = re.findall(pat_title_son, response_son.read())
    for c_item in res_title:
        title_son.append(c_item)

    # ɸѡ����Ŀ¼����
    pat_code_son = re.compile('<ul>(.*?)</ul>', re.S)
    middle_pattern = urllib2.Request(url_menu, headers=headers)
    middle_response = urllib2.urlopen(middle_pattern)
    res_code_son = re.search(pat_code_son, middle_response.read())

    # �����Ŀ¼���ӣ��ϳɴ�ͼ��ҳ����
    pat_link_son = re.compile('<li><a href="(.*?)" target="_blank"><img', re.S)
    res_link = re.findall(pat_link_son, res_code_son.group(1))
    i = 0
    # ��ʾ����
    print big_title[j]
    for d_item in res_link:
        # ��ô�ͼ��������
        if d_item == 'http://www.mmmwu.com/':
            pass
        else:
            new_link = 'http://www.netbian.com/' + d_item[:-4] + '-1920x1080.htm'
            print new_link
            request_real = urllib2.Request(new_link, headers=headers)
            response_real = urllib2.urlopen(request_real)
            pat_real = re.compile('<img src="(.*?)" alt=".*?"/></td></tr>')

            link_real = re.search(pat_real, response_real.read())
            # ����vip��ֽ
            if link_real:
                fina_link = link_real.group(1)
                # ��������Ŀ¼
                path_final = 'd:\\�˰���ֽ\\' + big_title[j] + '\\'
                if not os.path.isdir(path_final):
                    os.makedirs(path_final)
                path_pic = path_final + title_son[i] + '.jpg'
                f = open(path_pic, 'wb')
                data = urllib.urlopen(fina_link)
                f.write(data.read())
                f.close()
                if not data:
                    print "Download Failed."
            i += 1
    print 'One menu download OK.'
    j += 1