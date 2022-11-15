#Задание №1
students = ["Bekzhan", "Meerim", "Aigerim", "Nursultan"] 
students1 = list(enumerate(students, start=5))
print(students1)


#Задание №2
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36]
summa = 0
for i in lst:
    summa += i
print(summa)


#Задание №3
lst1 = [1, 2, 3]
lst2 = [11, 22, 33] 
lst3 = []
for i in range(len(lst1)):
    lst3.append(lst1[i])
    lst3.append(lst2[i])

print(lst3)



#Задание №4
lst_1 = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36,
97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15,
52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

lst_2 = [84, 98, 51, 51, 50, 72, 19, 58, 81, 86, 38, 28, 8, 13, 76, 47, 90,
90, 2, 1, 4, 39, 94, 81, 24, 25, 36, 9, 82, 54, 6, 70, 81, 79, 68, 44, 84, 86,
96, 6, 49, 70, 84, 10, 38, 51, 88, 21, 62, 13] 

lst_3 = [97, 59, 93, 77, 78,
29, 34, 25, 53, 80, 56, 44, 41, 89, 48, 59, 58, 22, 64, 69, 17, 16, 0, 32,
89, 91, 70, 32, 34, 93, 45, 43, 71, 77, 9, 1, 69, 53, 3, 0] 

uniques = [i for i in lst_1 and lst_2 and lst_3 if i in lst_1 and i in lst_2 and i in lst_3]
print(uniques)


#Задание №5

n = int(input("введите число: "))
n1 = int(str(n)[::-1])
res = n + n1
print(res)



#Задание №6
speed = int(input("Ваша скорость: "))
speed1 = [i for i in range(70,200,5)]
points = []
if speed <= 70:
    print("OK")
elif speed > 70:
    for i in speed1:
        if i <= speed and i > 70:
            points.append(i)
    if len(points) > 12:
     print("Лицензия приостановлена")
    else:
     print(f"Points: {len(points)}")



#Задание №7
dict_season = {
    1: "Зима",
    2:'Зима',
    3:'Весна',
    4:'весна',
    5:'Весна',
    6:'Лето',
    7:'Лето',
    8:'Лето',
    9:'Осень',
    10:'Осень',
    11:'Осень',
    12:'Зима',
}
def season(month: int):
  print(dict_season[month])

season(12)



#Задание №8
def avarage(*args: int):
    print(sum(args) / len(args))

avarage(6,2,5,7)



#Задание №9
b = []
for i in range(100,1000):
  for k in range(999,99,-1):
   num3 = str(i * k)
   if num3 == num3[::-1]:
    b.append(int(num3))
print(max(b))


#Задание №10


#Задание №11
def bank(money,years):
    m = 0
    while m < years:
        a = money * 0.1
        money = a + money
        m = m + 1
    print(round(money))

bank(2000,6)



#Задание №12
def is_prime(number):
    nums = []
    for i in range(1,number+1):
        if number % i == 0:
            nums.append(i)
    if len(nums) > 2:
        return False
    else:
        return True

print(is_prime(97))



#Задание №13
def quantity(*args):
    numbers = {}
    for i in args:
        numbers[i] = args.count(i)   
    print(numbers)
 
quantity(1, 1, 3, 2, 1, 3, 4)



#Задание №14
def chislo(*args: int):
    for i in args:
        if i == 139:
            break
        if i % 2 != 0:
            print(i)
        

chislo(2,6,3,9,13,59,67,45,139,65,48,9,63)
 


#Задание №15
number1 = int(input("Введите число: "))  
if number1 > 0:
    print("Число полажительное")    
else:
    print("Число отрицательное")



#Задание №16
number2 = int(input("Введите число:"))
if number2 > 100 or number2 < -100:
    print("--")
else:
    print("++")



#Задание №17
number3 = int(input("Введите отрицательное число:"))
if number3 < 0:
    print(number3 * -1)



#Задание №18
first_number = int(input("Введите число:"))
if first_number % 3 == 0 and first_number % 5 == 0:
    print("ого, делится")
elif first_number % 3 == 0:
    print("арара")
elif first_number % 5 == 0:
    print("огого")
    


#Задание №19
age = int(input("Введите возраст Алмаза:"))
if age <= 17:
    print("еще рано")
elif age >= 18 and age <=39:
    print("идем служить")
elif age >= 40:
    print("уже не надо")
 


#Задание №20
text = """Advertising companies say advertising is necessary and important. 
It informs people about new products. Advertising hoardings in the street make
 our environment colourful. And adverts on TV are often funny. Sometimes they are 
 mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too.
  Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to 
  look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.

But some consumers argue that advertising is a bad thing. They say that advertising is bad for children.
 Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children
  and want to give them everything. So they use children’s ‘pester power’ to sell their products. 
  Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy
   things like cigarettes and make people waste their money."""

print(text.count("s"))
print(text.count("t"))

print(text.lower().replace("advert", "ADVERT"))



#Задание №21
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
twenty = aTuple[1][1]
print(twenty)



#Задание №22
summ = 3456
summ1 = []
summ1 += str(summ)
summ2 = 0
for i in summ1:
    summ2 += int(i)
print(summ2)



#Задание №23
text = text.replace(",", "")
text = text.replace(".", "")
text = text.lower()
most_frequent = {}
text1 = text.split()
for i in text1:
    most_frequent[i] = text1.count(i)
frequent = sorted(most_frequent.items(), key = lambda item: item[1])
print(frequent[-1])


most_word = {}
text2 = text.split()
for i in text2:
    most_word[i] = len(i)
sorted_words = sorted(most_word.items(), key = lambda item: item[1])
print(sorted_words[-1])




