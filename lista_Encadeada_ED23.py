class NodeLista:
    def __int__(self, data):
        self.data = data
        self.next = None


class ListaEncadeada():
    def __int__(self):
        self.head = None
        self.size = 0
        
        
    def append(self, item):
        if self.head:
            pointer = self.head
            while(pointer.next):
                poiter = pointer.next
                
            poiter.next = Node(item)
        else:
            self.head = Node(item)
        self.size = self.size + 1
        
    def insert(self, index, item):
        if index == 0:
            node = Node(item)
            node.next= self.head
            self.head = node
            
        else:
            pointer =self.getnode(index -1)
            node.next = pointer.next
            pointer.next = node
        self.size = self.size + 1
        
        
        
    def index(self, item):
        poiter = self.head
        i= 0
        while(pointer):
            if poiter.data == item:
                return i
            pointer = poter.next
            i = i + 1
            
    def get(self, index):
        pass
    
    def set(self, index, item):
        pass
    
    def getitem(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer= pointer.next
            else:
                raise IndexError("list index out of range")
            
    def setitem(self, index, item):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer= pointer.next
            else:
                raise IndexError("list index out of range")
            
        if pointer:
            pointer.data = item
        else:
            raise IndexError("list index out of range")
        
        
    def remove(self, item):
        if self.head == None:
            raise ValueError ("{} is not in list".format(item))
        elif self.head.data == item:
            self.head = self.head.next
            return True
        else:
            ancestor = self.head
            pointer =self.head.next
            while (pointer):
                if pointer.data == item:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestror = pointer
                pointer= pointer.next
            return True
        raise ValueError("{} is not in list".format(item))
            
            
            
            
lista = ListaEncadeada()
lista.append(40)
lista.appende(9)
lista.append(35)
lista.append(67)
lsita.insert(2,45)
lista.getitem(3)
print(lista)
            
            
    
        