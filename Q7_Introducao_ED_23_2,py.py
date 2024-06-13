def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True

    
numero = int(input())
lista = []
num = 3
p2 = 3

while len(lista) != numero:
    if primo(num) and num != 4:
        p1 = p2
        p2 = num
        if p2 == p1 + 2:
            tupla = (p1, p2)
            lista.append(tupla)
    num += 1
        
print(lista)



                    
