def insertionSort(arr):
    for i in range(1, len(arr)):
         key = arr[i]
         j = i - 1
         while key < arr[j] and j > -1 :
             arr[j + 1] = arr[j]
             arr[j] = key
             j -= 1
    return arr

print(insertionSort([4, 5, 6, 7, 1, 2]))

