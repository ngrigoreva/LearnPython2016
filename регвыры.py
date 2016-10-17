html = open ('хытымыэль на проверку.txt', 'r', encoding = 'utf-8').read()

import re

def get_year(html):
    #author <p style="text-align: right;" align="right">
    regAuthor = re.compile('<p style="text-align: right;"( align="right")?>.*?([ёА-Яа-я. ]+)</strong>', flags=re.U | re.DOTALL)
    author = regAuthor.search(html)
    if author:
        author_ = author.group(2)
        author = re.sub('\.$', '', author_)
        #author = author_.strip('.') - strip тоже не работает
        print(author)
    else:
        regauthor = re.compile('<p align="right">.*?([ёА-Яа-я. ]+)</strong>', flags=re.U | re.DOTALL)
        author = regauthor.search(html)
        author = re.sub(r'\.$', '', author.group(1))
        print(author)


def get_header(html):
    #header - это то, что на синем фоне. в некоторых статьях (e.g., 322) есть ещё подзаголовок, его не учитываю
    regHeader = re.compile('<title>(.+) / газета За урожай, Смоленск, п. Шумячи</title>', flags=re.U | re.DOTALL)
    header = regHeader.search(html).group(1)
    #print(header)

#created


#topic
