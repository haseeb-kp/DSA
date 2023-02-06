def insertionSort(array):
    for i in range(len(array)-1):
        for j in range(i+1,0,-1):   
            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
            else:
                break   #since previous elements are already in sorted 
    return array
array = [-1,0,-2,1.5,68,78,98,2,3,4,5,6,1,2]
print(insertionSort(array))




'''def insertionSort(array):
    for i in range(len(array)-1):
        j = i+1
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array
array = [4,5,3,2,1]
print(insertionSort(array))'''