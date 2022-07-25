# Python Program to Extract Extension From the File Name
# In this example, you will learn to extract extension from the file name.

# using the splitext() method from os module
import os
sharad = os.path.splitext('img1.jpeg')
print(sharad)
print(sharad[1])

# using pathlib module: 

import pathlib
print(pathlib.Path('img1.jpeg').suffix)