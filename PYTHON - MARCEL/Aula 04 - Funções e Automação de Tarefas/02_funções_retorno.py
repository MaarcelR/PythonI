


# Com retorno

# def soma():
#     n1=float(input("numero 1: "))
#     n2=float(input("numero 2: "))    
#     return n1+n2

# def subtracao():
#     n1=float(input("numero 1: "))
#     n2=float(input("numero 2: "))    
#     return n1-n2

# def multiplicacao():
#     n1=float(input("numero 1: "))
#     n2=float(input("numero 2: "))    
#     return n1*n2
    
# def divisao():
#     n1=float(input("numero 1: "))
#     n2=float(input("numero 2: "))    
#     return n1/n2

# def potencia():
#     n1=int(input("numero 1: "))
#     n2=int(input("numero 2: "))    
#     return n1**n2

# while True:
#     escolha=int(input(f"escolha a operacao:\n[1] - Somar\n[2] - Subtrair\n[3] - Multiplicar\n[4] - Dividir\n[5] - Potencia\n[6] - Sair\n"))
#     match escolha:
#         case 1:
#             print(soma())
#         case 2:
#             print(subtracao())
#         case 3:
#             print(multiplicacao())
#         case 4:
#             print(divisao())
#         case 5:
#             print(potencia())
#         case 6:
#             break
#         case _:
#             print("Operacao inválida")
#             break

# def media():
#     nota1=float(input("Nota1: "))
#     nota2=float(input("Nota2: "))
#     nota3=float(input("Nota3: "))
#     nota4=float(input("Nota4: "))
#     media=float((nota1+nota2+nota3+nota4)/4)
#     if media >= 7.00:
#         aprovacao="Aprovado"
#     else:
#         aprovacao="Reprovado"
#     return aprovacao

# media()

# com mais de 1 retorno

#
#  
# Parâmetros x Argumentos
# 
# 

def boasVindas(nome): #incluindo parametro
    return f"bem vindo {nome}!"
print(boasVindas('João Pé de Feijão'))

print("________________________________")

def calculoIMC(peso,altura):
    print(peso/(altura**2))
calculoIMC(70,1.89)

print()

#Criar uma função que multiplique 2 valores: 

def multipliqueDoisValores(valor1,valor2):
    print(valor1*valor2)
multipliqueDoisValores(5,10)

# // ouuuu

def multiplica(a,b):
    return a*b
print(multiplica(10,20))

