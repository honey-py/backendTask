inputListInitial = [1, 2, 3, 7, 4, 5, 7, 8, 10, 13, 14, 15, 16, 17, 23, 12, 6, 9, 342, 435, 54]
target = int(input("target number: "))
output = []
rmIndex = []

# Removing duplicates from inputList, will not consider adding same numbers to get target as of now, this is just to
# ensure that no errors are generated. will add support for duplicates later if I have time.

inputList = []
for i in range(len(inputListInitial)):
    if inputListInitial[i] not in inputList:
        inputList.append(inputListInitial[i])
inputList.sort()
# there were some bugs when list wasn't sorted

for i in range(len(inputList)):
    for j in range(len(inputList)):
        if inputList[i] + inputList[j] == target:
            output.append((inputList[i], inputList[j]))

# Removing Duplicates from output
for i in range(len(output)):
    for j in range(len(output)):
        if output[i][0] == output[j][1] and output[i][1] == output[j][0]:
            rmIndex.append(j)
if len(rmIndex) % 2 == 0 and len(output) > 0:
    for i in range(int(len(rmIndex) / 2)):  # had to use int to avoid float interpretation as int error
        rmIndex.pop(-1)
elif len(rmIndex) % 2 != 0 and len(output) > 0:
    for i in range(int((len(rmIndex) + 1) / 2)):
        rmIndex.pop(-1)
# when len(rmIndex) is odd, it can mean only one thing, that the output value with the middle index is (a,a) and that
# shouldn't be removed because there isn't any duplicate of that, it's just that the program is recognizing it as a
# duplicate. divided by 2 to remove duplicate entries in rmIndex
rmIndex.sort(reverse=True)
# sorting because if I remove index 8 before 9, value at index 9 will be changed
for i in range(len(rmIndex)):
    output.pop(rmIndex[i])

print(output)
