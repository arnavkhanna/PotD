inputString = "(("
list1 = []
if len(inputString) % 2 == 0:
    if len(inputString)>0:
        if inputString[0] == "{" or inputString[0] == "[" or inputString[0] == "(":
            x = True
            for i in inputString:
                if i == "(" or i == "[" or i == "{":
                    list1.append(i)
                elif i == ")" or i == "]" or i == "}":
                    open1 = list1.pop()
                    if open1 == "(":
                        if i != ")":
                            x = False
                            break
                    elif open1 == "[":
                        if i != "]":
                            x = False
                            break
                    elif open1 == "{":
                        if i != "}":
                            x = False
                            break
                else:
                    x = False
                    break
            if len(list1) > 0:
                x = False
            if x:
                print("Valid")
            else:
                print("Invalid")
                    
        else:
            print("Invalid")
    else:
        print("Valid")
else:
    print("Invalid")
