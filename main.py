from functions import Document, applyER_text, count_matches, sub_array ,split_array

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
    authors = split_array(sub_array(applyER_text(AUTHOR_ER,FILE),r'((?i:author)[ \t]*=[ \t]*[{"]|[{}"\n]*)',''),'[ ]+and[ ]+')
    titles = ['title']*len(keys) #Modificar com as ER

    DOCUMENTS = [Document(categories[i],authors[i],titles[i],keys[i]) for i in range(len(keys))] #Array de Documentos

    dic_categories = count_matches(categories) #Diccionario con las categorias y sus respectivos matches