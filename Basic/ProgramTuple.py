# 1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and tuple which contains every number.

# input : 34,67,55,33,12,98
# output : [ '34', '67', '55', '33', '12' , '98' ]
#          ('34', '67', '55', '33', '12', '98')

# 2. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

# input : (1,2,3,4,5,6,7,8,9,10, 11)
# output : (1,2,3,4,5)
#         (6,7,8,9,10)

fulltup = input("Enter a sequence of comma-separated numbers: ")
fulltup = tuple(fulltup.split(','))
half = int(len(fulltup)/2)
print(half)
for i in range(len(fulltup)):
    # print(f'iteration {i}')
    if i < half:
        print(fulltup[i], end=',')
    elif i >= half:
        shift = True if i == half else False
        if shift:
            print()
        print(fulltup[i], end=',')


# 3. Write a program to generate and print another tuple whose values are even numbers in the given tuple
# input : (1,2,3,4,5,6,7,8,9,10)
# output : (2, 4, 6, 8, 10)

inputTup = (1,2,3,4,5,6,7,8,9,10)
evenTup = ()
for i in inputTup:
    if i % 2 == 0:
        evenTup += (i,)
print("Even numbers in the tuple:", evenTup)

inputList = [1,2,3,4,5,6,7,8,9,10]
evenList = []
for i in inputList:
    if i % 2 == 0:
        evenList += [i]
print("Even numbers in the List:", evenList)

inputset = {1,2,3,4,5,6,7,8,9,10}
evenSet = set()
for i in inputset:
    if i % 2 == 0:
        evenSet.add(i)
print("Even numbers in the Set:", evenSet)