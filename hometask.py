stop = "х"
add = []
while True:
    works = input("Введите название дело (или введите х для удаление):")
    if works == stop:
        break 
    else:
     add.append(works)
     print(add)

while True:
   trash = input("Введите название удаляемого дело (Введите х для зовершение работы):")
   if trash in add:
    add.remove(trash)
    print(add)
   elif trash == stop:
    break
   elif trash not in add:
    print(add, "Дело не найдено")
   else:
    continue


