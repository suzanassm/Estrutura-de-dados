num_testes = int(input())


for i in range(num_testes):
    planejamento =input()
    planejamento=list(planejamento)
    nao_feito = planejamento
    estudo = True
    
    for z in range(3):
        turno = input()
        turno =list(turno)
        while estudo and turno != None:
            for i in range(len(turno)-1):
                
                print((len(planejamento)-1))
                print(planejamento)
                
                for j in range(len(planejamento)-1):
                    if turno[i] == planejamento[j]:
                        if planejamento[j] in nao_feito:
                            letra = planejamento[j]
                            nao_feito.remove(letra)
                    else:
                        estudo= False
        
    if not estudo:
        print("You died!")
    elif len(nao_feito) != 0:
        print(f"Bora ralar:{nao_feito}")
    else:
        print("It's in the box!")
                        
