qntd_lesma = int(input())
velo_1 = 0
velo_2 = 0
velo_3 = 0
for i in range(qntd_lesma):
    velo = int(input())
    if velo < 10:
        if velo_1 < velo:
            velo_1 = velo
    if velo >= 10 and velo < 20:
        if velo_2 < velo:
            velo_2 = velo
    if velo >= 20:
        if velo_3 < velo:
            velo_3 = velo
            
print(velo_1, velo_2, velo_3)