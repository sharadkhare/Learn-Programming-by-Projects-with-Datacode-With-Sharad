# Python Program to Find Hash of File
# In this article, you'll learn to find the hash of a file and display it.

# there are many hashing functions like MD5,SHA-1.

# first we will import the hashlib module
import chunk
import hashlib

def hash_file(filename):
    # this function returns the SHA-1 hash:

    # now we will make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:

        # here now we will loop the file till the end of the file.
        chunk = 0
        while chunk != b'':
            # then read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
    # here now we will return the hex representation of the digest
    return h.hexdigest()

message = hash_file("img1.jpeg")
print(message)
