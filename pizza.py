"""
def pizza():
    enter = input("Вы хотите заказать пиццу? \n 1- да \n 2- нет \n  ")
    if enter == "1":
        ingrids = {
        "1" : "Колбасой",
        "2" : "Сыром",
        "3" : "Грибом",
        "4" : "Мясо",
        "5" : "Помидором",
        }
        order = []
        while True:
         chose = input("Выберите ингридиенты: \n Хотите добавить колбасу?: \n 1-да \n 2-нет \n ")
         if chose == "1":
             order.append(ingrids.get("1"))
         chose1 = input("Хотите добавить сыр?\n 1-да \n 2-нет\n")
         if chose1 == "1":
             order.append(ingrids.get("2"))
         chose2 = input("Хотите добавить грибы?\n 1-да \n 2-нет \n ")
         if chose2 == "1":
             order.append(ingrids.get("3"))
         chose3 = input("Хотите добавить мясо?\n 1-да \n 2-нет \n ")
         if chose3 == "1":
             order.append(ingrids.get("4"))
         chose4 = input("Хотите добавить помидоры?\n 1-да \n 2-нет \n ")
         if chose4 == "1":
             order.append(ingrids.get("5"))
             bill = ', '.join(order)
             if len(bill) < 0:
              print("Вы не выбрали ингридиент")
              break
         print(f"Ваш заказ: пицца с {bill}")
         approval = input( "1- подтвердить заказ \n2- изменить заказ \n3- отменить заказ \n")
         if approval == "1":
            print("Ваш заказ принят подаждите несколько минут")
            break
         elif approval == "2":
            order = []
            continue
         else:
            break

pizza()
"""




def enter():
   enter = input("Вы хотите заказать пиццу?\n 1- да\n 2- нет\n")
   if enter == "1":
     order()
   elif enter == "2":
    enter1 = input("Хотите купить напиток?\n 1- да\n 2- нет\n")
    if enter1 == "1":
        return drinkonly()
    else:
        exit()
    
pizzas = {"Пеперони" : 420, "Четыри сезона" : 350, "Жаренная пицца" : 370, "Маргарита" : 450, "Кальцоне" : 400}
drinks = {"Кола" : 80, "Фанта" : 75, "Пепси" : 80, "Fuse Tea" : 85}

def drinkonly():
    drink = []
    d_amount = []
    for i in drinks:
        ask1 = input(f"Хатите купить {i} ?\n 1- да\n 2- нет\n")
        if ask1 == "1":
            drink.append(i)
            d_amount.append(drinks[i])
    drinks1 = ", ".join(drink)
    d_sum = sum(d_amount)
    print(f"Вы купили: {drinks1}\n Сумма оплаты: {d_sum}")
    exit()


def order():
    pizz = []
    amount = []
    for i in pizzas:
        ask = input(f"Хотите заказать {i} ?\n 1-да\n 2-нет\n")
        if ask == "1":
            pizz.append(i)
            amount.append(pizzas[i])
    pizz1 = ", ".join(pizz)
    check = sum(amount)
    if check == 0:
        print("Вы ничего не заказали")
        ask0 = input("Хотите купить напиток? \n 1-да\n 2-нет")
        if ask0 == "1":
            drinkonly()
        else:
            exit()
            
    approve = input(f"Ваш заказ: {pizz1} \n Сумма заказа: {check} \n 1- Подтвердить заказ \n 2- Изменить заказ \n 3- Добавить напиток\n 4- Отменить заказ\n")
    if approve == "1":
        print(f"Ваш заказ принят!\nСумма оплаты: {check} ")
        exit()
    if approve == "2":
        order()
    if approve == "4":
        exit()
    if approve == "3":    
       drink = []
       d_amount = []
    for i in drinks:
        ask1 = input(f"Хатите добавить {i} ?\n 1- да\n 2- нет\n")
        if ask1 == "1":
            drink.append(i)
            d_amount.append(drinks[i])
    pizz.extend(drink)
    all_item = ", ".join(pizz)
    d_sum = sum(d_amount)
    print(f"Ваш заказ: {all_item}\n Сумма оплаты: {check+d_sum}")
    approve

enter()

    