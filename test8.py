import requests
from bs4 import BeautifulSoup



def display(max_page):
    page = 1
    required_search= input("请输入想搜索的bilibili内容：")
    while page < max_page:
        url = 'https://search.bilibili.com/all?keyword=' + str(required_search)
        source_code = requests.get(url)
        text1 = source_code.text
        soup = BeautifulSoup(text1)
        #print(soup)
        for link in soup.findAll('a', {'class': 'title'}):
            href = link.get('href')
            title = link.get('title')
            true_href = "http://"+href[2:]
            print(str(page) + title)
            print(true_href)
            get_single_item(true_href)
            page += 1

def get_single_item(item_url):
    source_code = requests.get(item_url)
    text = source_code.text
    soup = BeautifulSoup(text)
    for items in soup.findAll('div', {'class': 'v_desc report-scroll-module report-wrap-module'}):
        print('\t\t'+items.text)


max_page = input("请输入最大页数：")
display(int(max_page))