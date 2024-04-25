"""
Operadores Aritméticos e lógicos:

+  Adição           *  Multiplicação
-  Subtração        ** Exponenciação

/  Divisão
// Retorna o valor inteiro da divisão
%  Retorna o resto da divisão

>   Maior           ==  Igual
<   Menor           !=  Diferente

>=  Maior ou igual
<=  Menor ou igual
=   Atribuição
"""

# a = 2
# b = 3

# print(a + b)   # adição
# print(a - b)   # subtrair

# print(a * b)   # multiplicar
# print(a ** b)  # exp

# print(a / b)   # divisão
# print(a // b)  # divisão com valor inteiro
# print(a % b)   # resto da divisão

# print(a > b)   # [a] é maior que [b]?
# print(a <= b)  # [a] é menor ou igual [b]?
# print(a == b)  # [a] é igual [b]?
# print(a != b)  # [a] é diferente de [b]?


#Criar uma soma com dois Valores exibir para o usuario  
valorA = 500
valorB = 300
resultado = valorA + valorB
print (f'a Soma dos valores: {valorA} + {valorB} é igual a {resultado}')



#Cálculo de Media com duas notas exibir para o usuario o resultado da média

nota1 = 5 
nota2 = 5.3
media = (nota1+nota2) / 2

print(f"As notas do aluno foram: {nota1} e {nota2}, e a média das notas é {media:.0f}")  #notacao para incluir ou retirar casa decimal :.0f

# – Cálculo de aumento de salário
funcionario = "Marcos Guilherme"
salario = 10000.52
aumento = 0.35
aumentopercentual = (aumento*100)
salarioAtualizado = (salario*aumento)+salario
print(salarioAtualizado)

print(f'O funcionário: {funcionario}, teve um aumento salarial de {aumentopercentual:.0f}%, seu salario era de {salario} e agora seu novo salario é de {salarioAtualizado:.2f}')