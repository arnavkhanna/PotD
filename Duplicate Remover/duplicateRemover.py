
input1 = input("Enter a string: ")
list1 = []
list2 = [" "]
boolean = True
for i in input1:
    list1.append(i)
for i in list1:
    for a in list2:
        if i.lower() == a.lower():
            boolean = False
    if boolean == True:
        list2.append(i)
    boolean = True
finalStr = ""
for i in list2:
    finalStr += i

print(finalStr)
