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
     print(contack_name)

  elif act == "3":
    search = input("Введите имя контакта которого ищите:").capitalize()
    contack_name[search]
    print(f"Контакт найден {search}", contack_name.get(search,'контакт не найден'))
  
  elif act == "4":
     for i, e in contack_name.items():
        print(i, e)
