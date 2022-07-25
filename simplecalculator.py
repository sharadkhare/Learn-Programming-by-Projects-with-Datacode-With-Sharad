# Python Program to Make a Simple Calculator
# In this example you will learn to create a simple calculator that can add, subtract, multiply or divide depending upon the input from the user.
# This function adds two numbers:
def add(x,y):
    return x+y
# this function subtracts two number:
def subtract(x,y):
    return x-y
#This function multiplies 2 numbers:
def multiply(x,y):
    return x*y
# this function divides 2 numbers:
def divide(x,y):
    return x/y

print("Select Operations.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from users
    choice = input("Enter choice(1/2/3/4): ")

    # check if the choice is one of the four options or not:
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice =='1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice=='2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice=='3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice=='4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if the user want another calculation or not
        # then we will break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
    