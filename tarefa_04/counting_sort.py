def max_heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2 
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        max_heapify(arr, n, largest)

def heap_sort_max(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        max_heapify(arr, i, 0)

def min_heapify(arr, n, i):
    smallest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  
        min_heapify(arr, n, smallest)

def heap_sort_min(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        min_heapify(arr, i, 0)

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

arr = [7, 5, 4, 1, 2, 0]
heap_sort_max(arr)
print("HeapSort com Heap Máximo:", arr)

arr = [7, 5, 4, 1, 2, 0]
heap_sort_min(arr)
print("HeapSort com Heap Mínimo:", arr)

arr = [7, 5, 4, 1, 2, 0]
counting_sort(arr)
print("Counting Sort:", arr)