list1 = [2,9,7,12,3]
target = 9
a = 0
b = 0
while a < len(list1):
    while b < len(list1):
        if list1[a] + list1[b] == target:
            if a != b:
                list3 = [a,b]
                break
        b = b + 1
    a = a+1
print(str(list3))
