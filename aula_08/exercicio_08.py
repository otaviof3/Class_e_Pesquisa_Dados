import time
import math
def buscaBinariaIterativa (lista, x):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = esquerda + (direita - esquerda) // 2
        if lista[meio] == x:
            return meio
        elif lista[meio] < x:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def buscaBinariaRecursiva (lista, x, esquerda, direita):
    if esquerda <= direita:
        meio = esquerda + (direita - esquerda) // 2
        if lista[meio] == x:
            return meio
        elif lista[meio] < x:
            return buscaBinariaRecursiva(lista, x, meio + 1, direita)
        return buscaBinariaRecursiva(lista, x, esquerda, meio - 1)
    return -1

def jumpSearch (lista, x):
    num = len(lista)
    jump = math.sqrt(num)
    anterior = 0
    mini = min(jump, num)
    while mini - 1 < x:
        anterior = jump
        jump += math.sqrt(num)
        mini = min(jump, num)
        if anterior >= num:
            return -1
    i = anterior
    while i < mini:
        if lista[i] == x:
            return i
        i += 1
    return -1

def fibonacciSearch(lista, x):
    n = len(lista)
    fibN2 = 0         
    fibN1 = 1          
    fibN = fibN2 + fibN1  
    while fibN < n:
        fibN2 = fibN1
        fibN1 = fibN
        fibN = fibN2 + fibN1
    offset = -1
    while fibN > 1:
        mini = min(offset + fibN2, n - 1)
        if lista[mini] < x:
            fibN = fibN1
            fibN1 = fibN2
            fibN2 = fibN - fibN1
            offset = mini
        elif lista[mini] > x:
            fibN = fibN2
            fibN1 -= fibN2
            fibN2 = fibN - fibN1
        else:
            return mini
    if fibN1 == 1 and offset + 1 < n and lista[offset + 1] == x:
        return offset + 1
    return -1

def main():
    lista = []
    for v in range(1,10001):
        lista.append(v)

    print(lista[35])

    start_time = time.time()
    print(buscaBinariaIterativa(lista, 36))
    desempenho = time.time() - start_time
    print(desempenho)
    
    start_time = time.time()
    print(buscaBinariaRecursiva(lista, 36, 35, 37))
    desempenho = time.time() - start_time
    print(desempenho)

    start_time = time.time()
    print(jumpSearch(lista, 36))
    desempenho = time.time() - start_time
    print(desempenho)

    start_time = time.time()
    print(fibonacciSearch(lista, 36))
    desempenho = time.time() - start_time
    print(desempenho)

main()