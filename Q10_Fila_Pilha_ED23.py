num_eq = int(input())

for i in range(num_eq):
    s = Stack()
    cont = 0
    i= 0
    duplicada= False
    expressao=input()
    expressao = list(expressao)
    operacao = False
    
    while i < len(expressao) and not duplicada:
        
        if expressao[i] in "([{":
            s.push(expressao[i])
        elif expressao[i] in ")]}":
            s.pop()
            
        elif expressao[i] in "+-/*":
            operacao = True
            
        i += 1
    if duplicada:
        print("A expressão possui duplicata.")
    else:
        print("A expressão não possui duplicata.")
            