def ceil(array,number):
    start = 0
    end = len(array)-1
    while start<=end:
        mid = start+(end-start)//2
        if array[mid] == number:
            return array[mid]
        elif number > array[mid] :
            start = mid+1
        else:
            end = mid-1
    return array[start]

print(ceil([1,5,10,15,20,25], 22))