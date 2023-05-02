# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

print ((my_favorite_songs) [0:13])
print ((my_favorite_songs) [-13:])
print ((my_favorite_songs) [16:30])
print ((my_favorite_songs) [-26:-15])

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

a = random.sample(my_favorite_songs,3)
total_a = 0
for i in a:
    total_a += i[1]
print ('Три песни звучат' , total_a, 'минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

data = list(my_favorite_songs_dict.items())
a = random.sample(data,3)
total_a = 0
for i in a:
    total_a += i[1]
print ('Три песни звучат' , total_a, 'минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
a = random.sample(my_favorite_songs,5)
print(a)
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]


total_my_favorite_songs = 0
for i in my_favorite_songs:
    total_my_favorite_songs += i[1]
print ('Песни звучат', total_my_favorite_songs, 'минут')
import datetime
total_my_favorite_songs = (33*60) + 55
time_format = str(datetime.timedelta(seconds=total_my_favorite_songs))
print (time_format)

# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!


month_number = int(input ('Введите номер месяца:'))   
if month_number == 1:
    print ('Вы ввели январь. 31 день')
elif month_number == 2:
    print ('Вы ввели февраль. 28 дней')
elif month_number == 3:
    print ('Вы ввели март. 31 день')
elif month_number == 4:
    print ('Вы ввели апрель. 30 дней')
elif month_number == 5:
    print ('Вы ввели май. 31 день')
elif month_number == 6:
    print ('Вы ввели июнь. 30 дней')
elif month_number == 7:
    print ('Вы ввели июль. 31 день') 
elif month_number == 8:
    print ('Вы ввели август. 31 день') 
elif month_number == 9:
    print ('Вы ввели сентябрь. 30 дней') 
elif month_number == 10:
    print ('Вы ввели октябрь. 31 день') 
elif month_number == 11:
    print ('Вы ввели ноябрь. 30 дней')
elif month_number == 12:
    print ('Вы ввели декабрь. 31 день') 
else:
    print('Такого месяца нет!') 

#months = {'Январь': 31,'Февраль': 28,'Март':31}
        #'Апрель':30,
        #'Май':31,
        #'Июнь':30,
        #'Июль':31,
        #'Август':31,
        #'Сентябрь':30,
        #'Октябрь':31,
        #'Ноябрь':30,
        #'Декабрь':31}


#month_number = int(input ('Введите номер месяца:'))  
#for month, day in months.items():
#    if 1<= month_number <=12:
   #     print ('Вы ввели', month,'.',day, 'день') 
#    else:
   #     print('Такого месяца нет!')

         

# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"      


for name, code in titles.items(): 
    quantity = 0
    price = 0
    cost = 0
    for k in store[code]:
        quantity += k ['quantity'] 
        price = k ['price']
        cost += quantity*price
    print (name, '-', quantity,'шт, стоимость', cost, 'руб')

