arrayNums = [3, 5, 2, 4, 0, 1, 6, 8, 7]

top = 9
swap = False

while swap or top != 0:
    for i in range(0, top - 1):
        swap = False
        if arrayNums[i] > arrayNums[i+1]:
            temp = arrayNums[i]
            arrayNums[i] = arrayNums[i+1]
            arrayNums[i+1] = temp
            swap = True
    top -= 1
print(arrayNums)
