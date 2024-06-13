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
    
    

s = Stack()
s.peek()
s.peek()
print(f'Pilha com {s.size()} elementos.')
s.pop()
print(f'Pilha com {s.size()} elementos.')
s.pop()
print(f'Pilha com {s.size()} elementos.')
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(f'Pilha com {s.size()} elementos.')
while not s.isEmpty():
    print(s.pop())
s.pop()
s.push(42)
while not s.isEmpty():
    print(s.pop())