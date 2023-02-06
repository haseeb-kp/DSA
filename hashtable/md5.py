import hashlib

key = hashlib.md5("hi i am haseeb".encode('utf-8')).hexdigest()
print(key)