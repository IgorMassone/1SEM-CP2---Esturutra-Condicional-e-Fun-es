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
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.1

# Função que calcula a taxa fixa a partir de
def calcular_parcela(valor, taxa, parcela):
    return valor * ((taxa * (1 + taxa) ** parcela) / ((1 + taxa) ** parcela - 1))

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda_mensal = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor do valor emprestimo: "))
n_parcelas = int(input("Digite quantas parcelas você deseja (3 a 24): "))

aprovado = pode_aprovar(idade, renda_mensal, valor_emprestimo)

if aprovado:
    taxa = definir_taxa(n_parcelas)
    pmt = calcular_parcela(valor_emprestimo, taxa, n_parcelas)
    total_pago = calcular_total(pmt, n_parcelas)
    total_juros = calcular_juros(total_pago, valor_emprestimo)

    print(f"Olá {nome}!\nEmpréstimo de: R$ {valor_emprestimo:.2f}\nTaxa aplicada: {taxa * 100:.1f}% ao mês\nParcelas: {n_parcelas}x de R${pmt:.2f}\nValor Total Final: R$ {total_pago:.2f}\nTotal pago em juros: R$ {total_juros:.2f}")
else:
    print(f"Sinto muito, {nome}. Empréstimo negado com base nos critérios de idade ou renda.")
