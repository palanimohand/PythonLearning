marks = [78, 85, 62, 90, 55, 88]
m = marks.copy()
print(max(marks))
print(min(marks))
print(sum(marks)/len(marks))
for mark in marks:
    if mark > 75:
        print(mark)
marks.append(95)
print(marks)
marks.remove(55)
print(marks)
marks.sort()
sortedListed = sorted(marks)    
print(marks)
sorted(m)
print(m)
print(sortedListed)

def sumtotal(a,b):
    return a + b

sumtotal(11,b=5)

def calculate_salary(basic, hra, da, bonus=0):
    return basic+hra+da+bonus

print(calculate_salary(15000,5000,2000))
print(calculate_salary(15000,5000,2000,5))

def calc(*args):
    return print(args)

print(calc(4,5,6))
lister = [5,6,7]
print(calc(lister))