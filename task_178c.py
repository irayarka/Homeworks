from math import sqrt

# getting input data
n = int(input())
sequence = [int(input()) for i in range(n)]

counter = 0
for element in sequence:
    root = sqrt(element)
    if root ** 2 == element and root % 2 == 0:
        counter += 1

# printing the result
print(counter)
