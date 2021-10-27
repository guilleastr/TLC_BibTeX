import re
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

def document_cration(matches):
    
    return ""

htmli.write_to_file(applyER_text(r'@[a-zA-Z]+',PATH+file), "1.html")
htmli.write_document(applyER_text(r'\{[a-zA-Z0-9.:\-\\]+,\n',PATH+file),"2.html")







