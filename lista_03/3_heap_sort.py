def heapify(lista, n, i):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  
    if left < n and lista[left] > lista[largest]:
        largest = left
    if right < n and lista[right] > lista[largest]:
        largest = right
    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]  
        heapify(lista, n, largest)

def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  
        heapify(lista, i, 0)
    return lista
lista = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
heap_lista = heap_sort(lista)
print(heap_lista)