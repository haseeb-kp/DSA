def peak_index_in_mountain_array(array):
    start = 0
    end = len(array) - 1
    while start < end:
        mid = start + (end - start) // 2
        if array[mid] > array[mid+1]:
            '''
            you are in the decreasing part of array.
            This is a possible ans. but check in the left part also.
            This is why end != mid -1

            '''
            end = mid
        else:
            '''you are in ascending part of array'''
            start = mid + 1
            '''because we know that mid+1 element > mid element'''
    
    ''' 
    in the end start== end and pointing to the largest element
    start and end always tries to find max element in two above checks
    thus we can return start or end
    '''
    return start 
            