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

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size():
        return len(self.items)
for i in range(5):
    num_operacoes = int(input())
    pilha = Stack()
    fila = Queue()
    ehPilha = False
    ehFila = False
    ehPilhaFila = False

    for i in range(num_operacoes):
        operacao = input().split()
        if operacao[0] == "in":
            pilha.push(int(operacao[1]))
            fila.enqueue(int(operacao[1]))
        else: #operacao[0] == 0
            saida_pilha = pilha.pop(int(operacao[1]))
            saida_fila = fila.dequeue(int(operacao[1]))
            if saida_pilha == operacao[1] and saida_fila == operacao[1]:
                ehPilhaFila = True
            
            elif saida_pilha == operacao[1]:
                ehPilha = True
                
            elif saida_fila == operacao[1]:
                ehFila = True
                
            
            
            
