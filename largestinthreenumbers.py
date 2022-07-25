# Python Program to Find the Largest Among Three Numbers
# In this program, you'll learn to find the largest among three numbers using if else and display it.
sharad1 = 10
sharad2 = 14
sharad3 = 12

# uncomment the following lines to take three input from user.
#sharad1 = float(input("Enter the first Number: "))
#sharad2 = float(input("Enter the second Number: "))
#sharad3 = float(input("Enter the third Number: "))

if (sharad1 >= sharad2) and (sharad1 >= sharad3):
    largest = sharad1
elif (sharad2>= sharad1) and (sharad2 >= sharad3):
    largest = sharad2
else:
    largest = sharad3

print("The largest Number is", largest)