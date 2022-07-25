# Python Program to Check the File Size
# In this example, you will learn to check the file size.

# using the OS module : the output size you will get will be in Byte.
import os
sharad = os.stat('count.txt')
print(sharad.st_size)

# Using the Pathlib Module.
from pathlib import Path
sharad = Path('count.txt')
print(sharad.stat().st_size)