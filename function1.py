#Function1: Mult. two numbers

#Libraries#################
import os
#Functions#################
def calc(a, b):
    add = a + b
    return add

#Main######################
os.system("cls")
print("Press number 1: ")
n1 = int(input())
n2 = int(input("Press number 2: "))
print("The answer is: ", calc(n1,n2))