#Defina uma função nova chamada do_four que receba um objeto de função e um
#valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve
#haver só duas afirmações no corpo desta função, não quatro.

def print_twice(teste):
    print(teste)
    print(teste)

def do_twice(f):
    print(f)
    print(f)

def do_four(A):
    print((A) * 4)
   

def print_spam():
    print('spam')
    
do_four('spam')
