# Python Program to Add Two Matrices
# In this program, you'll learn to add two matrices using Nested loop and Next list comprehension, and display it.

# matrix addition through nested loop
x = [[12,7,3],[4,5,6],[7,8,9]]
y = [[5,8,1],[6,7,3],[4,5,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]

# iterate through rows:
for i in range(len(x)):
    # iterate through columns
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
for r in result:
    print(r)

# Matrix addition now by using the nested list comprehension:
x = [[12,7,3],[4,5,6],[7,8,9]]
y = [[5,8,1],[6,7,3],[4,5,9]]

result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
for r in result:
    print(r)