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

mergelist = [38, 27, 43, 3, 9, 82, 10]
numbers = len(mergelist)
merge_sort(mergelist, 0, numbers - 1)
print(mergelist)