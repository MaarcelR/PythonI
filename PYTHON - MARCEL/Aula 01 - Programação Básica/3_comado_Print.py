"""

Print:
    Função responsável por imprimir informações no console
"""

# print("ola mundo!")

#Armazenar um Numero(Int)
#valor=100
# print( valor)
#Armazena um Texto (String)
# curso='curso de Phyton'
# aluno="Marcel Rosa"
# print("Você está realizando: " + curso , "e o nome do aluno é: " , aluno  )

#Armazenar um Float(.)

# valorCurso = 1400.05
# descontoOferecido= 0.05

# print(f"o valor do curso é {valorCurso}, desconto oferecido é de {descontoOferecido}")



# Fstring (Mais usual)

# aluno="Camila Noronha"
# curso="mecanica"
# local="av. paulista"

# print(f'O(a) aluno(a) é {aluno}, esta fazendo curso de {curso} na {local}')

# nome= "Marcel"
# sobrenome = "Rosa"
# idade=37
# endereco="av elisio teixeira leite, 1000"

# print(f'Nome do usuário: {nome} {sobrenome},\n tem {idade} anos de idade e\n mora em {endereco}')



"Funções de Formatações "
#upper , Lower ,c , capitalize

nome="CUrso dE PHyToN"
nomeMinusculo = nome.lower()
nomeMaiusculo = nome.upper()
nomePrimeiraLetraMaiusculo = nome.title()
nomePrimeiraLetraFraseMaiusculo = nome.capitalize()
print(f'Texto da forma que escreveu: {nome}\nTexto em minusculo: {nomeMinusculo}\nTexto em maiusculo: {nomeMaiusculo}\nPrimeira letra maiusculo: {nomePrimeiraLetraFraseMaiusculo}\nPrimeira letra frase maiusculo: {nomePrimeiraLetraMaiusculo}')

# print(nome.lower()) #minusculo
# print(nome.upper()) #minusculo
# print(nome.title()) #cada primeira letra maiusculo
# print(nome.capitalize()) #primeira letra da frase maiusculo

