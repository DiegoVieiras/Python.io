#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
#que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7

h = float(input("Me informe a altura por favor: "))

homens = (72.7*h) - 58
mulheres = (62.1*h) - 44.7

print("\nPeso ideal para homens: ",round(homens,2))
print("\nPeso ideal para mulheres: ",round(mulheres,2))
