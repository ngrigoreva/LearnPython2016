html = open ('хытымыэль на проверку.txt', 'r', encoding = 'utf-8').read()

import re

#author
regAuthor = re.compile('<p style="text-align: right;"><strong>([ёА-Яа-я.]+)', flags=re.U | re.DOTALL)
author = regAuthor.search(html)
if author:
    print(author.group(1))
else:
    author = 'undefined'
    print(author)

#header
regHeader = re.compile('<title>([ёА-Яа-я.,!? ]+)', flags=re.U | re.DOTALL)
header = regHeader.search(html).group(1)
print(header)

#created


#topic


