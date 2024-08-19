def bubble(listnumbers):
    for numbers in range(len(listnumbers)-1, 0, -1):
        for i in range(numbers):
            if listnumbers[i] > listnumbers[i+1]:
                    temp = listnumbers[i]
                    listnumbers[i] = listnumbers[i+1]
                    listnumbers[i+1] = temp
    return listnumbers
listnumbers = [7,1,8,9,2,5]
listnumbers = bubble(listnumbers)
print(listnumbers)