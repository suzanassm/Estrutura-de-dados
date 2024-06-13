num_linhas = int(input())
indice = int(input())
lista = []
valor = 0
i=0
nova_lista = []
soma_teste = 0

for i in range(num_linhas):
    linha = [int(x) for x in input().split()]
    lista.append(linha)
print(lista)
for elemento in lista:
    soma = sum(elemento)
    i = 0
    for sub_elemento in elemento:
        
        if sub_elemento[i] == sub_elemento[indice]:
            if sub_elemeto > valor:
                valor = sub_elemento
                nova_lista.insert(0, elemento)
            else:
                nova_lista.append(elemento)
            if sub_elemento == valor:
                if soma_elemento > soma_teste:
                    nova_lista.insert(0, elemento)
                else:
                    nova_lista. insert(1, elemento)
        i+= 1
    soma_teste = soma
            
for elemento in nova_lista:
    print(elemento)
    
