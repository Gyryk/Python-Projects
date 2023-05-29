queue = [None for index in range(0, 10)]
frontPointer = 0
rearPointer = -1
queueFull = 10
queueLength = 0
item = None

def enqueue(myItem):
    global queueLength, rearPointer
    if queueLength < queueFull:
        if rearPointer < len(queue) - 1:
            rearPointer = rearPointer + 1
        else:
            rearPointer = 0
        queueLength = queueLength + 1
        queue[rearPointer] = myItem
    else:
        print("queue full")


def dequeue():
    global queueLength, frontPointer, item
    if queueLength == 0:
        print("empty queue")
    else:
        item = queue[frontPointer]
        if frontPointer == len(queue) - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
    queueLength = queueLength - 1
