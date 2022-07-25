# Python Program to Get Line Count of a File
# In this example, you will learn to get line count of a file.

def file_len(fname):
    with open(fname) as f:
        for i, j in enumerate(f):
            pass
    return i + 1
print(file_len('count.txt'))

# using the list comprehension:
sharad = sum(1 for i in open('count.txt'))
print(sharad)