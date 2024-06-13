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



nome = input().split()
rodadas = int(input())
fila = Queue()

for i in range(len(nome)):
    fila.enqueue(nome[i])
    
for j in range(rodadas):
    fila.enqueue(fila.dequeue())

primeiro = True
while not fila.isEmpty():
    if primeiro:
        primeiro = False
        frente = fila.dequeue()
    else:
        fim = fila.dequeue()
        
print(f"Pessoa da frente: {frente}")
print(f"Pessoa do fim: {fim}")
    
