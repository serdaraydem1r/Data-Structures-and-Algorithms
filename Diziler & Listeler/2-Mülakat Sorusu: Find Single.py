"""
Amazon
nums adlı int array verilecek. Her eleman 2 kere var. 1 tanesi tek yazılmış.
onu bul. bazı array sadece 1 tane var.

Time : O(N)
Space: O(1) olmalı
"""
# bit maipulation
def solution ():
    myList = [1,1,2,2,3]
    result = 0
    for num in myList:
        result = num ^result # xor kapısı. iki değer aynı ise 0 farklı ise 1
    return result
print(solution())
