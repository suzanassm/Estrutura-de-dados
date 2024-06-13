class Stcak():
    def __init__(self):
        self.lista = []
        
    def push(self, item):
        self.lista.insert(0, item)
        
    def pop(self):
        return self.lista.pop(0)
        
        
    def peek(self):
        return self.lista[0]
    
    def isEmpty(self):
        return self.lista == []
    
    def size(self):
        return self.len(self.lista)
    