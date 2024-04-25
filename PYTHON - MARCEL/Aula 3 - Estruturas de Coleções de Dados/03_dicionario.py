"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}


Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""
# compras={"Alface":0.45,
#          "Batata":1.20,
#          "Tomate":8.00,
#          "ovo":13.50,
#          "cenoura":7.22}
# print(compras.keys(),compras.values())
# print(compras.values())



# dadosClientes={"Nome":"Conan",
#                "Endereço":"Avenida Paulista, 1439",
#                "Telefone":"9-99999-9999"
#                }
# #inserir chave e valor no dicionario

# dadosClientes["Idade"]=40
# print(dadosClientes)

# #removendo item do dicionario com POP
# dadosClientes.pop("Nome")
# print(dadosClientes)

#programa com obtencao de preço

compras={"Alface":0.45,
         "Batata":1.20,
         "Tomate":8.00,
         "ovo":13.50,
         "cenoura":7.22}

while True:
    produto= input("Digite o nome do produto, Fim para terminar")
    if produto=="Fim":
        break
    if produto in compras:
        print(f"{produto} é R$ {compras[produto]:.2f}")
    else:
        print("Produto não encontrado")
        