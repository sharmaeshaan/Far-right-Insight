import requests
from bs4 import BeautifulSoup
import csv
import time

requests_header = {'user-agent': 'nlp-researcher'}
startlink = 'http://research.calvin.edu/german-propaganda-archive/goebmain.htm'

def get_all(x):
    link = requests.get(x, headers = requests_header)
    link.encoding = 'utf-8'
    soup = BeautifulSoup(link.text, 'html.parser')
    # relevant links are inside list items so get <li> tags first
    list_tags = soup.find_all('li')
    # list for all page links, available to other funcs. w. global
    global rel_page_links
    rel_page_links = list()
    # extract all links from list tags
    for i in list_tags:
        # extract href content inside each atag
        try:
            href_content = ((i.find('a').attrs['href']))
        except:
            pass
        # concatenate href content with main link and add 2 list
        full_link = 'http://research.calvin.edu/german-propaganda-archive/'+href_content
        rel_page_links.append(full_link)
    return rel_page_links

def get_each():
    # set count for generating filenames
    x = 0 
    # iterate over each page link  
    for l in rel_page_links:
        try:
            eachpage = requests.get(l, headers = requests_header)
            eachpage.encoding = 'utf-8'
            soup = BeautifulSoup(eachpage.text, 'html.parser')
            # extract all content within p-tags and place in list
            paras = soup.find_all('p')
            tagslist = list()
            for p in paras:
                tagslist.append(p.contents[0])
            para = list()
            for t in tagslist:
                # time.sleep(0.5)
                # there are tags like <center> and <font> within p-tags, so we append only that content to list which has no tag
                if t.name == None:
                # append all paragraphs of article/speech to a list
                    para.append(t)
                else:
                    pass
            # join all paras in list to form one single article/speech and write it to file
            content = ''.join(para)
            print(content)
            x = x + 1
            fhand = open(str(x)+'.txt', 'w')
            fhand.write(str(content))
            fhand.close()
        except:
            print('Error opening page')
            pass

get_all(startlink)
get_each()
