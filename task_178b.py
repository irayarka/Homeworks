# getting input data
n = int(input('Enter the number of elements: '))
print('Enter elements: ')
sequence = [int(input()) for i in range(n)]

counter = 0
for element in sequence:
    if element % 3 == 0 and element % 5 != 0:
        counter += 1

# printing the result
print(counter)
