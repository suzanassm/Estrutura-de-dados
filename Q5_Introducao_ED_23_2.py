num_buracos = int(input())
x_coelho, y_coelho = map(float,input().split())
x_raposa, y_raposa = map(float,input().split())
dist_menor = 100000

for i in range(num_buracos):
    x_buraco, y_buraco = map(float, input().split())
    dist_coelho = ((x_coelho - x_buraco)**2 + (y_coelho - y_coelho)**2)**0.5
    
    
    if dist_coelho <= dist_menor:
        dist_menor = dist_coelho
        x = x_buraco
        y= y_buraco
    
        

dist_raposa = ((x_raposa - x_buraco)**2 + (y_raposa - y_buraco)**2)**0.5
tempo_coelho = dist_coelho
tempo_raposa = dist_raposa/2



if tempo_raposa > tempo_coelho:
    print(f"O coelho pode escapar pelo buraco ({x:.03f}, {y:.03f}).")
else:
    print("O coelho nao pode escapar.")
        
        