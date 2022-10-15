
#Задание №1.1
number1 = int(input("Введите любое число:"))
number2 = int(input("Введите еще одно любое число:"))
if number1 > number2:
    print(f"{number1}")
elif number2 > number1:
    print(f"{number2}")

#Задание №1.2
number3 = int(input("Введите число:"))
if number3 > 0:
    print("Положительное число")
else:
    print("Отрицательное число")
    
#Задание №1.5
number4 = int(input("Введите отрицательное число:"))
if number4 < 0:
    print(number4 * -1)


#Задание №2
number5 = int(input("Ввелите первое число:"))
number6 = int(input("Введите второе число:"))
if number5 == number6:
    print("YES!!!")
else: 
    print("NO!!!")
    


#Задание №3
number7 = int(input("Введите число:"))
if number7 > 100 or number7 < -100:
    print("--")
else:
    print("++")
    


#Задание №4
month = int(input("Введите номер месяца:"))
if month >= 3 and month <= 5:
    print("Весна")
elif month >= 6 and month <= 8:
    print("Лето")
elif month >= 9 and month <= 11:
    print("Осень")
elif month == 1 or month == 2 or month == 12:
    print("Зима")
else:
    print("ОШИБКА!")
    


#Задание №5
number8 = int(input("Введите первое число:"))
number9 = int(input("Введите второе число:"))
number10 = int(input("Введите третье число:"))
if number8 > 10 and number9 > 10 and number10 > 10:
    print("YES")
else:
    print("NO")



#Задание №6
number11 = int(input("Введите первое число:"))
number12 = int(input("Введите второе число:"))
number13 = int(input("Введите третье число:"))
zero = 0
if number11 > 0:
    zero = zero + 1
if number12 > 0:
    zero = zero + 1
if number13 > 0:
    zero = zero + 1
    print("Количество положительных чисел:",zero)
else:
    print("Количество положитеьных чисел:",zero)



#Задание №7
years = int(input("Введите количество лет:"))
months = int(input("Введите количество месяцев:"))
y_amount = (years * 12) * 29
m_amount = months * 29
print(f"Количество дней:{y_amount + m_amount}")



#Задание №8
first_number = int(input("Введите число:"))
if first_number % 3 == 0 and first_number % 5 == 0:
    print("ого, делится")
elif first_number % 3 == 0:
    print("арара")
elif first_number % 5 == 0:
    print("огого")
    


#Задание №9
age = int(input("Введите возраст Алмаза:"))
if age <= 17:
    print("еще рано")
elif age >= 18 and age <=39:
    print("идем служить")
elif age >= 40:
    print("уже не надо")