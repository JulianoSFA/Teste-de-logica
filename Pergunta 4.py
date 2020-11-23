array = [9, 2, 3, 1, 4]
tempArray = list(array)
tempArray.sort()
n = tempArray[len(tempArray) - 1]

numberList = list(range(0, n+1))

for i in array:
    for x in numberList:
        if i == x:
            numberList.remove(x)

array.extend(numberList)
print(array)
