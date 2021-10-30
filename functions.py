import re

class Document:
    def __init__(self,category,authors,title,key):
        self.category = category
        self.key = key
        self.authors = authors
        self.title = title
    
    
class Author:
    def __init__(self,author):
        self.author = author
        self.publications = []
        self.colaborators = {}

    def add_colaborator(self,name,val=1):
        try:
            self.colaborators[name] += val
        except:
            self.colaborators[name] = 1

    def add_publication(self,doc):
        self.publications.append(doc.title)
        for auth in doc.authors:
            if auth != self.author:
                self.add_colaborator(auth)
    
    def concat_author(self, author):
        self.publications += author.publications
        for colab in author.colaborators:
            self.add_colaborator(colab,author.colaborators[colab])
    
    def print_author(self):
        print(f'{self.author}:\n\tPublicaciones:')
        for pub in self.publications:
            print(f'\t -{pub}')
        print(f'\tColaboradores:')
        for colab in self.colaborators:
            print(f'\t -{colab} = {self.colaborators[colab]}')

def applyER_text(ER,file,ngroup=0):
    matches = []
    with open(file,'r',encoding='UTF-8') as f:
        text = f.read()
        f.close()

    while m:=re.search(ER,text):
        text = text[m.end()+1:]
        matches.append(m.group(ngroup))
    return matches

def split_array(array,er):
    for k,a in enumerate(array):
        array[k] = re.split(er,a)
    return array


def sub_array(array,er,sub):
    for k,a in enumerate(array):
        array[k] = re.sub(er,sub,a)
    return array


def count_matches(matches):
    dic = {}
    for match in matches:
        try:
            dic[match] += 1
        except:
            dic[match] = 1
    return dic
