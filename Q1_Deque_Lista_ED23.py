class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def addFront(self, item):
        self.items.append(item)
        
    def addRear(self, item):
        self.items.insert(0, item)
        
    #pq o item nao tem self??
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
elemento = input().split()
lista_deque = Deque()
parada = False
while not parada:
    if elemento[0] == "I":
        lista_deque.addFront(elemento[1])
    elif elemento[0] == "F":
        lista_deque.addRear(elemento[1])
    elif elemento[0] == "D":
        print(lista_deque.removeFront())
    elif elemento[0] == "P":
        print(lista_deque.removeRear())
    elemento = input().split()
    if elemento[0] == "X":
        parada = True
 
for i in range(lista_deque.size()):
    print(lista_deque.removeFront())
    