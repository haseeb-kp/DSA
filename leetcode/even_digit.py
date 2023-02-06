'''
1295. Find Numbers with Even Number of Digits
Given an array nums of integers, return how many of them contain an even number of digits.
'''
import math
def findNumbers(nums):
    count = 0
    for num in nums:
        if int(math.log10(num)%2) == 0:
            count+=1
    return count

print(findNumbers())



    # def even(num):
    #     count = 0
    #     while num>0:
    #         count+=1
    #         num = int(num/10)
    #     return count
# import math
# num = 123456456456
# print(int(math.log10(num)+1))