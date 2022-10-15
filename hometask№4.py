
#Задние №1
my_list = ["cd1", "cd2", "cd3", "cd4", "cd5", "cd6", "cd7", "cd8", "cd9", "cd10"]
my_listb = my_list[:]
my_list[3] = my_list[7]
my_list[7] = my_listb[3]
print(my_list)



#Задание №2
my_fruits = ["apple", "berry", "banana", "watermelon", "lemon"]
my_fav_fruits = ["apple", "watermelon", "banana"]
for fruits in my_fruits:
    if fruits in my_fav_fruits:
        print("Мое любимое" + " " + fruits)
        


#Задание №3
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(list1[2:7])



#Задание №4
numbers = [1,2,3,4,5,6,7,8,9]
numbers.reverse()
print(numbers)



#Задание №5
numbers1 = list(range(1,11,1))
print(numbers1)



#Задание №6
a = [1,3,4,5]
b = [4,5,6,7]
del b [:2]
print(a,b)



#Задание №7
print(min(numbers1))



#Задагие №9
print(sum(numbers1))



#Задание №10
print(sum(numbers1) / len(numbers1))



#Задание №8
numbers1.clear()
print(numbers1)



#Задание №11
numbers2 = [2,4,6,8,10,12,14,16,18,20]
for nomers in numbers2:
    print(nomers)
