def quick_sort(array,low,high):
    if low >= high:
        return
    start = low
    end = high
    mid = start + (end-start)//2
    pivot = array[mid]
    while start <= end:
        while array[start] < pivot:
            start+=1
        while array[end] > pivot:
            end-=1
        if start <= end:
            array[start],array[end] = array[end],array[start]
            start+=1
            end-=1
    quick_sort(array, low, end)
    quick_sort(array, start, high)

array = [5,4,3,2,1]
quick_sort(array, 0, len(array)-1)
print(array)