"""
FUNÇÔES
Uma forma de organizar o código e garantir que ele 
possa ser reutilizado. Ideal que cada função seja 
responsável por uma tarefa...



>>>Sintaxe:
def nome_da_funcao(parametros):
    # Corpo da função
    # Instruções a serem executadas
    return valor_retornod
"""

# def: Palavra-chave usada para definir uma função.
# nome_da_funcao: Nome dado à função para chamá-la posteriormente.
# parametros: Argumentos que a função pode receber (opcionais).
# return: Palavra-chave usada para retornar um valor da função (opcional).
    
    
    
    
# # Função diz oi
# def aprendaDizerOi():
#     print("oi")

# aprendaDizerOi()







# Função canta parabéns

# def cantandoParabens():
#     print("Parabens pra você\n"
#           "Nessa data querida\n"
#           "muitas felicidades\n"
#           "muitos anos de vida!!")
# cantandoParabens()




# Função soma 2 valores

# def soma():
#     a=10
#     b=20
#     calc = a + b
#     print(f"Soma é: {calc}")
# soma()

'''1 -Exercicio : Média :Crie uma Função que Peça para o Usuario Entrar com 4 Notas, Se for >=7 aprovado Se não Reprovado '''


# def media():
#     nota1=float(input("Nota1: "))
#     nota2=float(input("Nota2: "))
#     nota3=float(input("Nota3: "))
#     nota4=float(input("Nota4: "))
#     media=float((nota1+nota2+nota3+nota4)/4)
#     if media >= 7.00:
#         print("Aprovado")
#     else:
#         print("Reprovado")


# media()



# 2-'''Exercicio:IMMC: Crie a entrada do usuário com Peso e Altura , faça o calculo do IMMC e mostre o resultado '''


def calcIMC():
    peso=float(input("Peso: "))
    altura=float(input("altura: "))
    
    imc=peso/(altura**2)
    print(f"Resultado IMC: {imc:.2f}")
    
calcIMC()