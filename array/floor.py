def floor(array,number):
    start = 0
    end = len(array)-1
    while start<end:
        mid = start+(end-start)//2
        if number>array[mid]:
            start = mid+1
        elif number<array[mid]:
            end = mid-1
        else:
            return number
    return array[end]
print(floor([1,5,10,15,20,25], 14)) 