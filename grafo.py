

class Grafo:
    def __init__(self):
        self.nodos=[]
        self.trabajando=[[]]

    def extract_position(self,name):
        for i in range(0,len(self.nodos)):
            if(self.nodos[i]==name):
                return i
        else:
             return -1

    def load_names(self,list_names):
        self.nodos=list_names

    

    def process_names(self,docs):
        document_tuple=[]
        for doc in docs:
            document_tuple.append(doc.c.extract_authors())
        for nodo in self.nodos:
            for doc in document_tuple:
                if(nodo in doc):
                    for colaborator in doc:
                        self.trabajando[self.extract_position(nodo)][self.extract_position[colaborator]]+=1

        print(self.trabajando)
            


