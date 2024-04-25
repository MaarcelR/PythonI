"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:


| Menor que 18.5      | Abaixo do peso       |
| >=18.5  E <= 24.9   | Peso Normal          |
| >= 25.0 E <= 29.9   | Excesso de peso      |
| >=30.0  E  <=34.9   | Obesidade classe I   |
| >=35.0  E  <=39.9   | Obesidade classe II  |
|caso contrário sera  | Obesidade classe III |

"""

user=str(input("Nome usuário: "))
peso=float(input("Informe seu peso: "))
idade=int(input("Informe sua idade: "))
altura=float(input("Informe sua altura: "))
calculoImc=float(peso/altura**2)

if (calculoImc < 18.5):
    print(f"Abaixo do peso: {calculoImc:.2f}")
elif (calculoImc >= 18.5) & (calculoImc <=24.9):
    print(f"Peso Normal: {calculoImc:.2f}")
elif (calculoImc >= 25.0) & (calculoImc <=29.9):
    print(f"Excesso de peso: {calculoImc:.2f}")
elif (calculoImc >= 30.0) & (calculoImc <=34.9):
    print(f"Obesidade classe I: {calculoImc:.2f}")
elif (calculoImc >= 35.0) & (calculoImc <=39.9):
    print(f"Obesidade classe II: {calculoImc:.2f}")
else:
    print(f"Obesidade classe III: {calculoImc:.2f}")
    
    
                    
             


