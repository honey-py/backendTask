s1 = input("str1: ")
s2 = input("str2: ")
array1 = []
array2 = []
common = 0

for i in range(len(s1)):
    array1.append(s1[i])
for i in range(len(s2)):
    array2.append(s2[i])

for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] == array2[j]:
            common += 1

if common > 0:
    print("strings are not complementary")
elif common == 0:
    print("strings are complementary")
