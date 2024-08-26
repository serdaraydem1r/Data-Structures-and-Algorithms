"""
Microsoft
Soru : Bir tane içinde int olan array verecek. Bir değer iki kere varsa
True döndür, yoksa False döndür.
input : nums = [1,2,3,1]
output: True
input : nums = [1,2,3,4]
output: False
"""


def duplicate (nums):
    """
    :Time : O(n)
    :Space : O(n)
    :param nums: nums
    :return: True, False
    """
    hashSet = set()
    for i in nums:
        if i in hashSet:
            return True
        hashSet.add(i)
    return False
nums = [1,2,3,1]
print(duplicate(nums))

def duplicate2 (nums):
    return len(nums) != len(set(nums))
nums = [1,2,3,4,2]
print(duplicate2(nums))