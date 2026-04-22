def inserir_valor():
    a = float(input("Digite o primeiro lado do triângulo: "))
    b = float(input("Digite o segundo lado do triângulo: "))
    c = float(input("Digite o terceiro lado do triângulo: "))
    return a, b, c

def reordenar(a, b, c):
#Coloca em uma lista decrescente. Sem o reverse sairia em ordem crescente
    a, b, c = sorted([a, b, c], reverse=True)
    return a, b, c

def calculo(a, b, c):
    if a >= b + c:
        print("Não forma triângulo")
    else:
        if a**2 == b**2 + c**2:
            print("Triângulo Retângulo")

        elif a**2 > b**2 + c**2:
            print("Triângulo Obtusângulo")

        else:
            print("Triângulo Acutângulo")

        if a == b and b == c:
            print("Triângulo Equilátero")
        elif a == b or b == c or a == c:
            print("Triângulo Isóceles")
        else:
            print("Triângulo Escaleno")
        

def main():
    a, b, c = inserir_valor()
    a, b, c = reordenar(a,b,c)
    calculo(a,b,c)

if __name__ == '__main__':
    main()