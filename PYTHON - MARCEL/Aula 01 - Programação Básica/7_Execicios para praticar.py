"""
1 -Vamos iniciar um programa que faça entrada com o usuario que receba:
nome
idade
peso
altura

Retorne o IMC do usuário.

IMC =   Peso
      --------
       Altura²
"""

# nome=str(input("Nome: "))
# idade=int(input("Idade: "))
# peso=float(input("Peso: "))
# altura=float(input("Altura: "))

# imc=peso/(altura**2)

# print(f'Olá {nome}, você tem {idade} anos,  seu peso é de {peso:.0f}kg, altura de {altura:.2f}m e seu IMC é de {imc:.2f}')


"""
2-Considere um programa que solicite a entrada do nome de uma pessoa e  seu ano de nascimento e apresente
a sua idade usando as variaveis nome, ano_nasc, ano_atual e variável idade para armzenar o calculo da idade.

"""

# nome=str(input("Nome: "))
# ano_nasc=int(input("Ano Nascimento: "))
# ano_atual = 2024
# idade = ano_atual - ano_nasc

# print(f'Ola {nome}, com as informações relatadas, esse ano você completa ou já completou {idade} anos ')


"""
3-O Programa Seguinte deve calcular o salário líquido de um profissional que trabalhe por hora.
Para tanto é necessário possuir alguns dados básicos, tais como:
valor hora , numero de horas trabalhada no mês , Percentual de Desconto do INSS
Apresentar os resultados do salário bruto do valor descontato e do salário Liquido.      

"""

valorHora =float(200.00) 
horasTrabalhadasMes =float(60.59) 
percentualDescontoInss = float(0.30)


salarioBruto = valorHora*horasTrabalhadasMes
valorDesconto = salarioBruto * percentualDescontoInss
salarioLiquido = salarioBruto - valorDesconto
# print(f"horas trabalhadas dentro do mês = {horasTrabalhadasMes:.2f}\n salario bruto = {salarioBruto:.2f} \n valor desconto = {valorDesconto:.2f} \n salario liquido = {salarioLiquido:.2f}")

print(f'Ola, funcionário!! \n Suas horas trabalhadas no último mês foi: {horasTrabalhadasMes:.2f}\n Seu salario bruto foi de: {salarioBruto:.2f}\n Desconto INSS: {valorDesconto:.2f}\n Seu salario liquido foi de {salarioLiquido:.2f}')