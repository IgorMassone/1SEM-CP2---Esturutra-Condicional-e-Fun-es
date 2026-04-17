nome = input("Digite o seu nome: ")
cargo = input("Digite o seu cargo: ")
salario_base = float(input("Digite sua renda mensal: "))
horas_extras = int(input ("Digite quantas horas extras foram trabalhadas: "))
faltas_mes = int(input("Digite o total de faltas no mês: "))
se_recebou_bonus = input("Digite se recebeu bônus (s ou n): ")

bonus = {"Gerente" : 1000, "Analista" : 500, "Assistente" : 300, "Estágiario" : 100}
valor_hora_extra = 1.5
desconto_falta = 2.0

if se_recebou_bonus == "s":
    se_recebou_bonus = True
elif se_recebou_bonus == "n":
    se_recebou_bonus = False
    
def calcular_horas_extras(salario_base,horas):
    valor_hora = (salario_base/100 * valor_hora_extra)
    return valor_hora * horas
def calcular_desconto_faltas(salario_base, faltas):
    valor_hora = (salario_base/100 * desconto_falta)
    return valor_hora * faltas
def calcular_bonus(cargo, recebeu_bonus):
    valor_bonus = 0
    if recebeu_bonus:
        valor_bonus = bonus[cargo]
    valor_descontado = calcular_desconto_faltas(salario_base, faltas_mes)
    valor_somado = valor_bonus + calcular_horas_extras(salario_base, horas_extras)
    resultado = (salario_base + valor_somado) - valor_descontado
    print (f"Atenção {nome} esses são os valores do seu salário:")
    print(f"Salário Base: {salario_base} | Total de acréscimos: {valor_somado} | Total de descontos: {valor_descontado}")
    print(f"Salário final: {resultado}")

calcular_bonus(cargo, True)
