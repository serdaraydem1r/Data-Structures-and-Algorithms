def solution(ops):
    myStack = []
    for i in ops:
        if i == "C":
            myStack.pop()
        elif i == "+":
            myStack.append(myStack[-1]+myStack[-2])
        elif i == "D":
            myStack.append(myStack[-1]*2)
        else:
            myStack.append(int(i))
    return sum(myStack)
ops = ["5","2","C","D","+"]
print(solution(ops))

