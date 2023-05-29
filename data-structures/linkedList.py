ll = [27, 19, 36, 42, 16, None, None, None, None, None, None, None]
llPointers = [-1, 0, 1, 2, 3, 6, 7, 8, 9, 10, 11, -1]
startPointer = 4
nullPointer = -1
heapStartPointer = 5

def find(itemSearch):
    found = False
    itemPointer = startPointer
    while itemPointer != nullPointer and not found:
        if ll[itemPointer] == itemSearch:
            found = True
        else:
            itemPointer = llPointers[itemPointer]
    return itemPointer


def insert(itemAdd):
    global startPointer, heapStartPointer
    if heapStartPointer == nullPointer:
        print("linked list full")
    else:
        ll[heapStartPointer] = itemAdd
        llPointers[heapStartPointer] = startPointer
        startPointer = heapStartPointer
        heapStartPointer = llPointers[heapStartPointer]


def delete(itemDelete):
    global startPointer, heapStartPointer
    if startPointer == nullPointer:
        print("linked list empty")
    else:
        index = startPointer
        while ll[index] != itemDelete and index != nullPointer:
            oldindex = index
            index = llPointers[index]
        if index == nullPointer:
            print("Item ", itemDelete, " not found")
        else:
            ll[index] = None
            tempPointer = llPointers[index]
            llPointers[index] = heapStartPointer
            heapStartPointer = index
            llPointer[oldindex] = tempPointer


item = int(input("item: "))
result = find(item)
if result == -1:
    print("not found")
else:
    print("found at", result)
