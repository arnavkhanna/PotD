
    
def a(x):
    if x == 0 or x == 1:
        return 1
    else:
        return a(x-1) + a(x-2)

times1 = int(input("How many numbers do you want to add? "))
print(a(times1))
