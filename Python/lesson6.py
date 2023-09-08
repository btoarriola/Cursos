# Ejercicio 1
print("ejercicio 1------------")
def is_valid_zip(zip_code):

    print(zip_code)
    if(len(zip_code)==5 and zip_code.isdigit()): 
        return True
    else:
        return False
    pass

# Ejercicio 2
print("ejercicio 2------------")
def word_search(doc_list, keyword):
    lista=[]
    i=0
    doc_list
    keyword=keyword.upper()
    if(len(doc_list)>0):
        for doc in doc_list:
            doc=doc.upper()
            narreglo=doc.split()
            for prueba in narreglo:
                prueba=prueba.strip(',.')
                if((prueba == keyword) and len(keyword)==len(prueba) ):
                    lista.append(i)
                    break
            i=i+1
        
            
    elif(keyword in doc_list):
        return [i]
    return lista
    
    pass

# Ejercicio 3
print("ejercicio 3------------")
def word_search(doc_list, keyword):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices