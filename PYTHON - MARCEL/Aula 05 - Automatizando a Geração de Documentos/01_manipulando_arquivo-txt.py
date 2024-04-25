#Integração com txt e csv


"""Método Open -> Abre um arquivo em txt

arquivo=open('nomedo arquivo.txt,'r')
------------------------------------------

Médotodo With - Abre e fecha a conexão do arquivo

"""

# r - Abrir o arquivo para a leitura(read)
# w -Tem a função substituir conteudo do arquivo 
# a-  Adiciona uma informação no arquivo(append)

#a-  Adiciona uma informação no arquivo(append)


with open('cliente.txt','a') as arquivo:
    arquivo.write("Aula de Python")
    
    
#Substitui o conteudo do arquivo


# with open("text.txt","a") as arquivo:
#     arquivo.write("Criando novo arquivo no Python")


# #Lendo o arquivo

with open('cliente.txt','r') as arquivo:
    linhas=arquivo.readlines()
    # print(arquivo.readlines())  ##sem precisar de variavel.
    for linha in linhas:
        print(linha)