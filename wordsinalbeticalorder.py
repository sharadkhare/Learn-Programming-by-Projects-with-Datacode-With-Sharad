# Python Program to Sort Words in Alphabetic Order
# In this program, you'll learn to sort the words in alphabetic order using for loop and display it.

from pyparsing import Word


my_str = "hello my full name is sharad khare"

# to take the input from the user then uncomment it
# my_str = input("Enter the string: ")

# here we will breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# now here we will sort the list
words.sort()

# now we will display the sorted words
print("The sorted words are: ")
for i in words:
    print(i)
