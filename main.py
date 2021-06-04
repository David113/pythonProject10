import random

# ----Переменные---------------------------------------------
money = 0
lvl = 1
exp = 0
zar = 0
lvl_up = [50, 100, 200, 300, 450, 600, 800, 1000, 2000, 2003, 2002, 2001]
car_1 = "Пусто"
car1 = 0
car_2 = "Пусто"
car2 = 0
car_3 = "Пусто"
car3 = 0
car_4 = "Пусто"
car4 = 0
house_1 = "Пусто"
house1 = 0
house_2 = "Пусто"
house2 = 0
house_3 = "Пусто"
house3 = 0
house_4 = "Пусто"
house4 = 0
house_5 = "Пусто"
house5 = 0
clothes_1 = "Пусто"
clothes1 = 0
clothes_2 = "Пусто"
clothes2 = 0
clothes_3 = "Пусто"
clothes3 = 0
clothes_4 = "Пусто"
clothes4 = 0
clothes_5 = "Пусто"
clothes5 = 0
aks_1 = "Пусто"
aks1 = 0
aks_2 = "Пусто"
aks2 = 0
aks_3 = "Пусто"
aks3 = 0
# ----Переменные---------------------------------------------
print('''
Добро пожаловать в мою первую игру

Суть проста - работать, покупать движимость и недвижимость, открывать новые работы и снова работать

Что бы пройти игру вам необходимо купить все, что есть в магазине и достигнуть максимального уровня, то есть 10

Для начала создайте своего персонажа
''')
name = input("Введите никнейм: ")
age = input("Введите возраст: ")
country = input("Введите страну: ")
print('''
Персонаж успешно создан

Для игры используйте команды, каждая из которых начинается со знака '/'. Основная команда, это команда - /menu 
/menu - это основное меню игры, откуда вы можете посмотреть как перейти в магазины, работы, посмотреть статистику 
персонажа или узнать другие команды. Однако эту команду нельзя вводить в магазине или на работе, что бы ввести её, 
вам нужно выйти из магазина или работы.

Удачной игры
''')
while True:
    if lvl == 10 and car_4 == "Lamborghini Huracan" and house_5 == "Небоскрёб в Дубае" and aks_3 == "Кольцо с большим бриллиантом":
        print("Поздравляю, вы прошли игру, что бы выйти введите /out")
    command_line = input()
    if command_line == '/out':
        break
    # Менюшка
    if command_line == '/menu':
        print('''
        Меню:
        1. Статистика персонажа - /stats
        2. Список команд - /help
        3. Магазины - /shops
        4. Работы - /jobs
        ''')
    # Статистика персонажа
    if command_line == '/stats':
        print("Имя: " + str(name))
        print("Возраст: " + str(age))
        print("Страна: " + str(country))
        print("Уровень: " + str(lvl))
        print("Авто: " + str(car_1) + ", " + str(car_2) + ", " + str(car_3) + ", " + str(car_4))
        print("Дома: " + str(house_1) + ", " + str(house_2) + ", " + str(house_3) + ", " + str(house_4) + ", " +
              str(house_5))
        print("Одежда: " + str(clothes_1) + ", " + str(clothes_2) + ", " + str(clothes_3) + ", " + str(clothes_4) + ", "
              + str(clothes_5))
        print("Аксессуары: " + str(aks_1) + ", " + str(aks_2) + ", " + str(aks_3))
        continue
    # Список команд
    if command_line == '/help':
        print('''
        Проверить баланс - /money
        Уровень игрока - /lvl
        Ваши авто - /mycars
        Ваши дома - /myhouses
        Ваша одежда - /myclothes
        Ваши аксессуары /myaks
        ''')
        continue
    # Другие команды
    if command_line == '/lvl':
        print("Ваш текущий уровень - " + str(lvl))
        print('''
        50 опыта - 2 lvl    450 опыта - 6 lvl  2000 опыта - 10 lvl
        100 опыта - 3 lvl   600 опыта - 7 lvl
        200 опыта - 4 lvl   800 опыта - 8 lvl
        300 опыта - 5 lvl   1000 опыта - 9 lvl
        ''')
        print("У вас " + str(exp) + " опыта")
    if command_line == '/money':
        print("Ваш баланс " + str(money) + "$")
    if command_line == '/mycars':
        print("Авто: " + str(car_1) + ", " + str(car_2) + ", " + str(car_3) + ", " + str(car_4))
    if command_line == '/myhouses':
        print("Дома: " + str(house_1) + ", " + str(house_2) + ", " + str(house_3) + ", " + str(house_4) + ", " +
              str(house_5))
    if command_line == '/myclothes':
        print("Одежда: " + str(clothes_1) + ", " + str(clothes_2) + ", " + str(clothes_3) + ", " + str(clothes_4) + ", "
              + str(clothes_5))
    if command_line == '/myaks':
        print("Аксессуары: " + str(aks_1) + ", " + str(aks_2) + ", " + str(aks_3))
    # Магазины
    if command_line == '/shops':
        while True:
            print('''
            Магазины:
            1. Автосалон - /carshop
            2. Дома - /houses
            3. Одежда - /clothes

            Выйти из магазинов - /exit
            ''')
            command_line_shops = input()
            if command_line_shops == '/exit':
                break
            # Магазины => автосалон
            if command_line_shops == '/carshop':
                while True:
                    print('''
                    1. ВАЗ 2107 - 1.000$. Купить - /buy1
                    2. Volkswagen Golf - 10.000$. Купить - /buy2
                    3. Nissan GT-R - 100.000$. Купить - /buy3
                    4. Lamborghini Huracan - 3.000.000$. Купить - /buy4

                    Выйти из автосалона - /exit
                    ''')
                    command_line_shops_car = input()
                    if command_line_shops_car == '/exit':
                        break

                    if command_line_shops_car == '/buy1' and money >= 1000 and car1 == 0:
                        money = money - 1000
                        print('Вы купили ВАЗ 2107')
                        car_1 = "ВАЗ 2107"
                        print("Авто добавлено в ваш гараж")
                        car1 = car1 + 1
                        continue
                    if command_line_shops_car == '/buy1' and money < 1000:
                        print("У вас недостаточно средств")
                    if command_line_shops_car == '/buy1' and car1 == 1:
                        print("У вас уже есть данная машина")

                    if command_line_shops_car == '/buy2' and money >= 10000 and car2 == 0:
                        money = money - 10000
                        print("Вы купили  Volkswagen Golf")
                        car_2 = "Volkswagen Golf"
                        print("Авто добавлено в ваш гараж")
                        car2 = car2 + 1
                        continue
                    if command_line_shops_car == '/buy2' and money < 10000:
                        print("У вас недостаточно средств")
                    if command_line_shops_car == '/buy2' and car2 == 1:
                        print("У вас уже есть данная машина")

                    if command_line_shops_car == '/buy3' and money >= 100000 and car3 == 0:
                        money = money - 100000
                        print("Вы купили  Nissan GT-R")
                        car_3 = "Nissan GT-R"
                        print("Авто добавлено в ваш гараж")
                        car3 = car3 + 1
                        continue
                    if command_line_shops_car == '/buy3' and money < 100000:
                        print("У вас недостаточно средств")
                    if command_line_shops_car == '/buy3' and car3 == 1:
                        print("У вас уже есть данная машина")

                    if command_line_shops_car == '/buy4' and money >= 3000000 and car4 == 0:
                        money = money - 3000000
                        print("Вы купили  Lamborghini Huracan")
                        car_4 = "Lamborghini Huracan"
                        print("Авто добавлено в ваш гараж")
                        car4 = car4 + 1
                        continue
                    if command_line_shops_car == '/buy4' and money < 3000000:
                        print("У вас недостаточно средств")
                    if command_line_shops_car == '/buy4' and car4 == 1:
                        print("У вас уже есть данная машина")
            # Магазины => дома
            if command_line_shops == '/houses':
                while True:
                    print('''
                    1. Однокомнатная квартира - 15.000$. Купить - /buy1
                    2. Дом на окраине города - 100.000$. Купить - /buy2
                    3. Трёхэтажный коттедж - 1.000.000$. Купить - /buy3
                    4. Дом в Beverly Hills - 5.000.000$. Купить - /buy4
                    5. Небоскрёб в Дубае - 50.000.000$. Купить - /buy5

                    Выход из выбора дома - /exit
                    ''')
                    command_line_shops_houses = input()
                    if command_line_shops_houses == '/exit':
                        break

                    if command_line_shops_houses == '/buy1' and money >= 15000 and house1 == 0:
                        money = money - 15000
                        print("Вы купили однокомнатную квартиру")
                        house_1 = "Однокомнатная квартира"
                        house1 = house1 + 1
                        continue
                    if command_line_shops_houses == '/buy1' and money < 15000:
                        print("У вас недостаточно средств")
                    if command_line_shops_houses == '/buy1' and house1 == 1:
                        print("У вас уже есть данный дом")

                    if command_line_shops_houses == '/buy2' and money >= 100000 and house2 == 0:
                        money = money - 100000
                        print("Вы купили дом на окраине города")
                        house_2 = "Дом на окраине города"
                        house2 = house2 + 1
                        continue
                    if command_line_shops_houses == '/buy2' and money < 100000:
                        print("У вас недостаточно средств")
                    if command_line_shops_houses == '/buy2' and house2 == 1:
                        print("У вас уже есть данный дом")

                    if command_line_shops_houses == '/buy3' and money >= 1000000 and house3 == 0:
                        money = money - 1000000
                        print("Вы купили трёхэтажный коттедж")
                        house_3 = "Трёхэтажный коттедж"
                        house3 = house3 + 1
                        continue
                    if command_line_shops_houses == '/buy3' and money < 1000000:
                        print("У вас недостаточно средств")
                    if command_line_shops_houses == '/buy3' and house3 == 1:
                        print("У вас уже есть данный дом")

                    if command_line_shops_houses == '/buy4' and money >= 5000000 and house4 == 0:
                        money = money - 5000000
                        print("Вы купили дом в Beverly Hills")
                        house_4 = "Дом в Beverly Hills"
                        house4 = house4 + 1
                        continue
                    if command_line_shops_houses == '/buy4' and money < 5000000:
                        print("У вас недостаточно средств")
                    if command_line_shops_houses == '/buy4' and house4 == 1:
                        print("У вас уже есть данный дом")

                    if command_line_shops_houses == '/buy5' and money >= 50000000 and house5 == 0:
                        money = money - 50000000
                        print("Вы купили небоскрёб в Дубае")
                        house_5 = "Небоскрёб в Дубае"
                        house5 = house5 + 1
                        continue
                    if command_line_shops_houses == '/buy5' and money < 50000000:
                        print("У вас недостаточно средств")
                    if command_line_shops_houses == '/buy5' and house5 == 1:
                        print("У вас уже есть данный дом")
            # Магазины => одежда
            if command_line_shops == '/clothes':
                while True:
                    print('''
                    Одежда:
                    1. Одежда рабочего - 100$. Купить - /buy1
                    2. Одежда офисного планктона - 1.000$. Купить - /buy2
                    3. Одежда мажора - 15.000$. Купить - /buy3
                    4. Одежда бизнесмена - 100.000$. Купить - /buy4
                    5. Одежда шейха - 1.000.000$. Купить - buy5
                    Аксессуары:
                    1. Часы ROLEX - 50.000$. Купить - /buy6
                    2. Золотая цепочка 999 пробы  - 100.000$. Купить - /buy7
                    3. Кольцо с большим бриллиантом - 1.000.000$. Купить - /buy8

                    Выйти из выбора одежды - /exit
                    ''')
                    command_line_shops_clothes = input()
                    if command_line_shops_clothes == '/exit':
                        break

                    if command_line_shops_clothes == '/buy1' and money >= 100 and clothes1 == 0:
                        money = money - 100
                        print("Вы купили одежду рабочего")
                        print("Одежда добавлена в ваш гардероб")
                        clothes_1 = "Одежда рабочего"
                        clothes1 = clothes1 + 1
                        continue
                    if command_line_shops_clothes == '/buy1' and money < 100:
                        print("У вас недостаточно средств")
                    if command_line_shops_clothes == '/buy1' and clothes1 == 1:
                        print("У вас уже есть данная одежда")

                    if command_line_shops_clothes == '/buy2' and money >= 1000 and clothes2 == 0:
                        money = money - 1000
                        print("Вы купили одежду офисного планктона")
                        print("Одежда добавлена в ваш гардероб")
                        clothes_2 = "Одежда офисного планктона"
                        clothes2 = clothes2 + 1
                        continue
                    if command_line_shops_clothes == '/buy2' and money < 1000:
                        print("У вас недостаточно средств")
                    if command_line_shops_clothes == '/buy2' and clothes2 == 1:
                        print("У вас уже есть данная одежда")

                    if command_line_shops_clothes == '/buy3' and money >= 15000 and clothes3 == 0:
                        money = money - 15000
                        print("Вы купили одежду мажора")
                        print("Одежда добавлена в ваш гардероб")
                        clothes_3 = "Одежда мажора"
                        clothes3 = clothes3 + 1
                        continue
                    if command_line_shops_clothes == '/buy3' and money < 15000:
                        print("У вас недостаточно средств")
                    if command_line_shops_clothes == '/buy3' and clothes3 == 1:
                        print("У вас уже есть данная одежда")

                    if command_line_shops_clothes == '/buy4' and money >= 100000 and clothes4 == 0:
                        money = money - 100000
                        print("Вы купили одежду бизнесмена")
                        print("Одежда добавлена в ваш гардероб")
                        clothes_4 = "Одежда бизнесмена"
                        clothes4 = clothes4 + 1
                        continue
                    if command_line_shops_clothes == '/buy4' and money < 100000:
                        print("У вас недостаточно средств")
                    if command_line_shops_clothes == '/buy4' and clothes4 == 1:
                        print("У вас уже есть данная одежда")

                    if command_line_shops_clothes == '/buy5' and money >= 1000000 and clothes5 == 0:
                        money = money - 1000000
                        print("Вы купили одежду шейха")
                        print("Одежда добавлена в ваш гардероб")
                        clothes_5 = "Одежда шейха"
                        clothes5 = clothes5 + 1
                        continue
                    if command_line_shops_clothes == '/buy5' and money < 1000000:
                        print("У вас недостаточно средств")
                    if command_line_shops_clothes == '/buy5' and clothes5 == 1:
                        print("У вас уже есть данная одежда")

                    if command_line_shops_clothes == '/buy6' and money >= 50000 and aks1 == 0:
                        money = money - 50000
                        print("Вы купили часы ROLEX")
                        print("Аксессуар добавлен в ваш гардероб")
                        aks_1 = "Часы ROLEX"
                        aks1 = aks1 + 1
                        continue
                    if command_line_shops_clothes == '/buy6' and money < 50000:
                        print("У вас недостаточно средств")
                    if command_line_shops_clothes == '/buy6' and aks1 == 1:
                        print("У вас уже есть данный аксессуар")

                    if command_line_shops_clothes == '/buy7' and money >= 100000 and aks2 == 0:
                        money = money - 100000
                        print("Вы купили золотую цепочку")
                        print("Аксессуар добавлен в ваш гардероб")
                        aks_2 = "Золотая цепочка"
                        aks2 = aks2 + 1
                        continue
                    if command_line_shops_clothes == '/buy7' and money < 100000:
                        print("У вас недостаточно средств")
                    if command_line_shops_clothes == '/buy7' and aks2 == 1:
                        print("У вас уже есть данный аксессуар")

                    if command_line_shops_clothes == '/buy8' and money >= 1000000 and aks3 == 0:
                        money = money - 1000000
                        print("Вы купили кольцо с большим бриллиантом")
                        print("Аксессуар добавлен в ваш гардероб")
                        aks_3 = "Кольцо с большим бриллиантом"
                        aks3 = aks3 + 1
                        continue
                    if command_line_shops_clothes == '/buy8' and money < 1000000:
                        print("У вас недостаточно средств")
                    if command_line_shops_clothes == '/buy8' and aks3 == 1:
                        print("У вас уже есть данный аксессуар")
    # Работы
    if command_line == '/jobs':
        while True:
            print('''
            Работы:
            1. Завод (1 уровень) - /factory
            2. Шахта (2 уровень, одежда рабочего) - /mine
            3. Офис (4 уровень, одежда офисного планктона, однокомнатная квартира) - /office
            4. Частная компания (6 уровень, одежда мажора, дом на окраине города, ВАЗ 2107) - /privatecompany
            5. Собственный бизнес (8 уровень, одежда бизнесмена, трёхэтажный коттедж, Volkswagen Golf, часы ROLEX) - /business
            6. Сеть магазинов (9 уровень, одежда шейха, дом в Beverly Hills, Nissan GT-R, золотая цепочка) - /myshops

            ! В скобках указаны то, что вам необходимо для данной работы
            ! Уровень повышается благодаря очкам опыта, которые вы получаете на работе
            Узнать свой уровень - /lvl
            Выйти из выбора работ - /exit
            ''')
            command_line_jobs = input()
            if command_line_jobs == '/lvl':
                print("Ваш текущий уровень - " + str(lvl))
                print('''
                50 опыта - 2 lvl    450 опыта - 6 lvl  2000 опыта - 10 lvl
                100 опыта - 3 lvl   600 опыта - 7 lvl
                200 опыта - 4 lvl   800 опыта - 8 lvl
                300 опыта - 5 lvl   1000 опыта - 9 lvl
                ''')
                print("У вас " + str(exp) + " опыта")
            if command_line_jobs == '/exit':
                break
            # Работы => завод
            if command_line_jobs == '/factory':
                print('''
                Добро пожаловать на начало вашего пути
                Ваша отправная точка - завод.
                Не задерживайтесь здесь надолго, вы достойны большего
                ''')
                while True:
                    print('''
                    Работать - /work
                    Узнать свой уровень - /lvl
                    Узнать баланс - /money
                    Закончить работу - /exit
                    ''')
                    command_line_jobs_factory = input()
                    if command_line_jobs_factory == '/exit':
                        break

                    if command_line_jobs_factory == '/work':
                        zar = random.randint(1, 2)
                        print("Вы заработали " + str(zar) + "$")
                        print("Опыт + 1")
                        money = money + zar
                        exp = exp + 1

                    if command_line_jobs_factory == '/money':
                        print("Ваш баланс " + str(money) + "$")

                    if command_line_jobs_factory == '/lvl':
                        print("Ваш текущий уровень - " + str(lvl))
                        print('''
                        50 опыта - 2 lvl    450 опыта - 6 lvl  2000 опыта - 10 lvl
                        100 опыта - 3 lvl   600 опыта - 7 lvl
                        200 опыта - 4 lvl   800 опыта - 8 lvl
                        300 опыта - 5 lvl   1000 опыта - 9 lvl
                        ''')
                        print("У вас " + str(exp) + " опыта")
                    for el in lvl_up:
                        if exp == el:
                            print("Ваш уровень повышен")
                            lvl = lvl + 1
                            exp = exp + 1
            # Работы => шахта
            if command_line_jobs == '/mine' and lvl < 2:
                print("Вам нужен 2 уровень")
            if command_line_jobs == '/mine' and clothes_1 != "Одежда рабочего":
                print("Вам нужна одежда рабочего")
            if command_line_jobs == '/mine' and lvl >= 2 and clothes_1 == "Одежда рабочего":
                print('''
                Работа в шахте - довольно грязная работа
                Но и платят тут больше чем на заводе
                За работу, ержан
                ''')
                while True:
                    print('''
                    Работать - /work
                    Узнать свой уровень - /lvl
                    Узнать баланс - /money
                    Закончить работу - /exit
                    ''')
                    command_line_jobs_mine = input()
                    if command_line_jobs_mine == '/exit':
                        break

                    if command_line_jobs_mine == '/work':
                        zar = random.randint(60, 150)
                        print("Вы заработали " + str(zar) + "$")
                        print("Опыт + 1")
                        money = money + zar
                        exp = exp + 1

                    if command_line_jobs_mine == '/money':
                        print("Ваш баланс " + str(money) + "$")

                    if command_line_jobs_mine == '/lvl':
                        print("Ваш текущий уровень - " + str(lvl))
                        print('''
                        50 опыта - 2 lvl    450 опыта - 6 lvl  2000 опыта - 10 lvl
                        100 опыта - 3 lvl   600 опыта - 7 lvl
                        200 опыта - 4 lvl   800 опыта - 8 lvl
                        300 опыта - 5 lvl   1000 опыта - 9 lvl
                        ''')
                        print("У вас " + str(exp) + " опыта")
                    for el in lvl_up:
                        if exp == el:
                            print("Ваш уровень повышен")
                            lvl = lvl + 1
                            exp = exp + 1
            # Работы => офис
            if command_line_jobs == '/office' and lvl < 4:
                print("Вам нужен 4 уровень")
            if command_line_jobs == '/office' and clothes_2 != "Одежда офисного планктона":
                print("Вам нужна одежда офисного планктона")
            if command_line_jobs == '/office' and house_1 != "Однокомнатная квартира":
                print("Вам нужна однокомнатная квартира")
            if command_line_jobs == '/office' and lvl >= 4 and clothes_2 == "Одежда офисного планктона" and \
                    house_1 == "Однокомнатная квартира":
                print('''
                Добро пожаловать в офис
                Мне кажется не нужно обьяснять что делать, просто работайте
                ''')
                while True:
                    print('''
                    Работать - /work
                    Узнать свой уровень - /lvl
                    Узнать баланс - /money
                    Закончить работу - /exit
                    ''')
                    command_line_jobs_office = input()
                    if command_line_jobs_office == '/exit':
                        break

                    if command_line_jobs_office == '/work':
                        zar = random.randint(250, 1000)
                        print("Вы заработали " + str(zar) + "$")
                        print("Опыт + 1")
                        money = money + zar
                        exp = exp + 1

                    if command_line_jobs_office == '/money':
                        print("Ваш баланс " + str(money) + "$")

                    if command_line_jobs_office == '/lvl':
                        print("Ваш текущий уровень - " + str(lvl))
                        print('''
                        50 опыта - 2 lvl    450 опыта - 6 lvl  2000 опыта - 10 lvl
                        100 опыта - 3 lvl   600 опыта - 7 lvl
                        200 опыта - 4 lvl   800 опыта - 8 lvl
                        300 опыта - 5 lvl   1000 опыта - 9 lvl
                        ''')
                        print("У вас " + str(exp) + " опыта")
                    for el in lvl_up:
                        if exp == el:
                            print("Ваш уровень повышен")
                            lvl = lvl + 1
                            exp = exp + 1
            # Работы => частная компания
            if command_line_jobs == '/privatecompany' and lvl < 6:
                print("Вам нужен 6 уровень")
            if command_line_jobs == '/privatecompany' and clothes_3 != "Одежда мажора":
                print("Вам нужна одежда мажора")
            if command_line_jobs == '/privatecompany' and house_2 != "Дом на окраине города":
                print("Вам нужен дом на окраине города")
            if command_line_jobs == '/privatecompany' and car_1 != "ВАЗ 2107":
                print("Вам нужна машина ВАЗ 2107")
            if command_line_jobs == '/privatecompany' and lvl >= 6 and clothes_3 == "Одежда мажора" and \
                    car_1 == "ВАЗ 2107" and house_2 == "Дом на окраине города":
                print('''
                В офисе вас заметил один из бизнесменов
                Предлогая зарлату больше, вы соглашаетесь на него работать
                ''')
                while True:
                    print('''
                    Работать - /work
                    Узнать свой уровень - /lvl
                    Узнать баланс - /money
                    Закончить работу - /exit
                    ''')
                    command_line_jobs_prcompany = input()
                    if command_line_jobs_prcompany == '/exit':
                        break

                    if command_line_jobs_prcompany == '/work':
                        zar = random.randint(6000, 10000)
                        print("Вы заработали " + str(zar) + "$")
                        print("Опыт + 1")
                        money = money + zar
                        exp = exp + 1

                    if command_line_jobs_prcompany == '/money':
                        print("Ваш баланс " + str(money) + "$")

                    if command_line_jobs_prcompany == '/lvl':
                        print("Ваш текущий уровень - " + str(lvl))
                        print('''
                        50 опыта - 2 lvl    450 опыта - 6 lvl  2000 опыта - 10 lvl
                        100 опыта - 3 lvl   600 опыта - 7 lvl
                        200 опыта - 4 lvl   800 опыта - 8 lvl
                        300 опыта - 5 lvl   1000 опыта - 9 lvl
                        ''')
                        print("У вас " + str(exp) + " опыта")
                    for el in lvl_up:
                        if exp == el:
                            print("Ваш уровень повышен")
                            lvl = lvl + 1
                            exp = exp + 1
            # Работы => собственный бизнес
            if command_line_jobs == '/business' and lvl < 8:
                print("Вам нужен 8 уровень")
            if command_line_jobs == '/business' and clothes_4 != "Одежда бизнесмена":
                print("Вам нужна одежда бизнесмена")
            if command_line_jobs == '/business' and house_3 != "Трёхэтажный коттедж":
                print("Вам нужен трёхэтажный коттедж")
            if command_line_jobs == '/business' and car_2 != "Volkswagen Golf":
                print("Вам нужна машина Volkswagen Golf")
            if command_line_jobs == '/business' and aks_1 != "Часы ROLEX":
                print("Вам нужен аксессуар часы ROLEX")
            if command_line_jobs == '/business' and lvl >= 8 and clothes_4 == "Одежда бизнесмена" and \
                    car_2 == "Volkswagen Golf" and aks_1 == "Часы ROLEX" and house_3 == "Трёхэтажный коттедж":
                print('''
                Вы накопили достаточно денег, чтобы открыть свой бизнес
                ''')
                while True:
                    print('''
                    Работать - /work
                    Узнать свой уровень - /lvl
                    Узнать баланс - /money
                    Закончить работу - /exit
                    ''')
                    command_line_jobs_business = input()
                    if command_line_jobs_business == '/exit':
                        break

                    if command_line_jobs_business == '/work':
                        zar = random.randint(10000, 15000)
                        print("Вы заработали " + str(zar) + "$")
                        print("Опыт + 1")
                        money = money + zar
                        exp = exp + 1

                    if command_line_jobs_business == '/money':
                        print("Ваш баланс " + str(money) + "$")

                    if command_line_jobs_business == '/lvl':
                        print("Ваш текущий уровень - " + str(lvl))
                        print('''
                        50 опыта - 2 lvl    450 опыта - 6 lvl  2000 опыта - 10 lvl
                        100 опыта - 3 lvl   600 опыта - 7 lvl
                        200 опыта - 4 lvl   800 опыта - 8 lvl
                        300 опыта - 5 lvl   1000 опыта - 9 lvl
                        ''')
                        print("У вас " + str(exp) + " опыта")
                    for el in lvl_up:
                        if exp == el:
                            print("Ваш уровень повышен")
                            lvl = lvl + 1
                            exp = exp + 1
            # Работы => сеть магазинов
            if command_line_jobs == '/myshops' and lvl < 9:
                print("Вам нужен 9 уровень")
            if command_line_jobs == '/myshops' and clothes_5 != "Одежда шейха":
                print("Вам нужна одежда шейха")
            if command_line_jobs == '/myshops' and house_4 != "Дом в Beverly Hills":
                print("Вам нужен дом в Beverly Hills")
            if command_line_jobs == '/myshops' and car_3 != "Nissan GT-R":
                print("Вам нужна машина Nissan GT-R")
            if command_line_jobs == '/myshops' and aks_2 != "Золотая цепочка":
                print("Вам нужен аксессуар золотая цепочка")
            if command_line_jobs == '/myshops' and lvl >= 9 and clothes_5 == "Одежда шейха" and car_3 == "Nissan GT-R" \
                    and aks_2 == "Золотая цепочка" and house_4 == "Дом в Beverly Hills":
                print('''
                Ваш бизнес процветает, и вы решаете открыть сеть магазинов
                Не пора бы купить небосрёб?
                ''')
                while True:
                    print('''
                    Работать - /work
                    Узнать свой уровень - /lvl
                    Узнать баланс - /money
                    Закончить работу - /exit
                    ''')
                    command_line_jobs_myshops = input()
                    if command_line_jobs_myshops == '/exit':
                        break

                    if command_line_jobs_myshops == '/work':
                        zar = random.randint(50000, 100000)
                        print("Вы заработали " + str(zar) + "$")
                        print("Опыт + 3")
                        money = money + zar
                        exp = exp + 3

                    if command_line_jobs_myshops == '/money':
                        print("Ваш баланс " + str(money) + "$")

                    if command_line_jobs_myshops == '/lvl':
                        print("Ваш текущий уровень - " + str(lvl))
                        print('''
                        50 опыта - 2 lvl    450 опыта - 6 lvl  2000 опыта - 10 lvl
                        100 опыта - 3 lvl   600 опыта - 7 lvl
                        200 опыта - 4 lvl   800 опыта - 8 lvl
                        300 опыта - 5 lvl   1000 опыта - 9 lvl
                        ''')
                        print("У вас " + str(exp) + " опыта")
                    for el in lvl_up:
                        if exp == el:
                            print("Ваш уровень повышен, вы достигли максимального уровня - 10")
                            lvl = lvl + 1
                            exp = exp + 1
