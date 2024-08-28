temperatures = [73,74,75,71,69,72,76,73]
def DailyTemp():
    result = [0] * len(temperatures)
    stack = [] # temp&index
    for index, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stackTemp, stackIndex =stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append([temp, index])
    return result
print(DailyTemp())

