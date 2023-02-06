def linear_search(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return True,i

print(linear_search([1,2,6,7,8,55,54,66,-1], -1))