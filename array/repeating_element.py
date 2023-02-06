#first repeating and non repeating elements in an array

array = [1,2,3,1,4,2]
for i in range(len(array)):
    for j in range (i+1,len(array)):
        if array[i]==array[j]:
            print("first repeating = ",array[i])
            break
    break

for i in range(len(array)):
    non_repeating = True
    for j in range(len(array)):
        if i != j and array[i]==array[j]:
            non_repeating = False
            break
    if non_repeating:
        print("first non repeating = ",array[i])
        break