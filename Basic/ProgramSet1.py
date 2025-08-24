# With two given lists [1, 3, 6, 78, 35, 55] and [12, 24, 35, 24, 88, 120, 155], write a program to make a list whose elements are intersection of the above given lists.

list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
set1 = set(list1).intersection(set(list2))
print("Intersection of the two lists:", set1)

# With a given list [12, 24, 35, 24, 88, 155, 88, 120, 155], write a program to print this list after removing all duplicate values with original order reserved.

list3 = [12, 24, 24, 24, 88, 155, 88, 120, 155]
uniqueList = []
for i in list3:
   if i not in uniqueList:
       uniqueList.append(i)
print("List after removing duplicates:", uniqueList)
list4 = list3.copy()
print(set(list4).union(list3))