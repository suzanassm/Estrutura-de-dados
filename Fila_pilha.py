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
        
        
class Fila_comPilhas:
    def __init__(self):
         self.pilha1 = Stack() #normal
         self.pilha2 = Stack() #invertida
         
    def enqueue(self,item):
        while (not self.pilha2.isEmpty()):
            self.pilha1.push(pilha2.pop())
        self.pilha1.push(item)
        
    def dequeue(self):
        if self.pilha1.isEmpty():
            return None
        else:
            while (not self.pilha1.isEmpty()):
                self.pilha2.push(self.pilha1.pop())
            return self.pilha2.peek()
        
    def imprime(self):
        i = 0
        while (not self.pilha1.isEmpty()):
                self.pilha2.push(self.pilha1.pop())
        while (not self.pilha2.isEmpty()):
            print(self.pilha2.pop())
           
        
"""def mudaPilha(origem, destino):
    while (not origem.isEmpty()):
        destino.push(origem.pop())"""
        
        
fila = Fila_comPilhas()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
print('dequeue - '+ str(fila.dequeue()))
fila.enqueue(6)
print('dequeue - '+ str(fila.dequeue()))
print('dequeue - '+ str(fila.dequeue()))
fila.imprime()
