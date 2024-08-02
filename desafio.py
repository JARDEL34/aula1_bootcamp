#Solicitar nome
nome = input("Digite seu nome: ")

#Salario
salario = float(input("Informe seu salário: "))

#Bônus
bonus = float(input("Informe o bônus recebido: "))

#Imprimindo KPI
kpi = 1000 + salario * bonus
print(kpi)

#mensagem
print(f'Ola, {nome}, seu bônus é final é de {kpi}.')
