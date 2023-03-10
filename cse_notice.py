import requests
from bs4 import BeautifulSoup as bs

def get_html(url):  
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    return soup

def get_items(data):
    items = data.find_all("item")
    return items

def extract_item(item):
    title = item.find("title").text
    date = item.find("pubdate").text.split()[0]
    link = item.find("link").next_sibling.text.replace("\r", "").replace("\t", "").replace("\n", "")
    author = item.find("author").text
    return {
        'title':title,
        'date':date,
        'link':link,
        'author': author
    }
    
def extract_items(items):
    notice_list = []
    for item in items:
        notice_list.append(extract_item(item))
    return notice_list

def get_notice():
    url = 'https://cse.pusan.ac.kr/bbs/cse/2605/rssList.do?row=30'
    html = get_html(url)
    items = get_items(html)
    notice_list = extract_items(items)
    return notice_list

    
