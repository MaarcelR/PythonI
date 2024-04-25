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
estoque=[]

#Loop do Menu Principal

while True: #Enquanto foi verdadeiro exibir o menu
    menu=int(input('''
    ------------ Menu ----------
    [1] Cadastrar Produto   
    [2] Atualizar Produto
    [3] Remover Produto
    [4] Mostrar Estoque
    [5] Realizar Venda
    [6] Sair              
    
    Opção:  '''))
    
    if menu==1: 
        produtos = dict(
            nomeProduto=str(input("Produto: ")),
            precoUnitario=float(input("Preço: ")),
            quantidadeEstoque=int(input("Quantidade:"))
        )
        estoque.append(produtos)

        print("Produto foi inserido com sucesso!")
    elif menu== 2:
        if estoque:
            produtoAlterado=input("Qual produto você deseja alterar: ")
            precoAlterado=float(input("Qual valor do produto: "))
            quantidadeAlterada=int(input("Quantidade alterada: "))
            for produto in estoque:
                nomeProduto,precoUnitario,quantidadeEstoque=produto
                if produto["nomeProduto"] == produtoAlterado:
                   produto["precoUnitario"] = precoAlterado
                   produto["quantidadeEstoque"] = quantidadeAlterada
        else:
            print("Produto nao cadastrado")    
    elif menu ==3:
        nomeDeletar=str(input("Escolha o produto a ser excluído: ")).title()
        for produto in estoque:
            nomeProduto,precoUnitario,quantidadeEstoque=produto
            if produto["nomeProduto"] == nomeDeletar:
                    estoque.remove(produto)
                    print(f"Produto {nomeDeletar} deletado da lista.")
        else:
            print("Produto não está no estoque")
    elif menu ==4:
        for produto in estoque:
            print ("------------------------------------")
            print ("Produto: ",  produto["nomeProduto"])
            print ("Preço: ",  produto["precoUnitario"])
            print ("Estoque: ",  produto["quantidadeEstoque"])
            print ("------------------------------------")
    elif menu ==5:
        produtoVendido =str(input("Qual foi o produto vendido: "))
        quantidadeVendida=int(input("Quantidade vendida: "))
        for produto in estoque:
            nomeProduto,precoUnitario,quantidadeEstoque=produto
            if produto["nomeProduto"] == produtoVendido:
                produto["quantidadeEstoque"] -= quantidadeVendida
                valorTotal =produto["precoUnitario"]*quantidadeVendida
                print(f"\nO produto vendido foi uma {produtoVendido}\n e o valor total da compra foi de R${valorTotal:.2f}")
    else:
        print("Opcao inválida")
        break            
                    
                    
    # elif menu == 3:
    #     if produtos:
    #         print("IMC dos usuários")
    #         for usuario in usuarios:
    #             nome,idade,peso,altura=usuario
    #             imc=peso/(altura**2)
    #             print(f"{nome}: {imc:.2f}")
    #             if imc<18.5:
    #                 print("IMC abaixo do peso")
    #             elif 18.5 <= imc < 24.9:
    #                 print("IMC normal")
    #             elif 24.9 <= imc < 29.9:
    #                 print("IMC sobre preso")
    #             elif 29.9 <= imc < 34.9:
    #                 print("IMC obesidade I")
    #             elif 34.9 <= imc < 39.9:
    #                 print("IMC obesidade II")
    #             else: 
    #                 print("IMC obesidade III")
    # elif menu == 4:
    #     if produtos:
    #         nomeDeletar=input("Digite nome do usuário a ser deletado: ")
    #         for usuario in usuarios:
    #             if usuario[0] == nomeDeletar:
    #                 usuarios.remove(usuario)
    #                 print(f"Usuario {nomeDeletar} deletado da lista.")
    #                 break
    #         else:
    #             print(f"Usuário {nomeDeletar} não encontrado") 
    #     else:
    #         print("Usuario não encontrado")   
    #         break          
    # else:
    #     break
        
