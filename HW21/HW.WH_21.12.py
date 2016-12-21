import os
import re

def mystem():
    os.system(r'C:\\Users\\ADMIN\\mystem.exe -ncid' + 'input.txt' + ' ' + 'output.txt')

def Tables():
    f = open('input.txt', 'r', encoding='utf-8')
    f1 = open('output1.sql', 'w', encoding = 'utf-8')
    words = f.read().split()#массив, разделенный по проебелам
    i = 0#позиция слова в тексте
    MystemFile = open('output.txt', 'r', encoding = 'utf-8')
    lines = MystemFile.readlines()
    sqlarr1 = []
    uniqueDict = {}
    for line in lines:
        regex = re.search('([а-яА-Яё]+?){([а-яА-Яё]+?)}', line)
        wordform = regex.group(1).lower()
        lemma = regex.group(2)
        if (wordform and lemma) in uniqueDict:
            continue
        else:
            uniqueDict[wordform] = lemma
        #uniqueDict = dict(zip(wordform, lemma)).lemma()
        #for key, value in uniqueDict:
            #wordform = dict.keys(uniqueDict)
            #lemma = dict.get(key[, default]) не работает
        sql1 = 'INSERT INTO table1 (id, wordform, lemma) VALUES (0, %s, %s)' % (wordform, uniqueDict[wordform])
        sqlarr1.append(sql2)
    table1 = 'CREATE TABLE table1 (id INTEGER PRIMARY KEY, wordform VARCHAR, lemma VARCHAR' + str(sqlarr1)
    sqlarr2 = []
    for word in words:
            lmark = 0
            rmark = 0
            strippedWord = word.strip(' .,?!^:;\"—()[]{}')
            #if word != strippedWord and strippedWord:
            if word[0] != strippedWord[0]:
                lmark = 1
            if word[-1] != strippedWord[-1]:
                rmark = 1                
                i += 1
                sql2 = 'INSERT INTO table1 (id, wordform, lmark, rmark, position, id2) VALUES (0, %s, %d, %d, %d, )' % (strippedWord, lmark, rmark, i)
                sqlarr2.append(sql2)
            selectLine2 = 'SELECT table1.id from table1 WHERE table2.id = table1.id'
            table2 = 'CREATE TABLE table2 (id INTEGER PRIMARY KEY, wordform VARCHAR, lmakr INTEGER PRIMARY KEY, rmark INTEGER PRIMARY KEY, position INTEGER PRIMARY KEY, id2 INTEGER PRIMARY KEY' + '\n' + str(sqlarr2) + '\n' + selectLine2
    f1.write(table2 + '\n' + table1)
    f1.close()
    f.close()



def main():
    mystem()
    Tables()

main()
