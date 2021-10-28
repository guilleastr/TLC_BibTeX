import re

class Document:
    def __init__(self,category,authors,title,key):
        self.category = category
        self.key = key
        self.authors = authors
        self.title = title

    def extract_authors(self):
        to_ret=[]
        i=1
        for auth in self.authors: 
            i+=1
            if(i<len(self.authors)>1):
                to_ret.append(auth)

        return to_ret

PATH = ''
file = 'exemplo-utf8.bib'

def applyER_text(ER,file):
    matches = []
    with open(file,'r',encoding='UTF-8') as f:
        text = f.read()
        f.close()

    while m:=re.search(ER,text):
        text = text[m.end()+1:]
        matches.append(m.group())
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
def document_cration(matches):
    
    return ""


