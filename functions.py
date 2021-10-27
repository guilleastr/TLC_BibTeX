import re

class Document:
    def __init__(self,category,authors,title,key):
        self.category = category
        self.key = key
        self.authors = authors
        self.title = title


def applyER_text(ER,file):
    matches = []
    with open(file,'r',encoding='UTF-8') as f:
        line = f.readline()
        while line:
            if (m := re.search(ER,line)):
                matches.append(m.group())
            line = f.readline()
        f.close()
    return matches

def split_array(array,i,j):
    for k,a in enumerate(array):
        array[k] = a[i:j]
    return array


def count_matches(matches):
    dic = {}
    for match in matches:
        try:
            dic[match] += 1
        except:
            dic[match] = 1
    
    return dic
