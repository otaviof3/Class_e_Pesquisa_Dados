import time
tempo_i = time.time()
def bubble(listnumbers):
    for numbers in range(len(listnumbers)-1, 0, -1):
        for i in range(numbers):
            if listnumbers[i] > listnumbers[i+1]:
                    temp = listnumbers[i]
                    listnumbers[i] = listnumbers[i+1]
                    listnumbers[i+1] = temp
    return listnumbers
inverselist = [9,8,7,6,5,4,3,2,1]
inverselist = bubble(inverselist)
print(inverselist)
orderlist = [1,2,3,4,5,6,7,8,9]
orderlist = bubble(orderlist)
print(orderlist)
repeatlist = [7,1,8,9,2,5,7,1,8]
repeatlist = bubble(repeatlist)
print(repeatlist)
randomlist = [7,1,8,9,2,5,3,8,2]
randomlist = bubble(randomlist)
print(randomlist)
tempo_f = time.time()
tempo = tempo_f - tempo_i
print(tempo)