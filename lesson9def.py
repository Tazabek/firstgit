#пользовательские функции
def b103():
    print("hello")

#b103() #вызов функции

def b104(massage): #параметр
    print("hello", massage)

b104("aruuke") #аргумент


def b105(a,b):
    print(a * b)

#b105(25,3)


def ispositive(x):
    if x > 0:
        return True

p = []
for i in range(-15,15):
    if ispositive(i):
        p.append(i)

#print(p)


while True:
    def calc():
        operation = input("+, - , *, /\n")
        if operation in ('+', '-' , '*', '/'):
            num1 = float(input("введите число: "))
            num2 = float(input("введите число: "))
            if operation == '+':
                print(num1+num2)
            elif num1 and num2 != float:
                print("error")
            elif operation == '-':
                print(num1-num2)
            elif operation == '*':
                print(num1*num2)
            elif operation == '/':
                print(num1/num2)
            else:
                print("ошибка")
        else:
            print("тебя же просят ввести символ! совсем!")

    calc()