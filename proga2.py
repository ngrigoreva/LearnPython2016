import os

def mystem:
    os.system(r'C:\\Users\\ADMIN\\mystem.exe -ncid' + 'input.txt' + ' ' + 'output.txt')

def Tables():
    f = open('input.txt', 'r', encoding='utf-8')
    words = f.read().split()#массив, разделенный по проебелам
    i = 0#позиция слова в тексте
    MystemFile = open('output.txt', 'r', encoding='utf-8')

    sql1 = 'INSERT INTO table1 (id, wordform, lmark, rmark, position, id2) VALUES (0, %s, %d, %d, %d, )' % (strippedWord, lmark, rmark, i)
    #дописать ссылку на айди2; найти все значения в ссылках
    f1 = open('output1.sql', 'w', encoding='utf-8')
    line = 'CREATE TABLE table1 (id INTEGER PRIMARY KEY, wordform VARCHAR, lmakr , rmark , position INTEGER PRIMARY KEY, id2 INTEGER PRIMARY KEY' + join(sql1)
    f1.write(line)

    f2 = open('output2.sql', 'w', encoding = 'utf-8')
    
    
return 


def main():
    #sth


main()


