nome=str(input("Digite seu nome: "))
empresa=str(input("Digite a empresa que vc trabalha: "))
cargo=str(input("Digite seu cargo: "))
salarioBruto=float(input("Digite salario Bruto: "))
deducaoIr=float
baseCalculo=float
aliquota=float
salarioLiquido=float


if  salarioBruto <= 1903.98:
    aliquota = 0.00
    deducaoIr = 0.00
elif salarioBruto >= 1903.99 and salarioBruto <= 2826.65:
    aliquota = 0.075
    deducaoIr = 142.80
elif salarioBruto >= 2826.66 and salarioBruto <= 3751.05:
    aliquota = 0.15
    deducaoIr = 354.80
elif salarioBruto >= 3751.06 and salarioBruto <= 4664.68:
    aliquota = 0.225
    deducaoIr = 636.13
else:
    aliquota = 0.275
    deducaoIr = 869.36
        
        
ir=(salarioBruto*aliquota)-deducaoIr        
salarioLiquido=salarioBruto-ir
        
print(f" Ola {nome},\n você trabalha na empresa:{empresa}\n seu cargo atual é: {cargo}\n seu salario bruto é de R${salarioBruto:.2f}\n você entrou na alíquota de: {aliquota*100:.2f}%\n e seu salario líquido após descontos de IR é de: {salarioLiquido:.2f}\n parcela a deduzir ficou no valor de R$:{deducaoIr:.2f}")        
        
    
