is_fast = True
if is_fast:
    car = "ferrari"
else:
    car = "tico"
    #print(car)

name = "ferrari" if is_fast == True else "tico"
#print(name)


a,b,c = 123,66,32
max = a if a > b and a > c else b if b > c else c
#print(max)

a2 = [i ** 2 for i in range(1,10)]
#print(a2)


my_pets = ["macentosh", "acer", "lenovo", "asus", "mac", "samsung"]
my_pets = [i.upper() for i in my_pets]
#print(my_pets)
#print(list(map(lambda x: x * 2, my_pets)))


#print(list(map(len, my_pets)))


circle = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344]
#print(list(map(round, circle, range(1,6))))


# Ниже приведен список баллов 10 студентов на экзамене по химии. Давайте отфильтруем тех, кто сдал с баллом выше 75. используя filter.
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
scores1 = list(filter(lambda s: s >= 75, scores))
print(scores1)

# Пример №2 / мы ищем в городе заведения с названием мак и мы должны их отфильтровать, чтобы выходило только "мак"
mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
mixed1 = list(filter(lambda f: f == "мак", mixed))
print(mixed1)
# Пример №3 / Следующим примером будет детектор палиндрома. «Палиндром» - это слово, фраза или последовательность, которые читаются одинаково в обе стороны. Давайте отфильтруем слова, являющиеся палиндромами, из набора (iterable) oподозреваемых палиндромов.
dromes = ("анна", "жанна", "rewire", "madam", "freer", "anutuna", "kiosk")
dromes1 = list(filter(lambda g: g[0::] == g[::-1], dromes))
print(dromes1)
# Пример №4 / четные числа
numbers = [2, 1, 3, 4, 7, 11, 18]
numbers1 = list(filter(lambda h:h%2 != 0, numbers))
print(numbers1)