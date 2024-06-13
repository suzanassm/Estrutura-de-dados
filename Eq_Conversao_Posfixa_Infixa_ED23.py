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







def PosfixoInfixoConverte(equacaoPos):
    equacaoPos = equacaoPos.split()
    pilha_operacoes = Stack()
    
    for elemento in equacaoPos:
        if elemento in"0123456789":
            pilha_operacoes.push(int(elemento))
            
        else:
            opr1 = pilha_operacoes.pop()
            opr2 = pilha_operacoes.pop()
            resultado = operacao(elemento, opr1, opr2)
            pilha_operacoes.push(resultado)
            
    return pilha_operacoes.pop()

def operacoes(op, opr1, opr2):
    if op == "*":
        return opr1*opr2
    elif op =="/":
        return opr1/opr2
    elif op == "+":
        return opr1 + opr2
    else:
        return opr1 - opr2
    
    
PosfixoInfixoConverte("17 10 + 3 * 9 /")    
