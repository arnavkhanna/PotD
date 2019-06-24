user = input("Enter a roman numeral: ")
list1 = []
for i in user:
    list1.append(i)
for x in range(len(list1)):
    if list1[x] == "I":
        list1[x] = 1
    elif list1[x] == "V":
        list1[x] = 5
    elif list1[x] == "X":
        list1[x] = 10
    elif list1[x] == "L":
        list1[x] = 50
    elif list1[x] == "C":
        list1[x] = 100
    elif list1[x] == "D":
        list1[x] = 500
    elif list1[x] == "M":
        list1[x] = 1000
used = False
list2 = []
for i in range(len(list1)):
    if used:
        used = False
        continue
    if i == (len(list1)-1):
        list2.append(list1[(len(list1)-1)])
    elif list1[i] < list1[i+1]:
        ab = list1[i+1]-list1[i]
        list2.append(ab)
        used = True
    else:
        list2.append(list1[i])
        used = False
print(sum(list2))
