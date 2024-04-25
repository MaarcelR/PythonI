"""
While >>> Permite que você crie um programa que execulte  repetições(loops) 
diversas vezez dependendo de uma condição.

vezes será repetido.
* Necessário atentar para o critério de parada.(loop infinito)

Sintaxe >>>  while <condição>:
                    bloco
  
"""

#Lógica 
"""
    variavel X que armazena um valor 1
    Enquando X for menor e igual a 3:
    Faça
       
"""
#exemplo

# x=1
# while x<=3:
#     print(f"valor de x é: {x}")
#     x = x+1
    
    
    
    
    
#Contatadores - Usado como Incremento da variavel ate  que seja Verdadeiro

#Exemplo


"""Interrompendo a repetição com TRUE e Break """

while True:
    resposta=str(input("Digite 'sair' para parar o programa! ")).lower()
    if resposta == 'sair':
        print(f"você digitou {resposta}, finalizando o programa")
        break
    else:
        print(f"você digitou {resposta}")
        
    

