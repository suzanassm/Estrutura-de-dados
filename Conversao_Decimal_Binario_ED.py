def divPorDois(decNumber):
    s = Stack()
    
    while decNumber > 0:
        rest = decNumber % 2
        s.psuh(rest)
        decNumber = decNumber//2
        
    string = ""
    while not s.isEmpty():
        string = string + str(s.popo())
        
    return string