class Sorting:
    def bubbleSort(self, array):
        for i in range(len(array)-1,0,-1):
            for j in range(i):
                if array[j] > array[j+1]:
                    array[j],array[j+1] = array[j+1],array[j]
        return array

sorting = Sorting()
print(sorting.bubbleSort([2,1,4,7,3,9,2,1]))


def selectionSort(self, array):
                for i in range(len(array)-1):
                    min_index = i
                    for j in range(i+1,len(array)):
                        if array[min_index] > array[j]:
                            min_index = j
                    if i != min_index:
                        array[i], array[min_index] = array[min_index], array[i]
                return array

print(sorting.selectionSort([2,1,4,7,3,9,2,1]))

#%%
def insertionSort(self, array):
        pass


