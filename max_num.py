import os
import random
import sys

f = open('max_num2.txt', 'w')

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

list4 = [9, 10, 11, 12]
list5 = []

list3 = list1 + list2 + list4
list5.append(list3)

print(list1)
print(list2)
print(list5)

print(max(list1))
print(max(list2))
print(max(list5))

f.write(str(list1))
f.write('\n')
f.write(str(list2))
f.write('\n')
f.write(str(list4))
f.write('\n')
f.write(str(list3))
f.write('\n')
f.write(str(max(list1)))
f.write('\n')
f.write(str(max(list2)))
f.write('\n')
f.write(ste(max(list5)))
f.write('\n')
f.close()
