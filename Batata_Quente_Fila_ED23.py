def BatataQuente(lista_nome, num):
    fila = Queque()
    for nome in lista_nome:
        fila.enqueque(nome)
        
    while fila.size() > 1:
        for i in range(num):
            fila.enqueque(fila.dequeque())
            
        fila.dequeque()
        
    return fila.dequeque()
