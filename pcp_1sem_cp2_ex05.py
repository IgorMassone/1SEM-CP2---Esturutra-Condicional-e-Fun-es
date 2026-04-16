# Função que aprova o financiamento com base no valor e da idade
def pode_aprovar(idade, renda, valor):
    if idade < 18 or valor > renda * 20:
        return False
    else:
        return True

# Função que define a taxa de juros de acordo como o número de parcelas
def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas == 7 or parcelas <= 12:
        return 0.08
    elif parcelas == 13 or parcelas <= 24:
        return 0.1

def calcular_parcela(valor, taxa, parcela):
    return valor * (((taxa*1+taxa)**parcela)/(1+taxa**parcela-1))

def calcular_total(parcela, parcelas):
    total = parcela * parcelas
    return total

def calcular_juros(total, valor):
    juros = total - valor
    return juros

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda_mensal = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor do valor emprestimo: "))
n_parcelas = int(input("Digite quantas parcelas você deseja (3 a 24): "))

aprovado = pode_aprovar(idade, renda_mensal, valor_emprestimo)

if aprovado:
    taxa = definir_taxa(n_parcelas)
    pmt = calcular_parcela(valor_emprestimo, taxa, n_parcelas)
    total = calcular_total(pmt, n_parcelas)
    juros = calcular_juros(total, valor_emprestimo)

    print(f"Olá {nome}, seu empréstimo de R$ {valor_emprestimo:.2f} com taxa de {taxa * 100}%, \ne valor da parcela fixa de R$ {pmt:.2f} resultou em um valor total de R$ {total:.2f}, com R$ {juros:.2f} de ")
else:
    print("Emprestimo negado >:(")

# FALTA CORRIGIR O VALOR FINAL AAAAAAAAA

