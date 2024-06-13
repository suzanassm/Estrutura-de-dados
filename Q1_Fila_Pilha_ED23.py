class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
       return self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items ==[]






frase= str(input())
fila = Queue()
resultado = ""
frase=list(frase)

for elemento in frase:
    if elemento == "*":
        resultado = resultado + str(fila.dequeue())
    else:
        fila.enqueue(elemento)
        
        
print(resultado)        
        
        
        
        