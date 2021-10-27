import re

class Document:
    def __init__(self,category,authors,title,key):
        self.category = category
        self.key = key
        self.authors = authors
        self.title = title

import html_indexer as htmli
PATH = ''
file = 'exemplo-utf8.bib'

def applyER_text(ER,file):
    matches = []
    with open(file,'r',encoding='UTF-8') as f:
        line = f.readline()
        while line:
            if (m := re.search(ER,line)):
                matches.append(m)
            line = f.readline()
        f.close()
    return matches

def split_array(array,i,j):
    return array[i:j]


def count_matches(matches):
    dic = {}
    for match in matches:
        try:
            dic[match.group()] += 1
        except:
            dic[match.group()] = 1
    
    return dic
def document_cration(matches):
    
    return ""

htmli.write_to_file(applyER_text(r'@[a-zA-Z]+',PATH+file), "1.html")
htmli.write_document(applyER_text(r'\{[a-zA-Z0-9.:\-\\]+,\n',PATH+file),"2.html")







