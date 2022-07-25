# Python Program to Generate Password by Sharad Khare
# To write a Python program to create a password, declare a string of numbers + uppercase + lowercase + special characters. Take a random sample of the string of a length given by the user:
import random
sharadlen = int(input("Please enter the length of the password to be generated: "))
sharad = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?"
password = "".join(random.sample(sharad, sharadlen))
print(password)