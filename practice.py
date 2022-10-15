#Задание №1

name_0 = input("Введите ваше имя:")
text1 = "Привет мой друг,"
text2 = "Привет мой друг,"
text3 = "Привет мой друг,"
text4 = "Привет мой друг,"
text5 = "Привет мой друг,"
print(f"{text1}{name_0}\n{text2}{name_0}\n{text3}{name_0}\n{text4}{name_0}\n{text5}{name_0}")

#Задание №2
name = input("Как вас зовут?-")
age = input("Cколько вам лет?-")
study = input("Где вы учитесь?-")
interest = input("Какая сфера IT вас интересует?-")
language = input("На каком языке вы программируете?-")
print(f"Ваше имя:{name}")
print("ваше имя:{}".format(name))
print("ваш возраст:{}".format(age))
print(f"Ваш возраст:{age}")
print(f"Место учебы:{study}")
print("место учебы:{}".format(study))
print("сфера IT:{}".format(interest))
print(f"Сфера IT:{interest}")
print(f"Язык программирования:{language}")
print("язык программирование:{}".format(language))


#Задание №3
string = input("Введите строку:")
number = f"{string}"
print(f"Количество букв:{len(string)}")
print(len(string)*(number))


#Задание №4
def polindrom(example):
    return example == example[::-1]
print(polindrom("искатьтакси"))
print(polindrom("0777029251"))
print(polindrom("lalalal"))


#Задание №5
string1 = "python"
print("python"[0],"python"[-1])


#Задание №6
number1 = "123456789"
print(number1[::2])
print(number1[1::2])