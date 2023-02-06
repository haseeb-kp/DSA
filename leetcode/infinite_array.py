'''
find position of element in sorted infinite array
can not use len(array)
'''

def ans(array,target):
    start = 0
    end = 1
    while target>array[end]:
        new_start = end + 1
        #end = end+size of box * 2
        end = end + (end - start + 1) * 2
        start = new_start
    return binary_search(array,target,start,end)

def binary_search(array,target,start,end):
    while start <= end:
        mid = (int)(start + (end-start) / 2)
        if target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid +1
        else:
            return mid
    return -1

print(ans([3,5,7,9,10,90,100,130,140,160,170],10))