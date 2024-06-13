
def divisores(num):
    lista = []
    numero = 1
    for i in range(num):
        div = num % numero
        if div == 0:
            lista.append(numero)
        numero += 1
        
    return lista
       
