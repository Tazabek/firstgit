contakt_name = ["Almaz", "Aziret", "Tariel", "Zaman", "Azamat"]
name = input("введите имя контакта:").title()
#name = name.capitalize()
#for i in contakt_name:
if name in contakt_name:
        print("контакт найден")
else:
    print("контакт не найден")
