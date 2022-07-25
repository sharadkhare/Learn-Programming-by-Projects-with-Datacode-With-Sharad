# Python Program to Check if a Number is Positive, Negative or 0 
# In this example, you will learn to check whether a number entered by the user is positive, negative or zero. This problem is solved using if...elif...else and nested if...else statement.

# through if...elif...else
sharad = float(input("Enter a Number: "))
if sharad > 0:
    print("Positive number")
elif sharad==0:
    print("Zero")
else:
    print("Negative Number")

# using the Nested if:
sharad = float(input("Enter a Number: "))
if sharad >=0:
    if sharad == 0:
        print("Zero")
    else:
        print("Positive Number")
else:
    print("Negative Number")


