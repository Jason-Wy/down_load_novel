# down_load_novel

前一段时间想看小说，但是找了半天没找到txt文件格式的小说
有时从网上下载的txt小说会出现读着读着一半一半或者中间插入广告文字，整的烦得不行不行
所以想了下，还是自己写了一个代码抓取笔趣阁文章的内容，然后把内容写入TXT文档

if __name__ == '__main__':
    '''下载笔趣阁小说使用
        需要第一章的地址
    '''
    url = "https://www.biqubu.com/book_b215/7129730.html"
这里是第一章的地址，到时自己找到第一章路径，粘贴进来就可以了