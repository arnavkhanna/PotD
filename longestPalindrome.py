a = "abcddcaa"
b = "".join(reversed(a))
list1 = []
list2 = []
for i in b:
    list2.append(i)
for i in a:
    list1.append(i)
count = 0
for x in range(len(list1)):
    y = x+1
    if list1[y]
