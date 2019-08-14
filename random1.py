#randint: generate random integer numbers
#uniform: generate random float numbers 
import os
from random import randint, uniform, random

def Z():
    a = randint(1,5)
    return a

def R():
    b = uniform(1,5)
    return b
os.system("cls")
print("The Z number generated is: ", Z())
print("The R number generated is: ", R())