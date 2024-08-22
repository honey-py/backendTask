# I could use functions like split() etc but I decided to do almost everything manually

s1 = input("str1: ")
s2 = input("str2: ")
array1 = []
array2 = []
common = 0


def is_duplicate(array):
    array_copy = []
    duplicate = False
    for item in range(len(array)):
        if array[item] not in array_copy:
            array_copy.append(array[item])
        else:
            duplicate = True
    return duplicate


for i in range(len(s1)):
    array1.append(s1[i])
for i in range(len(s2)):
    array2.append(s2[i])

for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] == array2[j]:
            common += 1

if not is_duplicate(array1) and not is_duplicate(array2):

    if common > 0 and common != min(len(array1), len(array2)):
        print("strings are not complementary")
    elif common == 0:
        print("strings are complementary")
    elif common > 0 and common == min(len(array1), len(array2)):
        print("strings are not complementary and are balanced")

elif is_duplicate(array1) or is_duplicate(array2):

    if common > 0:
        print("strings are not complementary")
    elif common == 0:
        print("strings are complementary")
