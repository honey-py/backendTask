# the language of the question is very confusing and doesn't tell enough things to make the program, like 1st customer
# has viewed all the products which 5th customer has viewed then shouldn't 5th be recommended product 4.
# and the question also doesn't specify if all the products should match in order to apply that recommendation rule or
# at least one product should match. and what should be the recommendation order if product view count is same for two
# products. so I have to make a lot of assumptions and THE OUTPUT WOULDN'T BE SAME. I still tried to make something

from utils import remove_duplicates

items = [
    [1, 2, 3, 4, 5],
    [1, 2, 4, 5],
    [1, 3, 4, 5],
    [2, 3, 5],
    [1, 2, 3]
]

for i in range(len(items)):
    items[i].sort()

# Overall Most Viewed Products

simplifiedItems = []
for i in range(len(items)):
    for j in range(len(items[i])):
        simplifiedItems.append(items[i][j])
simplifiedItems.sort()
sortedSimplifiedItems = sorted(simplifiedItems, key=simplifiedItems.count, reverse=True)
sortedUniqueSimplifiedItems = []
remove_duplicates(sortedSimplifiedItems, sortedUniqueSimplifiedItems)

# creating 2d output array

recommendation = []
for i in range(len(items)):
    recommendation.append(0)
    recommendation[i] = []

# making recommendation

for i in range(len(items)):
    for j in range(len(items)):
        match = True
        tempJ = items[j].copy()
        for k in range(len(items[i])):
            if items[i][k] not in items[j]:
                match = False
            else:
                tempJ.remove(items[i][k])
        if match and len(items[i]) < len(items[j]):
            # for l in range(len(items[j]) - len(items[i])):
            #     recommendation[i].append(items[j][len(items[i])+l])
            for l in range(len(tempJ)):
                recommendation[i].append(tempJ[l])

# adding remaining recommendations

for i in range(len(recommendation)):
    for j in range(3 - len(recommendation[i])):
        recommendation[i].append(sortedUniqueSimplifiedItems[j])

print(recommendation)
