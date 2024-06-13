class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


num_roupas = int(input())
pilha_roupa = Stack()
pilha_cor = Stack()
tempo_total = 0


for i in range(num_roupas):
    roupa, cor, tempo = input().split()
    tempo_total += int(tempo)
    pilha_roupa.push(roupa)
    pilha_cor.push(cor)
    

while not pilha_roupa.isEmpty():
    print(f"Tipo: {pilha_roupa.pop()}, Cor: {pilha_cor.pop()}")
print(f"Total de roupas: {num_roupas}")
print(f"Total de tempo: {tempo_total}")
    
    
    
    
    
    
    
    
    
    