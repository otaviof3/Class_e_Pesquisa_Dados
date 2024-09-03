import time

def insertionSort(lista):
	n = len(lista)
	if n <= 1:
		return lista
	for i in range(1, n): 
		key = lista[i] 
		j = i-1
		while j >= 0 and key < lista[j]:
			lista[j+1] = lista[j] 
			j -= 1
		lista[j+1] = key 
	return lista

def selectionSort(lista):
    taman = len(lista)
    for index in range(taman):
        min_index = index
        for j in range(index + 1, taman):
            if lista[j] < lista[min_index]:
                min_index = j
        (lista[index], lista[min_index]) = (lista[min_index], lista[index])
    return lista

def bubble(listnumbers):
    for numbers in range(len(listnumbers)-1, 0, -1):
        for i in range(numbers):
            if listnumbers[i] > listnumbers[i+1]:
                    temp = listnumbers[i]
                    listnumbers[i] = listnumbers[i+1]
                    listnumbers[i+1] = temp
    return listnumbers

def merge(mergelist, leng, me, merg):
    n1 = me - leng + 1
    n2 = merg - me
    temp1 = [0] * (n1)
    temp2 = [0] * (n2)
    for i in range(0,n1):
        temp1[i] = mergelist[leng + i]
    for j in range(0,n2):
        temp2[j] = mergelist[me + 1 + j]
    i = 0
    j = 0
    k = leng
    while i < n1 and j < n2:
        if temp1[i] <= temp2[j]:
            mergelist[k] = temp1[i]
            i += 1
        else:
            mergelist[k] = temp2[j]
            j += 1
        k += 1
    while i < n1:
        mergelist[k] = temp1[i]
        i += 1
        k += 1
    while j < n2:
        mergelist[k] = temp2[j]
        j += 1
        k += 1

def merge_sort(mergelist, leng, merg):
    if leng < merg:
        me = leng + (merg - leng) // 2
        merge_sort(mergelist, leng, me)
        merge_sort(mergelist, me + 1, merg)
        merge(mergelist, leng, me, merg)
    return mergelist

def shell_sort(lista):
    n = len(lista)
    hki = n // 2
    while hki > 0:
        for i in range(hki, n):
            temp = lista[i]
            j = i
            while j >= hki and lista[j - hki] > temp:
                lista[j] = lista[j - hki]
                j -= hki
            lista[j] = temp
        hki //= 2
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    less = [x for x in lista[1:] if x <= pivot]
    greater = [x for x in lista[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Lista já ordenada #
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8]
tempo_i = time.time()
insertion_lista = insertionSort(lista_ordenada)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {insertion_lista}")

tempo_i = time.time()
selection_lista = selectionSort(lista_ordenada)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {selection_lista}")

tempo_i = time.time()
bubble_lista = bubble(lista_ordenada)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {bubble_lista}")

tempo_i = time.time()
numbers = len(lista_ordenada)
merge_lista = merge_sort(lista_ordenada, 0, numbers - 1)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {merge_lista}")

tempo_i = time.time()
shell_lista = shell_sort(lista_ordenada)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {shell_lista}")

tempo_i = time.time()
quick_lista = quick_sort(lista_ordenada)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {quick_lista}")

# Lista com elementos na ordem inversa #
lista_inversa = [8, 7, 6, 5, 4, 3, 2, 1]
tempo_i = time.time()
insertion_lista = insertionSort(lista_inversa)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {insertion_lista}")

tempo_i = time.time()
selection_lista = selectionSort(lista_inversa)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {selection_lista}")

tempo_i = time.time()
bubble_lista = bubble(lista_inversa)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {bubble_lista}")

tempo_i = time.time()
numbers = len(lista_inversa)
merge_lista = merge_sort(lista_inversa, 0, numbers - 1)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {merge_lista}")

tempo_i = time.time()
shell_lista = shell_sort(lista_inversa)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {shell_lista}")

tempo_i = time.time()
quick_lista = quick_sort(lista_inversa)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {quick_lista}")

# Lista com elementos repetidos #
lista_repetidos = [5, 10, 5, 1]
tempo_i = time.time()
insertion_lista = insertionSort(lista_repetidos)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {insertion_lista}")

tempo_i = time.time()
selection_lista = selectionSort(lista_repetidos)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {selection_lista}")

tempo_i = time.time()
bubble_lista = bubble(lista_repetidos)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {bubble_lista}")

tempo_i = time.time()
numbers = len(lista_repetidos)
merge_lista = merge_sort(lista_repetidos, 0, numbers - 1)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {merge_lista}")

tempo_i = time.time()
shell_lista = shell_sort(lista_repetidos)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {shell_lista}")

tempo_i = time.time()
quick_lista = quick_sort(lista_repetidos)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {quick_lista}")

# Lista aleatória #
lista_aleatoria = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
tempo_i = time.time()
insertion_lista = insertionSort(lista_aleatoria)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {insertion_lista}")

tempo_i = time.time()
selection_lista = selectionSort(lista_aleatoria)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {selection_lista}")

tempo_i = time.time()
bubble_lista = bubble(lista_aleatoria)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {bubble_lista}")

tempo_i = time.time()
numbers = len(lista_aleatoria)
merge_lista = merge_sort(lista_aleatoria, 0, numbers - 1)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {merge_lista}")

tempo_i = time.time()
shell_lista = shell_sort(lista_aleatoria)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {shell_lista}")

tempo_i = time.time()
quick_lista = quick_sort(lista_aleatoria)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(f"Tempo: {tempo} e Lista: {quick_lista}")