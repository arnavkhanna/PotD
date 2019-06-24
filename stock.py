list1 = [5,4,3,2,1]
greatestDiff = 0
list2 = []
if len(list1) > 0:
    for i in range(len(list1)):
        list2.append(list1[i])
        minimum = min(list2)
        diff = list1[i]-minimum
        if diff > greatestDiff:
            greatestDiff = diff
print(greatestDiff)
    
