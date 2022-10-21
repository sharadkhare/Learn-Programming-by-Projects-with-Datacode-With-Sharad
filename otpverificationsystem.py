""" Steps to Create an OTP Verification System using Python """
# 1. first, we will create a 6 digit random number.
# 2. than we will store this number to a variable
# 3. then we need to write a program to send the email
# 4. when sending the email, we need to use the OTP as a message.
# 5. finally we need to request 2 user input, first for the user's email and then for the OTP that the user has recived.
import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP+= digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg = otp
""" this link is for singing the google app password. please foloow the instruction : https://support.google.com/accounts/answer/185833?hl=en """

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail Account", "Your App Password")
emailid = input("PLease Enter your Email: ")
s.sendmail('&&&&&&&&&&&', emailid, msg)
a = input("PLease Enter you OTP >>: ")
if a == OTP:
    print("Yes, Your OTP is Verified")
else:
    print("Please check your OTP Again")