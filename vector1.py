'''
    Escriba un programa que reciba en una lista de 10 numeros
    ingresados por el usuario desde consola.
'''
N = []
i = 1
'''Create list'''
while i <= 10 :
    print("Press number ", i ,": ")
    X = int(input())
    N.append(X)
    i = i + 1

'''Show list'''
i = 0
while i < 10:
    print("The value in the pos", i ,"is: ", N[i])
    i = i + 1

N.__len__()

