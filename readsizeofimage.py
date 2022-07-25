# Python Program to Find the Size (Resolution) of a Image
# You will learn to find resolution of a jpeg image in this example without using external libraries

# JPEG: Jay-Peg stands for Joint photographic Experts Group.
# 
def jpeg_res(filename):
    # this function prints the resolution of te jpeg image file.
    with open (filename, 'rb') as img_file:

        # height of the image(in 2 bytes) is at 164th position:
        img_file.seek(163) 

        # read the 2 bytes
        a = img_file.read(2)

        # calculate height
        height = (a[0] << 8) + a[1]

        # next 2 bytes is width
        a = img_file.read(2)

        # calculate width
        width = (a[0] << 8) + a[1]

    print("The resolution of the image is ", width, "x", height)

jpeg_res("img1.jpeg") 
