def frequencia(lista):
    lista_comparacao = lista
    cont_comparacao = 0
    if len(lista) == 0:
        return " "
    else:
        for elemento in lista:
            cont = 0
            for elemento_comparacao in lista_comparacao:
                if elemento == elemento_comparacao:
                    cont += 1
            if cont_comparacao < cont:
                cont_comparacao = cont
                elemento_comp = elemento
        
        return elemento_comp
            
        
