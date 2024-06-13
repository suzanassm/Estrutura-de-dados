class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size():
        return len(self.items)


quant_veiculos, fator_amostragem, peso = map(int, input().split())
tempo = 0
peso_carro = input().split()
fila = Queue()
cont = 0

for i in range(quant_veiculos):
    fila.enqueue(int(peso_carro[i]))
teste = True
while not fila.isEmpty():
    carro_revistado = fila.dequeue()
    if cont % fator_amostragem == 0:
        if int(carro_revistado) <= peso:
            tempo += 5
            
        else:
            fila.enqueue(carro_revistado -2)
            tempo += 10
            teste = False
    else:
        tempo += 1
    cont += 1

  
print(tempo)