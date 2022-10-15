#Задание №1

for i in range(5):
    print(i+1,"0000000")


#Задание №2
numbers = range(1,101,1)
print(sum(numbers))


#Задание №3
num1 = 23
num2 = 45
num3 = 56
if num1 == num2 or num2 == num3 or num3 == num1:
    print("YES")
else:
     print("Error")


#Задание №4
numb1 = 23
numb2 = 46
numb3 = 23
if numb1 + numb2 == numb3 or numb2 + numb3 == numb1 or numb3 + numb1 == numb2:
    print("YES")


#Задание №5
numbe1 = 23
numbe2 = 36
numbe3 = -56
nul = 0
if numbe1 > 0:
    nul = nul + 1
if numbe2 > 0:
    nul = nul + 1
if numbe3 > 0:
    nul = nul +1
print("Количество полажительных чисел",nul)


#Задание №6
s = range(0,497,)
for items in s:
    if items % 2 == 0:
     print(items)


#Задание №7
number = range(0,15,1)
print(sum(number))

"""
#Задание №8
multi = range(1,9435,2)
s = 1
for all in multi:
    s *= all
    print(s)
 """


#Задание №9

from array import array
divided = array("i",list(range(54,9184,)))
for div5 in divided:
 if div5 % 5 == 0:
    print(div5)

#Задание №10
A = 65
B = 56
for I in range(56,65+1,):
 if A < B:
    print(I)
for S in range(65,56-1,-1):
  if B < A:
    print(S)



#Задание №11
import math
a = 6
print(math.factorial(a))

