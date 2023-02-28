while True:
    stack = []
    w = input()
    if w==".":
        break
    check = 0
    for i in w:
        if i == ".":
            break
        elif i == "(":
            stack.append(i)
        elif  i == "[" :
            stack.append(i)
        elif i == ")":
            if len(stack)==0:
                print("no")
                check = 1
                break
            else:
                b = stack.pop()
                if b != "(":
                    print("no")
                    check = 1
                    break
        elif i == "]":
            if len(stack)==0:
                print("no")
                check = 1
                break
            else:
                b = stack.pop()
                if b != "[":
                    print("no")
                    check = 1
                    break

    if len(stack)==0 and len(stack)==0 and check == 0:
        print("yes")
    elif check == 1:
        continue
    else:
        print("no")