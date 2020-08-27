#Faça um Programa que pergunte quanto você ganha por hora 
#e o número de horas trabalhadas no mês. Calcule e mostre
#o total do seu salário no referido mês, sabendo-se que são
#descontados 11% para o Imposto de Renda, 8% para o INSS e
#5% para o sindicato, faça um programa que nos dê:

# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

Horast = int (input("Me informe suas horas trabalhadas: "))
salh = float (input("Quanto você ganha por hora?: "))

salb = Horast * salh

inss = salb * 8/100
imp_r = salb * 11/100
sindi = salb * 5/100

sal_liq = salb - inss - imp_r - sindi

desc_tot = inss + imp_r + sindi

print("\na. Seu salario bruto é de: R$", salb)
print("b. Você pagou ao INSS: R$", inss)
print("c. Você pagou ao sindicato: R$", sindi)
print("d. Seu salário liquido é de: R$", sal_liq)
print("e. Seus descontos totais foram", desc_tot, "e seu salário liquido ficou R$", sal_liq)
