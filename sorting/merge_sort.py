def merge_sort(array):
    if len(array)==1:
        return array
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]
    return merge_sorted_array(merge_sort(left_half),merge_sort(right_half))

def merge_sorted_array(left_half,right_half):
    sorted = [None] * (len(left_half)+len(right_half))
    i=j=k=0
    while i<len(left_half) and j<len(right_half):
        if left_half[i]<right_half[j]:
            sorted[k] = left_half[i]
            i +=1
        else:
            sorted[k]=right_half[j]
            j+=1
        k+=1
    while i<len(left_half):
        sorted[k] = left_half[i]
        i +=1
        k+=1
    while j<len(right_half):
        sorted[k] = right_half[j]
        j+=1
        k+=1
    return sorted

print(merge_sort([7, 6, 10, 5, 9, 2,1,15,7]))
