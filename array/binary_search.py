def binary_search(array,start,end,number):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == number :
            return True,mid
        if array[mid] < number :
            start = mid+1
        else :
            end = mid-1

    return -1
array = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(binary_search(array=array,start=0,end=len(array),number=7))