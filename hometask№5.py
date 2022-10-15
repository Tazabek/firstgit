
#Задание №1
fruits = ["яблоко", "банан", "киви", "арбуз", "Арбуз", "Манго", "Груша"]
for i, word in enumerate(fruits, 1):
    print(f"{i}.{word}")


#Задание №2
lst1 = [1, 3, 5, 7, 9]
lst2 = [3, 8, 6, 5]
del lst1[1],lst1[2]
print(lst1,lst2)



#Задание №3
lst = [1, 4, 3, 42, 48, 34, 4, 5, 10, 7, 8, 9]
for nums in lst:
    if nums % 2 == 0:
       nums1 = nums / 4
       print(nums1)  


#Задание №4
num = 3384456779
max = 0
while num > 0:
    last = num % 10
    if last > max:
        max = last
        print("Максимальная цифра:",max)


#Задание №5
dana_data = '01.01.2000'
data = {"01." : "первое",
        "01" : "января",
        "2000" : "2000 года"}
print (data.get("01."), data.get("01"), data.get("2000") )   



#Задание №6,7
my_list = [1, 2, 3, 4, 5, 5, 4, 5, 6, 7, 8, 10, 10, -1, -2, -1]
print(set(my_list))



#Задание №8
day = input("Введите номер дня:")
month = input("Введите номер месяца:")
year = input("Введите год:")
if len(day) == 2 and int(day) >= 1 and int(day) <= 31 and len(month) == 2 and int(month) >= 1 and int(month) <= 12 and len(year) == 4 and int(year) >= 1 and int(year) <= 9999:
    print(f"{day}.{month}.{year}")
else:
    print("Вы неправильно ввели дату")





