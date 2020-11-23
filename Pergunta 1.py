array = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
countOnes = 0

for i in array:
    if i == 1:
        countOnes += 1

for y in range(0, countOnes):
    array.remove(1)

for x in range(0, countOnes):
    array.insert(0, 1)

print(array)
