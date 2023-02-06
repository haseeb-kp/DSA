'''search in rotated sorted array
can optimize this using recursion
'''
def find_pivot(array):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = start + (end-start) // 2
        if mid < end and array[mid] > array[mid+1]: # mid < end -->to prevent index out of bond
            return mid
        if mid > start and array[mid] < array[mid-1]:
            return mid - 1
        if array[mid] <= array[start]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def search(array,number):
    pivot = find_pivot(array)
    print("pivot= ",pivot)
    #if pivot is -1 , then array is not rotated
    if pivot == -1:
        #normal binary search
        return binary_search(array, 0, len(array)-1, number)
    if array[pivot] == number:
        return pivot
    if number >= array[0]:
        return binary_search(array, 0, pivot-1, number)
    return binary_search(array, pivot+1, len(array)-1, number)
        


def binary_search(array,start,end,number):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == number :
            return mid
        if array[mid] < number :
            start = mid+1
        else :
            end = mid-1

    return -1        

array =[5,1,3]
print(search(array, 5))