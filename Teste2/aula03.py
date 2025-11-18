import random
import math
import datetime

def imprimir():
    print("Função sem parâmetro")
imprimir ()

def somar (a, b):
    return a + b

def multiplicacao (x, y):
    resultado = x * y
    return resultado

print(somar(5, 2))
print(multiplicacao(4, 3))

print (random.randint(1, 100))
print (math.sqrt(121))

print (datetime.datetime.now())