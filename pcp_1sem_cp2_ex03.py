cp1=float(input("Digite a nota da sua CP1: "))
cp2=float(input("Digite a nota da sua CP2: "))
cp3=float(input("Digite a nota da sua CP3: "))
sp1=float(input("Digite a nota da sua Sprint 1: "))
sp2=float(input("Digite a nota da sua Sprint 2: "))
GS=float(input("Digite a nota da sua GS: "))

if cp1<cp2 and cp1<cp3:
    mediasempeso1 = (cp2 + cp3 + sp1 + sp2)/4
    mediapeso= mediasempeso1*0.4 + GS*0.6
    print()
    print(f"A sua média sem os pesos é {mediasempeso1:.1f}")
    print(f'A sua média com os pesos é {mediapeso:.1f}')
if cp2<cp1 and cp2<cp3:
    mediasempeso2 = (cp1 + cp3 + sp1 + sp2)/4
    mediapeso2 = mediasempeso2 * 0.4 + (GS * 0.6)
    print()
    print(f"A sua média sem os pesos é {mediasempeso2:.1f}")
    print(f'A sua média com os pesos é {mediapeso2:.1f}')
if cp3<cp1 and cp3<cp2:
    mediasempeso3 = (cp1 + cp2 + sp1 + sp2)/4
    mediapeso3 = mediasempeso3 * 0.4 + (GS * 0.6)
    print()
    print(f"A sua média sem os pesos é {mediasempeso3:.1f}")
    print(f'A sua média com os pesos é {mediapeso3:.1f}')
    #aaaaaaaaaaaaaaa
