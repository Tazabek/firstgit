# Задача №1 - нужно объединить два списка, а повторяющиеся элементы выкинуть
list_names = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
get_names = ['Kuma', 'Anna', 'Adilet', 'Sasha']
list_names.extend(get_names)
print(set(list_names))

# Задача №2 - в строке нужно найти все числа и составить их в список "frg5gth57ubdfh9sbf4dsbdr0dxbf2"
my_str = "frg5gth57ubdfh67 sbf4dsbdr0dxbf 2"
result = []

for i in my_str:
    try:
     int(i)
    except ValueError:
        pass
    else:
     result.append(i)
   

print("".join(result))