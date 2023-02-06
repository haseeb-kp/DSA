def is_palindrome(string):
    return string == string[::-1]

string = "racecar"
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")


str = "haseeb"
print(len(str))



test_string = "MohammedHaseeb"
new_string = test_string[:2] + test_string[3:]
print ("new string : " + new_string)


name = "haseeb"
name2 = "kp"
print(name+" "+name2)