#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
#cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print("Informa a quantidade de metros quadrados: ")
mq = float(input())

cobert = int (mq / 3)
tot_lata = int (cobert/18)

if (cobert < 18 ):
    tot_lata = tot_lata + 1 
else: 
  if (cobert % 18 !=0):
    tot_lata = tot_lata + 1 
  else: 
    if (cobert % 18 ==0):
      tot_lata = tot_lata    
  
tot_prec = float (tot_lata * 80)

print("\nTotal de latas a serem compradas ", (tot_lata))
print("\nO preço final total : R$", round(tot_prec,2))
