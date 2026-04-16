cp1=float(input("Digite a nota da sua CP1: "))
cp2=float(input("Digite a nota da sua CP2: "))
cp3=float(input("Digite a nota da sua CP3: "))
sp1=float(input("Digite a nota da sua Sprint 1: "))
sp2=float(input("Digite a nota da sua Sprint 2: "))
GS=float(input("Digite a nota da sua GS: "))

if cp1<cp2 and cp1<cp3:
    media1=(cp2 + cp3 + sp1+ sp2)* 0.4 /4
    mediapeso=media1 +(GS*0.6)
    print()
    print(f"A sua média sem os pesos é {media1:.2f}")
    print(f'A sua média com os pesos é {mediapeso:.2f}')
if cp2<cp1 and cp2<cp3:
    media2 = (cp1 + cp3 + sp1 + sp2)* 0.4 /4
    mediapeso2 = media2 + (GS * 0.6)
    print()
    print(f"A sua média sem os pesos é {media2:.2f}")
    print(f'A sua média com os pesos é {mediapeso2:.2f}')
if cp3<cp1 and cp3<cp2:
    media3 = (cp1 + cp2 + sp1 + sp2)* 0.4 /4
    mediapeso3 = media3 + (GS * 0.6)
    print()
    print(f"A sua média sem os pesos é {media3:.2f}")
    print(f'A sua média com os pesos é {mediapeso3:.2f}')
    #aaaaaaaaaaaaaaa

