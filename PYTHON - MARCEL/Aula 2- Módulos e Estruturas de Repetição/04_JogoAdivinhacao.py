
# import random 


# Randind <inicio><fim>


#Importando a toda a biblioteca Random



# import random 
# numeroAleatorio=random.randint(1,60)
# print(numeroAleatorio)


#usando alias (apelido)

# import random as rd 
# numeroAleatorio=rd.randint(1,2)
# print(numeroAleatorio)







#Importando somente a Bibioteca Randint
# from random import randint as rd
# numeroAleatorio=rd(1,50)
# print(numeroAleatorio)


# import random
# credito=10
# numreroSorteado=random.randint(1,60)

# while True:
#     numero=int(input(f"Teste sua sorte, você tem {credito} tentativas, digite um número: "))
#     if numero == numreroSorteado:
#         print(f"Parabéns, você digitou {numero} e o numero sorteado foi {numreroSorteado}!")
#         break
#     else:
#         credito -= 1 
#         match credito:
#             case 3:
#                 print(f"Errouuuuu, você possui {credito} tentivas!") 
#             case 2:
#                 print(f"Sua sorte está acabando! Você possui {credito} tentativas!") 
#             case 1:
#                 print(f"Last One!!! Só resta {credito} tentativa") 
#             case 0:
#                 tentativas=str(input(f"Ihh parça, suas tentativas acabaram.\n O número sorteado foi {numreroSorteado}\n Quer jogar novamente?\n Digite 'S' para Sim e 'N' para Não: " )).lower()
#                 if tentativas == 's':
#                     credito = 10
#                 else:
#                     print(f" Obrigado por jogar conosco.") 
#                     break
#             case __:
#                 print(f"Shiiiii, você errou! Cuidado pois você tem apenas {credito} tentativas\nE você escolheu o numero {numero}.")
        
        
        
    