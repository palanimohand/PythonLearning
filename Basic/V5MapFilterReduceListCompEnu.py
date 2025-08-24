x = lambda a,b,c,*args,**kwargs : print(a,b,c,args,kwargs)
print(type(x))
# positional arguments
x(1,2,3,5,6,7,8,9,10,abc=1,deff=2)
x(2,2,2)

a = x(3,3,3)

print(a)

x = "string"

abc = ['a','C','Z','b','c','c']
abc = ('a','C','Z','b','c', 'b')
abc = {'a','C','Z','b','c','c'}
abc = {'a':9,'b':8,'c':10}

def makeUpper(a):
    return a.upper()

makking_upper = lambda x:x.lower()

print(sorted(abc, key=lambda x:x.upper()))
print(sorted(abc, key=makking_upper))
print(sorted(abc, key=makeUpper, reverse=True))

print(x)
print(type(x))

def sq(x):
    return x**2

def cu(x):
    return x**3

def applyfun(x,y):
    return y(x)

lsu = lambda x : x+x
lmu = lambda x : x*x

print(applyfun(2, sq))
print(applyfun(2, cu))
print(applyfun(3, lsu))
print(applyfun(3, lmu))

#lamba with if else condition
y = lambda z : "even" if z%2==0 else "odd"
print(y(2))




# Lambda
from functools import reduce
m = lambda x: x**3
n = lambda x,y: x+y
set1 = {1, 2, 3, 4, 5}
# allowed
# set2 = [6, 7, 8, 9]
# set2 = (6, 7, 8, 9, 10)
# set2 = {6, 7, 8, 9, 10}
set2 = {6: 'a', 7: 'b', 8: 'c', 9: 'd', 10: 'e'}
# not allowed
# set2 = {'a': 6, 'b': 7, 'c': 8, 'd': 9, 'e': 10}
print(list(map(m, set1)))
print(list(map(n, set1, set2)))
# Question - How does this casting of dictionary happen ? - Keys are taken by default

conditional = lambda x : x%2 == 0
print(list(filter(conditional, set1)))

add = lambda a,b : a + b
print(reduce(add, set1))
# what other expressions can be used in a reduce apart from a + b and max function
# reduce max function
maxi = lambda a,b : a if a>b else b
print(reduce(maxi, set1))
# other than max and sum functions can we try strings, for lambda string iam trying for the first time
str = lambda a,b : a + b
stringlist = ["Palani", " ", "i"]
print(reduce(str, stringlist))
# strsplit = lambda a,b : a.split(b) #throws an error arg 2 must support iteration here split returns a list
# print(reduce(stringlist, strsplit))
# stringlist = ["Palani", 1, 2]
# strsplit = lambda a,b : a.zfill(b) #throws an error arg 2 must support iteration here split returns a list
# print(reduce(stringlist, strsplit))
# "ae".zfill(1)


convert_to_farenheit = lambda c : (c[0],(c[1]*(9/5)) + 32)  #without braket it doesnt consider as an expression and comes as c undefined

# print(convert_to_farenheit(36))
city_temperatures = {
    'chennai' : 36,
    'mumbai' : 34,
    'ooty' : 22,
    'kanyakumari' : 28
}
# print(list(map(convert_to_farenheit,city_temperatures.values())))
print(list(map(convert_to_farenheit,city_temperatures.items())))
print(dict(map(convert_to_farenheit,city_temperatures.items())))
print([(city_temp[0],(city_temp[1]*(9/5)+32)) for city_temp in city_temperatures.items()])
print(list(enumerate(city_temperatures.items(), start=3)))


for city_temp in city_temperatures.items():
    output = (city_temp[0] , ((city_temp[1]*9/5)+32))
    print(output)

for num,city_temp in enumerate(city_temperatures.items()):
    output = (city_temp[0] , ((city_temp[1]*9/5)+32))
    print(num,output)

# string to character
text = "Automation and AI"
listofChar = []
# no toChar method required unlike java as automatically it converts to single character
for i in text:
    listofChar.append(i)
print(listofChar)
# equivalent of tochar one more approach as a map
print(list(map(lambda a:a,text)))
# a string can be place where ever an iterable can be placed

# list comprehension
lcl = [1,2,3,4]
# as list comprehension
print([a**2 for a in lcl])
# same logic as a map
print(list(map(lambda a : a**2, lcl)))
print(list(map(lambda a : a**2 if a%2==0 else a-1, lcl)))

# if condition based list comprehension
print([a**2 for a in range(1,10)])
print([a for a in range(1,10) if a%2==0])
# print([a for a in range(1,10) if a%2==0 else a-1]) invalid syntax error message
print([a**2 for a in range(1,10) if a%2==0])
# nested list comprehension
print([b**2 for b in [a**2 for a in range(1,10)]])


