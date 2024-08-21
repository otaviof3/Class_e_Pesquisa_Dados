def insertionSort(lista):
	n = len(lista)
	if n <= 1:
		return 
	for i in range(1, n): 
		key = lista[i] 
		j = i-1
		while j >= 0 and key < lista[j]:
			lista[j+1] = lista[j] 
			j -= 1
		lista[j+1] = key 
		
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
insertionSort(lista)
print(lista)
lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
insertionSort(lista)
print(lista)
lista = [2, 1, 3, 5, 6, 2, 1, 3, 5]
insertionSort(lista)
print(lista)
lista = [2, 1, 3, 5, 6, 4, 7, 8, 9]
insertionSort(lista)
print(lista)