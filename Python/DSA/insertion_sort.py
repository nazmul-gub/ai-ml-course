def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i-1

        while(j >= 0 and key < a[j]):
            a[j+1] = a[j]
            j = j-1

        a[j+1] = key


arr = [100, 2, 55, 78, 4]
insertion_sort(arr)
print(arr)