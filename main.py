from functions import Document, applyER_text, count_matches, sub_array ,split_array
import html_indexer as htmli
from grafo import Grafo
PATH = ''
FILENAME = 'exemplo-utf8.bib'
FILE = PATH+FILENAME

CATEGORY_ER = r'@[a-zA-Z]+'
KEY_ER = r'\{[a-zA-Z0-9.:\-\\]+,\n'
AUTHOR_ER = r'(?i:author)[ \t]*=[ \t]*[{"][^}"]+[\n\t ]*[}"]' #Verificar RODRIGO
TITLE_ER = r' title[ \t]*=[ \t]*[{"][^}"]+[\n\t ]*[}"]' #Verificar RODRIGO

if __name__ == '__main__':
    categories = sub_array(applyER_text(CATEGORY_ER,FILE),'@','')
    keys = sub_array(applyER_text(KEY_ER,FILE),r'[{,\n]','')
    authors = split_array(sub_array(applyER_text(AUTHOR_ER,FILE),r'((?i:author)[ \t]*=[ \t]*[{"]|[{}"\n]*)',''),'[ ]+and[ ]+.*')
    titles = ['title']*len(keys) #Modificar com as ER

    DOCUMENTS = [Document(categories[i],authors[i],titles[i],keys[i]) for i in range(len(keys))] #Array de Documentos

    dic_categories = count_matches(categories) #Diccionario con las categorias y sus respectivos matches
    #htmli.write_to_file(dic_categories, "exercise1.html")

    #htmli.write_document(DOCUMENTS,"exercise2.html")


    grafo = Grafo()
    names=[]
    for doc in DOCUMENTS:
        
        for auth in doc.authors:
            print(auth)
            names.append(auth)
    names=list(set(names))
    print(names)
    grafo.load_names(names)
    #print(grafo.nodos)
