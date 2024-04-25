"""1.Uma escola precisa de um software que calcule a 
média de alunos. 
Para isso o software deve receber o nome e três 
notas dos alunos. Com estes dados o software deve imprimir:
| ---------------------------------- | 
| Média	    | Imprimir               | 
| ---------------------------------- | 
| ==10	    | Aprovado com Distinção |
| >=7	    | Aprovado!              |
| >=5   	| Em exame               |
| <5	    | Reprovado              |
| ---------------------------------- | 
"""
nome=str(input("Nome do aluno: "))

nota1=float(input("nota 1: "))
nota2=float(input("nota 2: "))
nota3=float(input("nota 3: "))
calculo=(nota1+nota2+nota3)/3
media=(float(calculo))

if media == 10:
  print(f"Aprovado com Distinção {media:.2f}")
elif media>=7:
    print(f"Aprovado!{media:.2f}")
elif media>=5:
    print(f"Shiii, em exame {media:.2f}")
elif media<5:
    print(f"Ai ai ai, reprovou meu xegado, sua média foi:  {media:.2f}")
    

