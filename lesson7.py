"""
todo = ['закончить первый класс', "почистить зубы", "принять душ с шампунем"]
destvie = input("Выберите действие:\n1 - это добавление\n2 - это удаление\n3 - это просмотр\n")
if destvie == '3':
    for i in todo:
        print(i)
elif destvie == '1':
    delo = input("добавляй дело: ")
    todo.append(delo)
    print(f"успешно добавлено: {delo}")
elif destvie == '2':
    # remove - удаление по значению
    # del_delo = input("удалить дело: ")
    # if del_delo in todo:
    #     todo.remove(del_delo)
    # print(todo)    
    # remove - удаление по значению
    # по индексу
    del_delo = int(input("удалить дело: "))
    print(todo.pop(del_delo))
"""
contack_name = {
    "Abdulkadyr" : 969696,
    "Naima" : 9696969,
    "Zegion" : 969696,
}
while True:
  act = input("Выберите действие: \n 1-добавить нового номера \n 2-удалить существующего номера \n 3-поиск контакта по имени \n 4-вывести список контактов \n")
  if act == "1":
    new = input("Введите имя контакта:").capitalize()
    number = input("Введите номер контакта:")
    contack_name[new] = number
    for key, value in contack_name.items():
     print(key,value)
  elif act == "2":
    trash = input("Чтобы удалить введите имя контакта:").capitalize()
    del contack_name[trash]
    for i, e in contack_name.items():
        print(i, e)
  elif act == "3":
    search = input("Введите имя контакта которого ищите:").capitalize()
    contack_name[search]
    print(f"Контакт {search} {contack_name.get(search)} найден")
  
  elif act == "4":
     for i, e in contack_name.items():
        print(i, e)
