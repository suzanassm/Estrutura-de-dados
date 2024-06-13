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





def conversaoInfixoPosfixo(equacao):
    dic ={} #precedencia dos elemnetos
    dic["*"] = 3
    dic["/"] = 3
    dic["+"] = 2
    dic["-"] = 2
    dic["("] = 1
    
    pilha_operacoes = Stack()
    lista_eq = equacao.split()
    posFixo = []
    
    for elemento in lista_eq:
        if elemento in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or elemento in "0123456789":
            posFixo.append(elemento)
            
        elif elemento == "(":
            pilha_operacoes.push(elemento)
            
        elif elemento == ")":
            topo_pilha = pilha_operacoes.pop()
            while topo_pilha != "(":
                posFixo.append(topo_pilha)
                topo_pilha = pilha_operacoes.pop()
        
        else:
            while (not pilha_operacoes.isEmpty()) and (dic[pilha_operacoes.peek()] >= dic[elemento]):
                posFixo.append(pilha_operacoes.pop())
            pilha_operacoes.push(elemento)
            
    while not pilha_operacoes.isEmpty():
        posFixo.append(pilha_operacoes.pop())
        
    return "".join(posFixo)
            
    
conversaoInfixoPosfixo("10 + 3 * 5 / (16 - 4)")    