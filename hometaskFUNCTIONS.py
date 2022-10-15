#Задание №1
"""
total = 0

while True:
    def calc():
        global total
        operation = input("+, - , *, /\nОчистить историю\n")
        if operation == 'Очистить историю':
            total = 0
        elif total != 0:
            num1 = input("введите число: ")
            try:
                float(num1)
            except ValueError:
                print('Введите только числа')
            else:
                try:
                    num1 = float(num1)
                    if operation == '+':
                        total += num1
                        print(total)
                    elif operation == '-':
                        total -= num1
                        print(total)
                    elif operation == '*':
                        total *= num1
                        print(total)
                    elif operation == '/':
                        total /= num1
                        print(total)
                    else:
                        print("ошибка")
                except ZeroDivisionError:
                    print('На нуль делить нельзя!')

        elif operation in ('+', '-' , '*', '/') and total == 0:
            num1 = input("введите число: ")
            num2 = input("введите число: ")
            try:
                float(num1)
                float(num2)
            except ValueError:
                print('Введите только числа')
            else:
                try:
                    num1 = float(num1)
                    num2 = float(num2)
                    if operation == '+':
                        total += num1 + num2
                        print(total)
                    elif operation == '-':
                        total += num1 - num2
                        print(total)
                    elif operation == '*':
                        total += num1 * num2
                    elif operation == '/':
                        total += num1 / num2
                    else:
                        print("ошибка")
                except ZeroDivisionError:
                    print('На нуль делить нельзя!')
            finally:
                print("___________________________")
        else:
            print("тебя же просят ввести символ! совсем!")

    calc()
"""

#Задание №2
a = [5,27,36,25,14,16,15,39,19,139,25,64,35]
for i in a:
        if i == 139:
            break
        elif i % 2 != 0:
         print(i)



#Задание №3
def is_year_leap(x):
    if x % 4 == 0:
        print("True")
    else:
        print("False")

is_year_leap(2024)



#Задание №4
def square(s):
    print("Периметр:", s+s+s+s)
    print("Площадь", (s*s),"**2")
    print(f"Диагонал, sqrt({(s*s)+(s*s)})")

square(5)



#Задание №5
def bank(money,years):
    m = 0
    while m < years:
        a = money * 0.1
        money = a + money
        m = m + 1
        print(money)

bank(2000,4)


#Задание №6
def is_prime(z):
    if z > 0 and z < 1000 and z % 1 == 0:
        print('True')
    else:
        print("False")

is_prime(26.6)



#Задание №7
def date(d,m,y):
    if d > 0 and d <= 30 and m > 0 and m <= 12 and y > 0 and y <= 2022:
        print("True")
    else:
        print("False")

date(2,13,2022)



#Задание №8
spisok = [1, 1, 3, 2, 1, 3, 4]
for i in spisok:
    spis = spisok.count(i)
    print(f"{i} встречается {spis} раз(-a)")


