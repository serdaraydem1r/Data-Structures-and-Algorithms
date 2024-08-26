myList = [1,2,3,4,5]
otherList = [6,7,8,9,10]
myList.extend(otherList) # ekleme yapar.
print(myList)

result = [0]*8
print(result)
result[3] = 6
print(result)

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 6, 0, 0, 0, 0]
"""

import sys # sistemle iletişime geçmeyi sağlar
n = 15
myDynamicArray = []
for i in range(n):
    myLenght = len(myDynamicArray)
    myByte = sys.getsizeof(myDynamicArray)
    print(f"Lenght: {myLenght} Byte: {myByte}")
    myDynamicArray.append(n)
"""
Lenght: 0 Byte: 56
Lenght: 1 Byte: 88
Lenght: 2 Byte: 88
Lenght: 3 Byte: 88
Lenght: 4 Byte: 88
Lenght: 5 Byte: 120
Lenght: 6 Byte: 120
Lenght: 7 Byte: 120
Lenght: 8 Byte: 120
Lenght: 9 Byte: 184
Lenght: 10 Byte: 184
Lenght: 11 Byte: 184
Lenght: 12 Byte: 184
Lenght: 13 Byte: 184
Lenght: 14 Byte: 184
"""