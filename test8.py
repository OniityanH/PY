import requests
from bs4 import BeautifulSoup



def display(max_page):
    page = 1
    required_search= input("请输入想搜索的bilibili内容：")
    while page < max_page:
        url = 'https://search.bilibili.com/all?keyword=' + str(required_search)
        source_code = requests.get(url)
        print(source_code)
        text1 = source_code.text
        soup = BeautifulSoup(text1)
        for link in soup.findAll('a', {'class': 'title'}):
            href = link.get('href')
            title = link.get('title')
            print(title)
            print(href)
        page += 1

max_page = input("请输入最大页数：")
display(int(max_page))