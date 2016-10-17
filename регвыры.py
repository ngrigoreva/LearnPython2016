#html = open ('хытымыэль на проверку.txt', 'r', encoding = 'utf-8').read()
import urllib.request
import re

def get_author(html):
   #author <p style="text-align: right;" align="right">
   regAuthor = re.compile('<p style="text-align: right;"( align="right")?>.*?([ёА-Яа-я. ]+)</strong>', flags=re.U | re.DOTALL)
   author = regAuthor.search(html)
   if author:
       author_ = author.group(2)
       author = re.sub('\.$', '', author_)
        #author = author_.strip('.') - strip тоже не работает
        return(author)
  else:
        regauthor = re.compile('<p align="right">.*?([ёА-Яа-я. ]+)</strong>', flags=re.U | re.DOTALL)
        author = regauthor.search(html)
        author = re.sub(r'\.$', '', author.group(1))
        #print(author)
        return(author)


def get_header(html):
    #header - это то, что на синем фоне. в некоторых статьях (e.g., 322) есть ещё подзаголовок, его не учитываю
    regHeader = re.compile('<title>(.+) / газета За урожай, Смоленск, п. Шумячи</title>', flags=re.U | re.DOTALL)
    header = regHeader.search(html).group(1)
    return(header)
    #print(header)
    
def get_created(html):
    regDate = re.compile('<span class="date">([0-9/-])</span>', flags=re.U | re.DOTALL)
    date = regDate.search(html).group(1)
    date = re.sub(r'-', '.', date)
    return(date)
    
#def get_topic(html):

#def get_article(html):
    #<a href=".*">(.*) там невозможно разобраться в оформлении :/
    
    
def download_page(pageUrl):
    try:
        page = urllib.request.urlopen('http://www.urogay-smol.ru/')
        html = page.read().decode('utf-8')
        #print(pageUrl, 'ok') - все ok!
    except:
        #print('Error at', pageUrl)
        return
    auth = get_author(html)
    head = get_header(html)
    date = get_created(html)
commonUrl = 'http://www.urogay-smol.ru/?module=articles&action=view&id='
for i in range(135, 736):
    pageUrl = commonUrl + str(i)
    download_page(pageUrl)
