"""Função And(E)"""

"""Situação
Se a média for Maior e igual a 7 E média Menor e igual 10
"Aluno Aprovado"

Se a media for Maior e Igual a 5 E media menor que 7
"Aluno de Recuperação"

se a media for maior e igual que 0 e media menor 5
"aluno reprovado"

senão "Média invalida"

"""
"""
nome=str(input("Nome do aluno: "))

nota1=float(input("nota 1: "))
nota2=float(input("nota 2: "))
nota3=float(input("nota 3: "))
calculo=(nota1+nota2+nota3)/3
media=(float(calculo))

if (media >= 7) and (media <= 10):
  print(f"Aluno {nome} Aprovado! Media: {media:.2f}")
elif (media >= 5) & (media < 7):
    print(f"Aluno {nome} está de recuperação! Media: {media:.2f}")
elif (media>=0) & (media <5):
    print(f"Aluno {nome} está reprovado! Media: {media:.2f}")
else:
    print(f"Media invalida :X")

"""


""" Usando o Comando OR (ou)"""

""" 
lucas = 21
carolina=18

se idade de Lucas for >=18 ou idade carolina for >=18
então "Pelo menos um dos dois são de maior Idade"

"""

    
idade1 = int(input("Digite sua idade Lucas: "))
idade2 = int(input("Digite sua idade Carolina: "))

if (idade1 >= 18) or (idade2 >=18):
    print(f"Pelo menos um dos dois são maior de idade")
else:
    print(f"Idade de Lucas: {idade1} e Idade de Carolina {idade2}")
        