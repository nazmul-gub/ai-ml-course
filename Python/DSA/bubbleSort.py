def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

arr = [100, 2, 55, 78, 4]
bubbleSort(arr)
print(arr)