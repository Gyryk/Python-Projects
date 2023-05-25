for i in range(1, 100):
    divis = i % 5
    if i % 3 == 0:
        if divis == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif divis == 0:
        print("Buzz")
    else:
        print(i)
