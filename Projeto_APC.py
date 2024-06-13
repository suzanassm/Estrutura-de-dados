frase = input().split()
cont_aluguel = 0
cont_venda = 0
cont_casa = 0
cont_apt = 0
cont_cep = 0
cont_area = 0
cont_valor = 0
telefone = []
i = 0
j = 0
endereco = []
cont_virgula = 0
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for elemento in frase:
    
    #Modalidade
    if elemento == "aluguel" or elemento == "alugo" or elemento =="alugar":
        cont_aluguel += 1
    if elemento == "venda" or elemento == "vendo" or elemento == "vender":
        cont_vender += 1
    
    #Tipo
    if elemento == "Casa" or elemento == "casa":
        cont_casa += 1
    if elemento == "Apartamento" or  elemento == "apartamento":
        cont_apt += 1
        
    #Endereco
    if elemento == "Rua" or elemento == "Avenida":
        for elemento in frase[i:-1]:
            if elemento == ",":
                cont_virgula += 1
                if cont_virgula != 0:
                    break
            endereco.append(elemento)
            
            
    #Cep ou telefone:
    if elemento == "-":
        if frase[i+4] in numeros: #eh telefone
            if frase[i-5] in numeros: #tem 5 digitos antes do -
                if len(telefone) > 0:
                    telefone2 = *telefone
                    telefone = frase[i-5:i+4], telefone2
                else:
                    telefone = frase[i-5:i+4]
            else: #tem 4 digitos antes do -
                if len(telefone) > 0:
                    telefone2 = *telefone
                    telefone = frase[i-5:i+4], telefone2
                else:
                    telefone = frase[i-4:i+4]
        else: #eh cep
            cep = frase[i-5:i+3]
            cont_cep += 1
    #Área:
    if elemento == "metros quadrados" or elemento == "m2":
        ????
        cont_area += 1
        
    #Valor
    if elemento == "R$":
        for elemento in frase[i:]:
            if elemento in numeros:
                valor.append(elemento)
            else:
                if frase[j+1] in numeros:
                    valor.append(elemento)
                else:
                    break
            j += 1
        cont_valor += 1
        
    if elemento == "reais":
        ????
        cont_valor += 1
    
    #Responsável:
        ???
        
        
    i += 1
#Print modalidade  
if cont_aluguel != 0:
    print("Modalidade: Aluguel")
else:
    print("Modalidade: Venda")

#Print tipo
if cont_casa != 0:
    print("Tipo: Casa")
else:
    print("Tipo: Apartamento")
    
#Print enderco
print(f"Endereco: {*endereco}")

#Print cep
if cont_cep != 0:
    print(f"CEP: {*cep}")
else:
    print("CEP: nao informado")
    
#Print area
if cont_area != 0:
    print(f"Area: {*area}")
else:
    print("Area: nao informado")

#Print valor
if cont_valor != 0:
    print(f"Valor: {*valor}")
else:
    print("Valor: nao informado")
    
#Print telefone
print("Telefone: {*telefone}")

#Print responsável
print(f"Responsavel: {*responsavel}")


#estou com dificuldade quando a palavra chave vem depois do que preciso e o do nome do responsavel nao faco ideia



        
        