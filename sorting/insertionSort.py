arr = [5, 2, 3, 9, 1, 0, 10]

top = len(arr)
key = 0
place = 0

for i in range(1, top):
    key = arr[i]
    place = i - 1
    if arr[place] > key:
        while place >= 0 and arr[place] > key:
            temp = arr[place + 1]
            arr[place + 1] = arr[place]
            arr[place] = temp
            place = place - 1
        arr[place + 1] = key
    print(arr)

print(arr)
