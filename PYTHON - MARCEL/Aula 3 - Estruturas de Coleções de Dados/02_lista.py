"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

"""

# *Criar uma lista de Produtos*
# produtos=["Bacon",08.20,"Ovos",10.20,"Picanha",76.00,"Pão",05.50,"Cebola",00.25]
# print(produtos) 

#Acesso ao elementos da lista
# print(f"O produto é {produtos[4]}, R$ {produtos[5]}") ### O produto é Picanha, R$ 76.0


"""Fatiamento de itens da Lista"""

#obter os dois primeiro elementos da lista [: indice]

# print(produtos[:2]) ### ['Bacon', 8.2]

#obter os elementos após o segundo elemento [indice :]
# print(produtos[2:])  ###['Ovos', 10.2, 'Picanha', 76.0, 'Pão', 5.5, 'Cebola', 0.25]



#Obter Trechos de uma Lista [indice inicial :indice final]

# print(produtos[4:6]) ### ['Picanha', 76.0]

"""acessar os elementos de uma  lista usando indice negativo """

# print(produtos[-6:-4])  ### ['Picanha', 76.0]

#APPEND >>> Atribui a lista, um elemento por vez (no final da lista)

# nomes=["Chaves","Kiko","Chiquinha","Seu Madruga","Sr. Barriga"]
# nomes.append("Popis")
# nomes.append("Girafales")
# nomes.append("Godinez")

# print(nomes) ### ['Chaves', 'Kiko', 'Chiquinha', 'Seu Madruga', 'Sr. Barriga', 'Popis', 'Girafales', 'Godinez']

#INSERT >>> Atribui vários elementos, integrando à lista original.

# nomes.insert(0,"Nhonho")
# print(nomes) ###['Nhonho', 'Chaves', 'Kiko', 'Chiquinha', 'Seu Madruga', 'Sr. Barriga', 'Popis', 'Girafales', 'Godinez']

#POP >>> Remove um valor da lista por índice.

# nomes.pop(0)
# print(nomes) ###['Chaves', 'Kiko', 'Chiquinha', 'Seu Madruga', 'Sr. Barriga', 'Popis', 'Girafales', 'Godinez']


#REMOVE >>> Remove um valor da lista por valor.
# nomes.remove("Chaves")
# print(nomes)



#CLEAR >>> Limpa a lista.

# nomes.clear()
# print(nomes)


#SORT >>> Ordena os dados de uma lista.

# nomes.sort()
# print(nomes)


#REVERSE >>> Inverte a lista.


# nomes.reverse()
# print(nomes)


#Interar os itens de uma lista 


# personagens=["Chaves","Kiko","Chiquinha","Seu Madruga","Sr. Barriga"]
# personagens.sort()
# for nome in personagens:
#         print(nome)

# nomes =[]
# for nome in range(5):
#         nomes.append(str(input("Nome: ")))
#         print(nomes)
#         if nome == 4:
#            print (nomes)

#Funções (Sum,Max,Min,Len,Count,Sort, Reverse)

# numbers=[1,1,1,1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
# print(sum(numbers))

# print(max(numbers))

# print(min(numbers))

# print(len(numbers))

# print(numbers.count(1))


# varias listas 

produto1=['Ovos', 10.2, 'Picanha', 76.0, 'Pão', 5.5, 'Cebola', 0.25]
produto2=['Camiseta',99.00,'Bermuda',120.00,'Cueca',35.00,'Meia',15.00]
produto3=['Relogio',199.00,'Televisão',1120.00,'VideoGame',3435.00,'Geladeira',5415.00]

# compras=[produto1,produto2,produto3]
# compras.sort()
# print(compras)

#juntar lista
# compras=produto1+produto3
# print(compras)

#Listar usando instrutura IF
for i in produto2:
        if i == "Cueca":
                print(produto2)
                break

