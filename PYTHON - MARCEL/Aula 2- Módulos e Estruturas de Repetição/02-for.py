"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> inicio, fim, passo
"""
# sintaxe

# for contagem in range(0,20,2):
#     print(contagem)
     

   
    

'''
Crie um sistema que receba 4 notas 
usar uma variavel soma para acumula as notas e 
calcule a média, ao fim apresente a média e situção
do aluno, sendo:
> 7 aprovado, > 5 em recuperação e < 5 reprovado.
'''
soma=0
for mediaAluno in range(1,5):
    nota=float(input(f"Digite nota{mediaAluno}:"))
    soma += nota
media = soma/mediaAluno
print(f"media final foi de: {media:.2f}")
if media >=7:
    print("Aprovado")
elif media >5 and media <7:
    print("em recuperação")
else:
    print("reprovado")
        

    


    
