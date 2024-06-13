bits = int(input())
cont = 0
soma_bits = 0
soma = 0
print(f"Transmitindo {bits} bytes...")

while soma != bits:
    bits_carregando = int(input())
    soma += bits_carregando
    soma_bits += bits_carregando
    cont += 1
    if cont%5 == 0 and cont!=0:
        vel = soma_bits/5
        rest = soma_bits % 5
        if vel == 0 and rest == 0:
           print("Tempo restante: pendente...")
        else:
            seg = (bits-soma)//vel
            resto = (bits-soma)%vel
            if resto != 0:
                seg = seg +1
            if seg != 0:
                seg = int(seg)
                print(f"Tempo restante: {seg} segundos.")
        soma_bits = 0   
    

print(f"Tempo total: {cont} segundos.")