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

for i in [1, n + 1]:
    if ceil(i/5) % 4 == 1:
        a = floor(whileLoopCounter) - 1
        # for b in range(floor(whileLoopCounter) - 1, n + 1 - floor(whileLoopCounter)):
        customer_input[a][floor(whileLoopCounter) + i - 2] = i
    elif ceil(i/5) % 4 == 2:
        b = n - (floor(whileLoopCounter) - 1) - 1
        # for a in range(floor(whileLoopCounter), n + 1 - floor(whileLoopCounter)):
        customer_input[a][b] = i
    elif ceil(i/5) % 4 == 3:
        a = n - (floor(whileLoopCounter) - 1) - 1
        # for b in reversed(range(floor(whileLoopCounter) - 1, n - floor(whileLoopCounter))):
        customer_input[a][b] = i
    elif ceil(i/5) % 4 == 4:
        b = floor(whileLoopCounter) - 1
        # for a in reversed(range(floor(whileLoopCounter), n + 1 - floor(whileLoopCounter))):
        customer_input[a][b] = i

    whileLoopCounter += 0.25

# print(n - (floor(whileLoopCounter) - 1))

for i in range(n):
    print(customer_input[i])
