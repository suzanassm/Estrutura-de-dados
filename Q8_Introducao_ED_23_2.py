num_vezes = int(input())
for i in range(num_vezes):
    lista = map(int,input().split())
    cont = 0
    cont_comp = 0
    
    for num in lista:
        if num == "0":
            cont += 1
        else:
            cont_comp = cont + cont_comp
            cont = 0
        j += 1
    print(cont_comp)
            
            
        
    