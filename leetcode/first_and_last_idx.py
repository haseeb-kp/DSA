'''
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
'''
def searchRange( nums, target):
    ans = [-1,-1]
    start = search(nums,target,True)
    end = search(nums,target,False)
    ans[0]=start
    ans[1]=end
    return ans
def search(nums,target,find_start_idx):
    ans = -1
    start = 0
    end = len(nums)-1
    while start<=end:
        mid = (int)(start+(end-start)/2)
        if target<nums[mid]:
            end = mid-1
        elif target>nums[mid]:
            start = mid+1
        else:
            ans = mid
            if find_start_idx:
                end = mid-1
            else:
                start = mid+1
    return ans

print(searchRange( [1,2,3,4,5,5,8,], 5))