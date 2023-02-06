def valueEqualToIndex(arr):
    sol =[]
    for i, num in enumerate (arr,1):
        if i == num:
            sol.append(i)
    return sol
print(valueEqualToIndex([1,2,10,5,6,42,7,8]))