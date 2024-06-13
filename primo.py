nome, red, green, blue = input().split()
red = int(red)
green =int(green)
blue = int(blue)
red = bin(red)
green =bin(green)
blue = bin(blue)
i = 1
j=0


red = red[2:]
while i > len(red):
    hexa_red0 = red[-i]*(2**i)
    i += 1
    j += 1
    hexa_red = hexa_red0
    if i <  len(red):
        hexa_red1 = red[-i]*(2**i)
        i += 1
        j += 1
        hexa_red = hexa_red + hexa_red1
    if i < len(red):
        hexa_red2 = red[-i]*(2**i)
        i += 1
        j += 1
        hexa_red = hexa_red + hexa_red2
    if i < len(red):
        hexa_red3 = red[-i]*(2**i)
        i += 1
        j += 1
        hexa_red = hexa_red + hexa_red3
    
    if hexa_red == 10:
        hexa_red = "A"
    if hexa_red == 11:
        hexa_red = "B"
    if hexa_red == 12:
        hexa_red = "C"
    if hexa_red == 13:
        hexa_red = "D"
    if hexa_red == 14:
        hexa_red = "E"
    if hexa_red == 15:
        hexa_red = "F"
    if j > 4:   
        hexa_red_final = (f"{hexa_red}{hexa_red_final}")
    else:
        hexa_red_final = (f"{hexa_red}")
print(hexa_red_final)
    


    


