import re

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

def count_matches(matches):
    dic = {}
    for match in matches:
        try:
            dic[match.group()] += 1
        except:
            dic[match.group()] = 1
    
    return dic

def convert2HTML(dic):
    s = '<UL>\n'
    tags = [x for x in dic]
    for tag in tags:
        s += f'\t<LI>{tag[1:]}: {dic[tag]}</LI>\n'
    s += '</UL>'
    return s

def convert2HTMLchave(dic):
    s = '<UL>\n'
    tags = [x for x in dic]
    for tag in tags:
        s += f'\t<LI>{tag[1:-2]}: {dic[tag]}</LI>\n'
    s += '</UL>'
    return s

html = '''<!DOCTYPE html>
<html>
<head>
<title>TLC 1</title>
</head>
<body>

<h1>Categorias do BibTeX</h1>
'''
html += convert2HTML(count_matches(applyER_text(r'@[a-zA-Z]+',PATH+file)))
html += convert2HTMLchave(count_matches(applyER_text(r'\{[a-zA-Z0-9.:\-\\]+,\n',PATH+file)))

#Esta expressão regular encontra todos os autores mas é preciso remover todos os espaços repetidos
#para depois poder fazer tag[n:]
#Há uma frase no ficheiro .bib que está em camps lock por isso talvez tenhamos de tornar esta ER case insensitive
#html += convert2HTMLchave(count_matches(applyER_text(r'author[ \t]*=[ \t]*[{"][^}"]+[\n\t ]*[}"]',PATH+file)))

#É preciso fazer a mesma coisa 
#html += convert2HTMLchave(count_matches(applyER_text(r' title[ \t]*=[ \t]*[{"][^}"]+[\n\t ]*[}"]',PATH+file)))

html += '</body>\n</html>'

with open('index.html','w') as f:
    f.write(html)
    f.close()