
def find_duplicate(string):
    table = {}
    for i in string:
        if i in table:
            return True
        else:
            table[i]=True
    return -1
    
string = "hello"
print(find_duplicate(string))