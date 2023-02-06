def bubbleSort(array):
    #run the steps n-1 times
    for i in range(len(array)):
        swapped = True
        #for each iteration largest element comes at end
        for j in range(1,len(array)-i):
            #swap if element is smaller than previous
            if array[j] < array[j-1]:
                #swap
                # print("Entered")
                array[j],array[j-1] = array[j-1],array[j]
                swapped = False
    #if swapped is True then the array is already sorted thus return
    if swapped:
        return array
    return array


# array=[1,2,3,4,5]
array = [-1,0,-2,1.5,68,78,98,2,3,4,5,6,1,2]
print(bubbleSort(array))
