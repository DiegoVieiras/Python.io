#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Me informe sua altura: "))

peso_ideal= (72.7*altura) - 58

print("\nSeu peso ideal é de: ",round(peso_ideal,2))
