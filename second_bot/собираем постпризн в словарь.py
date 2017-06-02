import random
import json
import re
import pymorphy2

# создаем список словоформ, содержащихся в  файле, скачанном с сайта НКРЯ
def pymrlist_lemma_():
    text = (open('поговори с достоевским.txt', 'r', encoding = 'utf-8')).read()
    pymrlist_lemma = []
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    mass = text.split()
    for x in mass:
        x.strip(',«.»')
        x.strip(',«.»')
    for x in mass:
        ana = morph.parse(x)
        #print(ana)
        for z in ana:
            pymrlist_lemma.append(z.word)
    return pymrlist_lemma

# собираем посотоянные признаки и слова с ними в словарь {неизменяемые признаки: [список слов, имеющих эти признаки]}
def pymrlist_postprizn(pymrlist_lemma):
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    dictionary = {}
    for lemma in pymrlist_lemma:
        ana = morph.parse(lemma)
        tags = str(ana[0].tag).split(' ')[0] # постоянные признаки
        if tags in dictionary:
            dictionary[tags].append(lemma)
        else:
            dictionary[tags] = [lemma]
    with open('dictionary.json', 'w') as f:
        json.dump(dictionary, f)

pymrlist_postprizn(pymrlist_lemma_())
