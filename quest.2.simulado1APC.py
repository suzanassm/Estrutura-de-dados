peixe, valor = input().split()
valor= float(valor)
i= 0

print("+--------------------+--------------------+")
print("|        peixe       |      preço   R$    |")
print("+--------------------+--------------------+")
if peixe == "fim":
    print("|           Hoje não tem peixe            |")
    print("+-----------------------------------------+")
    
while peixe != "fim":
    preco = (f"{valor:.02f}")
    print(f"| {peixe:<18} | {preco:>18} |")
    print("+--------------------+--------------------+")
    if i == 0:
        menor_peixe = peixe
        menor_valor  = valor
    
    peixe, valor = input().split()
    valor= float(valor)
    if peixe != "fim":
        i=+1
        if menor_peixe < peixe:
            menor_peixe = menor_peixe
            menor_valor = menor_valor
        else:
            menor_peixe = peixe
            menor_valor =valor
if i != 0:
    menor_valor = (f"{menor_valor:.02f}")
    print(" ")
    print("+-----------------------------------------+")
    print("|         Cambada de menor preço          |")
    print("+--------------------+--------------------+")
    print(f"| {menor_peixe:<18} | {menor_valor:>18} |")
    print("+--------------------+--------------------+")
    
    