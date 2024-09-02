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
lista = [10, 24, 6, 36, 12]
shell_sort(lista)
print("Lista ordenada:", lista)