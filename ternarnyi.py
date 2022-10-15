
# Задание №1
age = int(input("Возраст: ")) 
age1 = "Доступ разрешен" if age >= 18 and age <= 50 else "Вы уже старый" if age > 50 else "иди домой"
print(age1)


# Задание №2
my_passwords = ["qwerty", "12345678"] 
user_input = input("Введите пароль: ") 
user = "Пароль верный" if user_input in my_passwords else "Неверный пароль"
print(user)



# Задание №3
number = int(input("Пожалуйста ведите цифру: ")) 
number1 = "четным" if number % 2 == 0 else "нечетным"
print(f"Ваша цифра {number} является {number1}")



# Задание №4
boolean = False
boolean1 = "является истиной" if boolean == True else "является ложью"
print(f"{boolean} {boolean1}")



# Задание №5
name = input("Ваше имя: ").title()
names = ["Mark", "Kate", "Anna", "Smit"] 
names1 = "в нашем классе " if name in names else "не в нашем классе"
print(f"{name} {names1}" )



# Задание №6
lst = [i for i in range(10)] 
print(lst)



# Задание №7
lst1 = [i for i in range(10) if i % 2 == 0]
print(lst1)



# Задание №8
cars = ["Bmw", "Mersedes", "Lexus", "Kia", "Lada"] 
newcars = [i for i in cars if "a" in i]
print(newcars)



# Задание №9
squares = [i ** 2 for i in range(10)] 
print(squares)
