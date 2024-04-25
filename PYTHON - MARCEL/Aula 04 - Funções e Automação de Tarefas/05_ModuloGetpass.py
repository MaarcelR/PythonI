#Modulo GetPass serve para ocultar uma senha. Muito usado para login.
import getpass as gt

username=input("Nome: ")
password=gt.getpass("senha: ")
print(f"Olá {username}, sua senha: {password}")
 
     