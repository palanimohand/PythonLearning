def fizbuzz(number):
    for i in range(1,(number+1)):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizbuzz(5)