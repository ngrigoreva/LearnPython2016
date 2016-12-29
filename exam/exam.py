import urllib.request
import os
import re
import html.parser 

def five():
    req = urllib.request.Request('http://web-corpora.net/Test2_2016/short_story.html')
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    #regex_title = re.compile('<h1 class="b-topic__title">«(.*?)»</h1><h2 class="b-topic__rightcol">(.*?)</h2>', flags=re.U | re.DOTALL)
    # первая группа - заголовок, вторая - подзаголовок
    regex_russian_words = re.compile('.*?[>&{(«" ]\b([а-яА-Яё ]+?[-]?[а-яА-Яё ]*?)[ \s<:;,.!?})%»"].*?', flags=re.U | re.DOTALL)
    russian_words = re.findall(regex_russian_words, html) 
    #html.parser.HTMLParser().unescape(russian_text) # замена специальных символов

    # все найденные тексты делим на слова, слова кладем в массив all_russian_words
    
    all_russian_words = []
    for text in russian_words:
        word1 = text.split()
        for word in word1:
            all_russian_words.append(word)

    print(len(all_russian_words))

    words_s = []
    for word in all_russian_words:
        if word.startswith('с') or word.startswith('С'):
            print(word)
            words_s.append(word)
        else:
            continue
    return words_s
    
def eight(words_s):
    file_s = open('file_s.txt', 'w')
    for word in words_s:
        file_s.write(word + ' \n')
    os.system('C:\\Users\\student\\Desktop\\exam\\mystem.exe -nid file_s.txt output_s.txt')
    MystemFile = open('output_s.txt', 'r', encoding='utf-8')
    parsed_s = MystemFile.read()
    regex_verbs = re.compile(r'(.*?){.*?=V,.*?}', flags=re.U | re.DOTALL)
    verbs = re.findall(regex_verbs, parsed_s)
    for verb in verbs:
        print(verb)
    fl = open('insert_file.txt', 'w')
    lines = MystemFile.readlines()
    sqlarr1 = []
    uniqueDict = {}
    for line in lines:
        regex = re.search('([а-яА-Яё]+?){([а-яА-Яё]+?)=([A-Z])}', line)
        wordform = regex.group(1).lower()
        lemma = regex.group(2)
        part_of_speech = regex.group(3)
        if (wordform and lemma) in uniqueDict:
            continue
        else:
            uniqueDict[wordform] = lemma
        sql1 = 'INSERT INTO table1 (id, wordform, lemma, part_of_speech) VALUES (0, %s, %s, %s)' % (wordform, uniqueDict[wordform], part_of_speech)
        sqlarr1.append(sql1)
    table1 = 'CREATE TABLE table1 (id INTEGER PRIMARY KEY, wordform VARCHAR, lemma VARCHAR, part_of_speech VARCHAR' + str(sqlarr1)
    fl.write(table1)
    fl.close()
    file_s.close()


def main():
    words_s = five()
    ten = eight(words_s)
       
if __name__=='__main__':
    main()
