class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if  not self.isEmpty():
            return self.items.pop()

    def peek(self):
        #if not self.items.isEmpty():
        if  not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        if  not self.isEmpty():
            return len(self.items)
        else:
            return 0




peso = int(input())
pilha_pesos = Stack()

while peso != 0:
    pilha_pesos.push(peso)
    peso = int(input())
    
peso_escolhido = int(input())

saida = pilha_pesos.pop()
cont = 1
peso_total = saida
while saida != peso_escolhido:
    cont += 1
    print(f"Peso retirado: {saida}")
    saida = pilha_pesos.pop()
    peso_total += saida
    
print(f"Peso retirado: {saida}")
print(f"Anilhas retiradas: {cont}")
print(f"Peso total movimentado: {peso_total}")