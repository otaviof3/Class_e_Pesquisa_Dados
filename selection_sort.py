import time
tempo_i = time.time()
def selectionSort(lista, taman):
    for index in range(taman):
        min_index = index
        for j in range(index + 1, taman):
            if lista[j] < lista[min_index]:
                min_index = j
        (lista[index], lista[min_index]) = (lista[min_index], lista[index])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
taman = len(lista)
selectionSort(lista, taman)
print(lista)
lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
taman = len(lista)
selectionSort(lista, taman)
print(lista)
selectionSort(lista, taman)
lista = [2, 1, 3, 5, 6, 4, 7, 8, 9]
taman = len(lista)
selectionSort(lista, taman)
print(lista)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(tempo)