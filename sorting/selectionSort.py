def selectionSort(array):
    for i in range(len(array)):
        #find max element in remianing array and swap it with correct index
        last = len(array)-i-1
        maxIndex = getMaxIndex(array,0,last)

        #swap
        array[maxIndex],array[last] = array[last],array[maxIndex]
    return array

def getMaxIndex(array,start,end):
    max = start
    for i in range(start,end+1):
        if array[max]<array[i]:
            max = i
    return max

array = [5,1,78,4,32,0,6,82]
print(selectionSort(array))