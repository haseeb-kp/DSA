# def twoSum(array, target):
#     for i in range(len(array) - 1):
#         for j in range(i + 1, len(array)):
#             if array[i] + array[j] == target:
#                 print((array[i],array[j]))
# array = [3, 5, 2, -4, 8, 11]
# target = 7

# twoSum(array, target)

def two_sum(array,target_num):
    nums={}
    for num in array:
        match = target_num-num
        if match in nums:
            return [match,num]
        else:
            nums[num]=True
    return -1

array = [3,3]
print(two_sum((array),6))
print(two_sum((array),64))