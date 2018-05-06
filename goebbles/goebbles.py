import requests
from bs4 import BeautifulSoup
import time

requests_header = {'user-agent': 'nlp-researcher'}

def goeb_all(x):
    link = requests.get(x)
    link.encoding = 'utf-8'
    soup = BeautifulSoup(link.text, 'html.parser')
    # relevant links are inside list items so get <li> tags first
    list_tags = soup.find_all('li')
    rel_page_links = list()
    # extract all links from list tags
    for i in list_tags:
        # extract href content inside each atag
        try:
            href_content = ((i.find('a').attrs['href']))
        except:
            pass
        full_link = 'http://research.calvin.edu/german-propaganda-archive/'+href_content
        rel_page_links.append(full_link)
    return print(rel_page_links)
    # atags = list_tags.find_all('a')
    # for i in atags:
    #     print(i)


goeb_all('http://research.calvin.edu/german-propaganda-archive/goebmain.htm')