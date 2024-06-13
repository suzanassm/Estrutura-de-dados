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







def ConvertorBases(decNumber, base):
    digitos ="0123456789ABCDEF"
    s= Stack()
    while decNumber > 0:
         resto = decNumber%base
         s.push(resto)
         decNumber = decNumber//base
         
    string = ""
    while not s.isEmpty():
        string = string + digitos[s.pop()]
        
    return string



print(ConvertorBases(25,8))
print(ConvertorBases(256,16))
print(ConvertorBases(26,26))
