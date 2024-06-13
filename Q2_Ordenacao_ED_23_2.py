num_pretendentes = int(input())
lista_nome = []
lista_sobrenome = []
lista_altura = []
lista_massa = []
passadas = num_pretendentes -1

for i in range(num_pretendentes):
    nome, sobrenome, altura, massa = input().split()
    altura = int(altura)
    massa = int(massa)
    lista_nome.append(nome)
    lista_sobrenome.append(sobrenome)
    lista_altura.append(altura)
    lista_massa.append(massa)
    
for i in range(num_pretendentes):
    dif_altura = ((lista_altura[i] - 180)**2)**0.5
    lista_altura[i] = dif_altura




mudanca = True
while passadas > 0 and mudanca:
    mudanca = False
    for i in range(passadas):
        if lista_altura[i]>lista_altura[i+1]:
            mudanca = True
            temp = lista_altura[i]
            lista_altura[i] = lista_altura[i+1]
            lista_altura[i+1] = temp
            
            temp = lista_nome[i]
            lista_nome[i] = lista_nome[i+1]
            lista_nome[i+1] = temp
            
            temp = lista_sobrenome[i]
            lista_sobrenome[i] = lista_sobrenome[i+1]
            lista_sobrenome[i+1] = temp
            
            temp = lista_massa[i]
            lista_massa[i] = lista_massa[i+1]
            lista_massa[i+1] = temp
            
        elif lista_altura[i]==lista_altura[i+1]:
            dif_massa_i = (lista_massa[i] - 75)
            dif_massa_j = (lista_massa[i+1] - 75)
            if dif_massa_i == 0 or dif_massa_j == 0 or (dif_massa_i<0 and dif_massa_j<0):
                dif_massa_i = ((lista_massa[i] - 75)**2)**0.5
                dif_massa_j = ((lista_massa[i+1] - 75)**2)**0.5
                
            if dif_massa_i > dif_massa_j:
                mudanca = True
            
                temp = lista_altura[i]
                lista_altura[i] = lista_altura[i+1]
                lista_altura[i+1] = temp
            
                temp = lista_nome[i]
                lista_nome[i] = lista_nome[i+1]
                lista_nome[i+1] = temp
            
                temp = lista_sobrenome[i]
                lista_sobrenome[i] = lista_sobrenome[i+1]
                lista_sobrenome[i+1] = temp
            
                temp = lista_massa[i]
                lista_massa[i] = lista_massa[i+1]
                lista_massa[i+1] = temp
                
                
            elif dif_massa_i == dif_massa_j:
                lista_sobrenome_ordenada = []
                lista_sobrenome_ordenada.append(lista_sobrenome[i])
                lista_sobrenome_ordenada.append(lista_sobrenome[i+1])
                lista_sobrenome_ordenada.sort()
            
                if lista_sobrenome[i+1] == lista_sobrenome_ordenada[0] and lista_sobrenome[i+1] != lista_sobrenome[i]:
                    mudanca = True
                    
                    temp = lista_altura[i]
                    lista_altura[i] = lista_altura[i+1]
                    lista_altura[i+1] = temp
                
                    temp = lista_nome[i]
                    lista_nome[i] = lista_nome[i+1]
                    lista_nome[i+1] = temp
                
                    temp = lista_sobrenome[i]
                    lista_sobrenome[i] = lista_sobrenome[i+1]
                    lista_sobrenome[i+1] = temp
                
                    temp = lista_massa[i]
                    lista_massa[i] = lista_massa[i+1]
                    lista_massa[i+1] = temp
                    
                elif lista_sobrenome[i+1] == lista_sobrenome[i]:
                    lista_nome_ordenada = []
                    lista_nome_ordenada.append(lista_nome[i])
                    lista_nome_ordenada.append(lista_nome[i+1])
                    lista_nome_ordenada.sort()
                    
                    if lista_nome[i+1] == lista_nome_ordenada[0]:
                        mudanca = True
                        
                        temp = lista_altura[i]
                        lista_altura[i] = lista_altuta[i+1]
                        lista_altura[i+1] = temp
                    
                        temp = lista_nome[i]
                        lista_nome[i] = lista_nome[i+1]
                        lista_nome[i+1] = temp
                    
                        temp = lista_sobrenome[i]
                        lista_sobrenome[i] = lista_sobrenome[i+1]
                        lista_sobrenome[i+1] = temp
                    
                        temp = lista_massa[i]
                        lista_massa[i] = lista_massa[i+1]
                        lista_massa[i+1] = temp

            
    passadas = passadas -1
    
for i in range(num_pretendentes):
    print(f"{lista_sobrenome[i]}, {lista_nome[i]}")
    
    
                    
                

                



            
    
    
    