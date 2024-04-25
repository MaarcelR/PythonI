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
# Cadastro IMC
usuarios=[]

#Loop do Menu Principal

while True: #Enquanto foi verdadeiro exibir o menu
    print("Menu:")
    print("1 - Inserir novo usuário")
    print("2 - Exibir dados do usuário")
    print("3 - Exibir IMC dos usuários")
    print("4 - Deletar usuários")
    print("5 - Sair")
    
    opcao=input("Escolha uma opção:")
    
    if opcao == "1":
        nome=str(input("Digite nome do usuario: "))
        idade=int(input("Digite idade do usuario: "))
        peso=float(input("Digite peso do usuario: "))
        altura=float(input("Digite altura do usuario: "))
        usuarios.append((nome,idade,peso,altura))
        print(f"Usuario {nome} foi inserido com sucesso!")
    elif opcao=="2":
        if usuarios:
            print("Dados dos usuarios")
            for usuario in usuarios:
                nome,idade,peso,altura=usuario
                print(f"Nome: {nome}, Idade: {idade},Peso: {peso}, Altura: {altura} ")
    elif opcao =="3":
        if usuarios:
            print("IMC dos usuários")
            for usuario in usuarios:
                nome,idade,peso,altura=usuario
                imc=peso/(altura**2)
                print(f"{nome}: {imc:.2f}")
                if imc<18.5:
                    print("IMC abaixo do peso")
                elif 18.5 <= imc < 24.9:
                    print("IMC normal")
                elif 24.9 <= imc < 29.9:
                    print("IMC sobre preso")
                elif 29.9 <= imc < 34.9:
                    print("IMC obesidade I")
                elif 34.9 <= imc < 39.9:
                    print("IMC obesidade II")
                else: 
                    print("IMC obesidade III")
    elif opcao =="4":
        if usuarios:
            nomeDeletar=input("Digite nome do usuário a ser deletado: ")
            for usuario in usuarios:
                if usuario[0] == nomeDeletar:
                    usuarios.remove(usuario)
                    print(f"Usuario {nomeDeletar} deletado da lista.")
                    break
            else:
                print(f"Usuário {nomeDeletar} não encontrado") 
        else:
            print("Usuario não encontrado")   
            break          
    else:
        break
        
