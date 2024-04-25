"""
IF, ELSE, ELIF
Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Sintaxe:

if (teste):
    Bloco que será executado se o teste retornar True
    
Exemplo de aplicação: 
"""

# Condição simples (IF)
'''
Programa - Verificando Se a idade inserida é maior ou igual a 18
'''

# idade =int(input("Idade: "))

# if (idade > 18):
#     print(f"Você atingiu a maioridade: Você tem {idade} anos")


# Condição composta (If/else)
"""Programa - Verificar: Se a idade é maior ou igual a 18 , exibir "Maior Idade" caso contrario
será de Menor Idade """

# idade =int(input("Idade: "))

# if (idade > 18):
#     print(f"Você atingiu a maioridade: Você tem {idade} anos")
# else:
#     print(f"Ainda falta um tempo para atingir a maioridade. Você ainda tem {idade} anos")






# Condição Aninhada (If/Elif/Else)

"""Programa - Se a idade for maior e igual a 18,"maior idade"
              Se a idade for  igual a 16 "você esta quase lá"
              caso contrário "você é menor de idade"
"""

idade = int(input("Idade: "))
if (idade >= 18):
    print(f"Você atingiu a maioridade: Você tem {idade} anos")
elif (idade == 16):
    print(f"Você está quase lá. Você ainda tem {idade} anos")
else:  
    print(f"Calma pequeno gafanhoto. Você ainda tem {idade} anos")
