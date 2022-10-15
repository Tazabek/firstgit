#f = open("user.txt", "r", encoding="utf-8")
#print(f)
#f.close()

#file = open("user.txt", "r", encoding="utf-8")
#file.write("hello world")

#f = open("user.txt", "r", encoding="utf-8")
#print(f.read())
num_codes = {
    "0999" : "Мегаком: ",
    "0998" : "Мегаком: ",
    "0997" : "Мегаком: ",
    "0995" : "Мегаком: ",
    "0990" : "Мегаком: ",
    "0755" : "Мегаком: ",
    "0550" : "Мегаком: ",
    "0551" : "Мегаком: ",
    "0552" : "Мегаком: ",
    "0553" : "Мегаком: ",
    "0554" : "Мегаком: ",
    "0555" : "Мегаком: ",
    "0556" : "Мегаком: ",
    "0557" : "Мегаком: ",
    "0558" : "Мегаком: ",
    "0559" : "Мегаком: ",
    "0770" : "Билайн: ",
    "0771" : "Билайн: ",
    "0772" : "Билайн: ",
    "0773" : "Билайн: ",
    "0774" : "Билайн: ",
    "0775" : "Билайн: ",
    "0776" : "Билайн: ",
    "0777" : "Билайн: ",
    "0778" : "Билайн: ",
    "0779" : "Билайн: ",
    "0220" : "Билайн: ",
    "0221" : "Билайн: ",
    "0222" : "Билайн: ",
    "0223" : "Билайн: ",
    "0224" : "Билайн: ",
    "0225" : "Билайн: ",
    "0227" : "Билайн: ",
    "0500" : "О! :",
    "0501" : "О! :",
    "0502" : "О! :",
    "0503" : "О! :",
    "0504" : "О! :",
    "0505" : "О! :",
    "0507" : "О! :",
    "0508" : "О! :",
    "0509" : "О! :",
    "0700" : "О! :",
    "0701" : "О! :",
    "0703" : "О! :",
    "0704" : "О! :",
    "0705" : "О! :",
    "0706" : "О! :",
    "0707" : "О! :",
    "0708" : "О! :",
    "0709" : "О! :",
}
while True:
    chose = input("Выберите действие:\n1-добавить\n2-выйти")
    if chose == "1":
       fio = input("Введите Ф.И.О:").title()
       fio.split()
       try:
         fio[2] in fio
         first_name = fio.split()[0]
         second_name = fio.split()[1]
         third_name = fio.split()[2]
         if len(first_name) > 2 and len(second_name) > 3 and len(third_name) > 3:
            try:
               tel = input("Введите номер телефона (пример: 0770717171) :")
               if len(tel) == 10:                           
                   try:
                       borth = int(input("Введите год рождение:"))
                       if borth > 1930 and borth < 2023:
                            place = input("Введите мосто жительство:")
                            if "г." in place or "город" in place or "city" in place:
                                oper = []
                                for i in num_codes:
                                    if tel[:4] == i:
                                        oper.append(num_codes[i])
                                lst = [fio,*oper,tel, borth, place]  
                            else:
                                print("Место проживание пиши правильно")
                                continue
                       else:
                        print("Ты шо?!-_-")
                        continue
                   except ValueError:
                    print("пиши цифры тупица!")
               else:
                print("Вы не правильно ввели номер")
                continue
            except ValueError:
                print("пиши цифрами тупица!")
                continue
       except IndexError:
            print("Введите полное Ф.И.О")
            continue
       print(lst)
       with open("user1.txt", "a", encoding="utf-8") as file1:
        print(*lst, file = file1)
    elif chose == "2":
        break          