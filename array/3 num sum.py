def threeNumSum(array,target):
    for i in range (len(array)-2):
        for j in range (i+1,len(array)-1):
            for k in range (j+1,len(array)):
                if array[i]+array[j]+array[k]==target:
                    return [array[i],array[j],array[k]]
    return -1
array =[1,2,3,4,5,6]
print(threeNumSum(array, 9))