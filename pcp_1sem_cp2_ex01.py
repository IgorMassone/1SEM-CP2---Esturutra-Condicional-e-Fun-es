def receber_dados():
    peso_t = float(input("Digite o peso da carga em T: "))
    estado = int(input("Digite o estado de origem (1-5): "))
    codigo = int(input("Digite o código da carga (10-40): "))
    return peso_t, estado, codigo

def converter_peso(peso_t):
    peso_t = peso_t * 1000
    return peso_t

def preco_carga(codigo, peso):
    if 10 <= codigo <= 20:
        preco = peso * 100
    elif 21 <= codigo <= 30:
        preco = peso * 250
    elif 31<= codigo <= 40:
        preco = peso * 340
    else:
        return 0
    return preco

def calculo_imposto(estado, preco):
    if estado == 1:
        imposto = preco * 0.35
    elif estado == 2:
        imposto = preco * 0.25
    elif estado == 3:
        imposto = preco * 0.15
    elif estado == 4:
        imposto = preco * 0.05
    elif estado == 5:
        return 0
    return imposto



def main():
    peso_t, estado, codigo = receber_dados()
    peso = converter_peso(peso_t)
    preco = preco_carga(codigo,peso)
    imposto = calculo_imposto(estado,preco)
    total = imposto + preco

    print(f"Peso em KG {peso:.0f}")
    print(f"Preço da carga R${preco:.2f}")
    print(f"Imposto R${imposto:.2f}")
    print(f"Valor total R$ {total:.2f}")

if __name__ == '__main__':
    main()