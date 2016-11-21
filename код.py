import os
import re

files = os.listdir(path='C:\\Users\\student\\Desktop\\папка\\thai_pages')
#print(files)
def get_thaiWords(line):
       #thai-eng_word: <tr><td class=th><a href='/id/148333'>-------ปัตตะเลี่ยน--------</a>
       #</td><td>bpat<span class='tt'>L</span> dta<span class='tt'>L</span>
       #liian<span class='tt'>F</span></td><td class=pos>noun</td><td>--------hair clippers-------</td></tr>
    regWordsThai = re.compile('<tr><td class=[a-z]+><a href=\'/id/[0-9]+\'>(.*?)</a>', flags=re.U | re.DOTALL)
    wordsThai = regWordsThai.search(line)
    if wordsThai:
        thai = wordsThai.group(1)
        print(thai)
    #return(thai)

#'</a></td><td>[a-z]+<span class=\'[a-z]+\'>[a-zA-Z]+
#</span> [a-z]+<span class=\'[a-z]+\'>[a-zA-Z]+</span> [a-z]+<span class=
#\'[a-z]+\'>[a-zA-Z]+</span>[a-z<span class+\'[a-z]+\'>[a-zA-Z]+</span></td><td class=[a-z]+>[a-z]+</td><td>(.*)</td></tr>'
def get_engWords(line):
    regWordsEng = re.compile('</a></td><td>[a-z]+<span class=\'[a-z]+\'>[a-zA-Z]+</span> [a-z]+<span class=\'[a-z]+\'>[a-zA-Z]+</span>[a-z]+<span class=\'[a-z]+\'>[a-zA-Z]+</span>[a-z<span class+\'[a-z]+\'>[a-zA-Z]+</span></td><td class=[a-z]+>[a-z]+</td><td>(.*)</td></tr>', flags=re.U | re.DOTALL)
    wordsEng = regWordsEng.search(line)
    if wordsEng:
        eng = wordsEng.group(1)
        print(eng)
    #return(eng)

os.chdir(path='C:\\Users\\student\\Desktop\\папка\\thai_pages')
for fl in files:
    f = open(fl, encoding = 'UTF-8')
    cooldict = {}
    for line in f:
        get_thaiWords(line)
        get_engWords(line)
        #cooldict[thai] = eng
    #print(cooldict)
