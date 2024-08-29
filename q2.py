from math import ceil
from math import floor

n = int(input("n: "))
customer_input = []

for i in range(n):
    customer_input.append(0)
    customer_input[i] = []
    for j in range(n):
        customer_input[i].append(0)
        customer_input[i][j] = 0

whileLoopCounter = 1

for i in range(1, n * n + 1):
    if ceil(i/n) % 4 == 1:
        a = floor(whileLoopCounter) - 1
        customer_input[a][floor(whileLoopCounter) + (i%n) -2] = i
    elif ceil(i/n) % 4 == 2:
        b = n - (floor(whileLoopCounter) - 1) - 1
        customer_input[n - (floor(whileLoopCounter) + (i%n) -1)][b] = i
    elif ceil(i/n) % 4 == 3:
        a = n - (floor(whileLoopCounter) - 1) - 1
        customer_input[a][-(n - floor(whileLoopCounter) - (i%n) + 1)] = i
    elif ceil(i/n) % 4 == 0:
        b = floor(whileLoopCounter) - 1
        customer_input[-(n - floor(whileLoopCounter) - (i%n) + 1)][b] = i

    whileLoopCounter += 1 / n

print(whileLoopCounter)

for i in range(n):
    print(customer_input[i])
