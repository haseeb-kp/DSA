'''
find_in_mountain_array - leetcode hard problem
same as other problems. Find the peak element and then do binary search on both side to find the element
'''
def find_in_mountain_array(array,target):
    start = 0
    end = len(array) - 1
    peak = find_peak(array)
    print("peak",peak)
    index = binary_search(array, target, start, peak)
    if index != -1:
        return index
    else:
        index = binary_search(array, target, peak, end)
        if index != -1:
            return index
        return -1
    return -1

def find_peak(array):
    start = 0
    end = len(array)-1
    while start < end:
        mid = start + (end-start) // 2
        if array[mid]>array[mid+1]:
            end = mid
        else:
            start = mid+1
    return start

def binary_search(array,target,start,end):
    ascending = True if array[start] < array[end] else False
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        if ascending:
            if array[mid] > target:
                end = mid -1
            else:
                start = mid+1
        else:
            if array[mid] > target:
                start = mid+1     
            else:
                end = mid -1
    return -1

array = [1,5,2]
print(find_in_mountain_array(array, 2))