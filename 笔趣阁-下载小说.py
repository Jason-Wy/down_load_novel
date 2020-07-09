from bs4 import BeautifulSoup

import requests
import os
import threading

file_path = './file/神魂至尊22.txt'

def check_and_creat_dir(file_url):
    '''
    判断文件是否存在，文件路径不存在则创建文件夹
    :param file_url: 文件路径，包含文件名
    :return:
    '''
    file_gang_list = file_url.split('/')
    if len(file_gang_list)>1:
        [fname,fename] = os.path.split(file_url)
        print(fname,fename)
        if not os.path.exists(fname):
            os.makedirs(fname)
        else:
            return None
        pass
    else:
        return None



def request_html(url):
    print("开始请求地址"+url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # write_to_file(name,response.text)
            response.encoding = 'utf-8'
            return response.text
    except requests.RequestException:
        return None

def write_to_file(name,content):
    file_name = name
    print('写入文件信息'+file_name)
    check_and_creat_dir(file_name)
    with open(file_name,'w',encoding='utf-8') as f:
        # f.write(json.dump(content,ensure_ascii=False))
        f.write(content)


def write_to_continue_file(name,content):
    file_name = name
    # print('文件继续写入'+file_name)
    check_and_creat_dir(file_name)
    with open(file_name,'a',encoding='utf-8') as f:

        f.write(content)


def beautiful_request_url(url):
    '''解析网页详情数据'''
    html = request_html(url)
    soup = BeautifulSoup(html,'lxml')

    #开启多线程把标题与内容写入本地文件

    H_tiltle = soup.find(attrs={"class": "bookname"})
    content_title = H_tiltle.h1.get_text()
    content_title = '\n'+content_title +'\n'
    print(content_title)

    content_word = soup.find(attrs = {"id":"content"})

    content = content_title +''+content_word.get_text('\n')

    write_to_continue_file(file_path, content)

    next_file_list = soup.find_all(attrs={"class": "bottem2","class": "bottem"})
    '''本页数据循环'''
    for next_file_item in next_file_list:
        '''解析出来下一页的地址，开始爬取下一页'''
        for item  in next_file_item.find_all("a"):
            if item.text == '下一章':
                if '.html' in item['href'] and ('http' not in item['href']):
                    url = "https://www.biqubu.com"+item['href']
                    beautiful_request_url(url)
                elif '.html' in item['href'] and ('http' in item['href']):
                    url = item['href']
                    beautiful_request_url(url)
                else:
                    print("爬取完毕")


if __name__ == '__main__':
    '''下载笔趣阁小说使用
        需要第一章的地址
    '''
    # url = "https://www.biqubu.com/book_b215/7129730.html"
    # url = "https://www.biqubu.com/book_1354/820039.html"
    url = 'http://www.biquge.info/35_35964/13146961.html'
    try:

        beautiful_request_url(url)
    except:
        ''''''
        import traceback
        traceback.print_exc()
        beautiful_request_url(url)

