from utils import remove_duplicates

items = [
    [1, 2, 3, 4],
    [1, 2, 4, 5],
    [1, 3, 4, 5],
    [2, 3, 5],
    [1, 2, 3]
]

for i in range(len(items)):
    items[i].sort()

# the language of the question is very confusing and doesn't tell enough things to make the program, like 1st customer
# has viewed all the products which 5th customer has viewed then shouldn't 5th be recommended product 4.
# and the question also doesn't specify if all the products should match in order to apply that recommendation rule or
# at least one product should match. so I have to make a lot of assumptions and the output wouldn't be same

# Overall Most Viewed Products
simplifiedItems = []
for i in range(len(items)):
    for j in range(len(items[i])):
        simplifiedItems.append(items[i][j])
simplifiedItems.sort()
sortedSimplifiedItems = sorted(simplifiedItems, key = simplifiedItems.count, reverse = True)
sortedUniqueSimplifiedItems = []
remove_duplicates(sortedSimplifiedItems, sortedUniqueSimplifiedItems)
print(sortedUniqueSimplifiedItems)

# creating 2d output array
recommendation = []
for i in range(len(items)):
    recommendation.append(0)
    recommendation[i] = []

# making recommendation
# for i in range(len(items)):
#     tempItems = items.pop(i)
#     for j in range(len(items) - 1):
#         if
