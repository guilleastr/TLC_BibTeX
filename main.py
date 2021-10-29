from functions import Document, applyER_text, count_matches, sub_array ,split_array

PATH = ''
FILENAME = 'exemplo-utf8.bib'
FILE = PATH+FILENAME

CATEGORY_ER = r'@([a-zA-Z]+)'
KEY_ER = r'\{([a-zA-Z0-9.:\-\\]+),\n'
AUTHOR_ER = r'(?i:author)[ \t]*=([ \t]*[{"][^}"]+)[\n\t ]*[}"]' 
TITLE_ER = r' (?i:title)[ \t]*=([ \t]*[{"][^}"]+)[\n\t ]*[}"]' #Verificar RODRIGO

#alternativa title  [^a-z]title[ \t]*=[ \t]*[{"][^(",)]+[\n\t ]*[}"]

if __name__ == '__main__':
    categories =applyER_text(CATEGORY_ER,FILE,1)
    keys =(applyER_text(KEY_ER,FILE,1))
    authors = split_array(sub_array(applyER_text(AUTHOR_ER,FILE,1),r'[ \n\t]+'," "),'[ ]+and[ ]+')
    titles = 

    DOCUMENTS = [Document(categories[i],authors[i],titles[i],keys[i]) for i in range(len(keys))] #Array de Documentos

    dic_categories = count_matches(categories) #Diccionario con las categorias y sus respectivos matches
