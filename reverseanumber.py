# Python Program to Reverse a Number
# In this example, you will learn to reverse a number.

# Reversing a number using the while loop.
sharad = 1234
reverse_sharad = 0
while sharad != 0:
    digit = sharad % 10
    reverse_sharad = reverse_sharad * 10 + digit
    sharad //=10
print("Reversed Number is: " + str(reverse_sharad))

# now we will do by string slicing
sharad = 123456
print(str(sharad)[::-1])
