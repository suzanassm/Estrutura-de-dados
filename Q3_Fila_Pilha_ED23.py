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


frase = input()
frase = list(frase)
pilha = Stack()
resultado = ""

for elemento in frase:
    if elemento == "*":
        resultado = resultado + str(pilha.pop())
        
    else:
        pilha.push(elemento)
print(resultado)        