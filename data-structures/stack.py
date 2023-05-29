stack = [None for index in range(0, 10)]
basePointer = 0
topPointer = -1
stackFull = 10
item = None

def pop():
    global topPointer, basePointer, item
    if topPointer == basePointer - 1:
        print("empty stack")
    else:
        item = stack(topPointer)
        topPointer = topPointer - 1


def push(myItem):
    global topPointer
    if topPointer < stackFull - 1:
        topPointer = topPointer + 1
        stack[TopPointer] = myItem
    else:
        print("full stack")

