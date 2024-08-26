"""
Bir dizi içerisinde en çok geçen elemanı döndürün.

"""

myList = [2,3,1,3,1,1,5,6,1,8,1,8,8,8,8,8,8,8,8]
def solution():
    numbers = {} # sözlük (hashmap)
    result = 0
    maxNumber = 0
    for i in myList:
        numbers[i] = 1 + numbers.get(i, 0)
        if numbers[i] > maxNumber:
            result = i
        maxNumber = max(maxNumber, numbers[i])
    return result
print(solution())



def boyerMoore():
    result = 0
    count = 0
    for num in myList:
        if count == 0:
            result = num
        if num == result:
            count += 1
        else :
            count -=1
    return result
print(boyerMoore())