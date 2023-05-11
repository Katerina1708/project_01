# Задача 2.1. 
# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0] -> мин = 0, макс = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

arr =[[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]
for i in arr:
    n = len(i)
    for a in range (n-1):
      for b in range (n-a-1):
        if i[b]>i[b+1]:
            i[b],i[b+1]=i[b+1],i[b]
    print (i,'Минимальное значение:', i[0])
    print (i,'Максимальное значение:', i[-1])
 
# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.


month = int(input("Введите номер месяца: "))
list =((1, 2, 3), 1), ((4, 5, 6), 2),((7, 8, 9), 3),((10, 11, 12),4)
def quarter_of(month:int):
  for months, quarter_of in list:
     if month in months:
        return quarter_of
print ('месяц',month, 'является частью', quarter_of(month),'квартала')

# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'Один'
# switch_it_up(3) -> 'Три'
# switch_it_up(10000) -> Нет
# Использовать условный оператор if-elif-else нельзя!

number = int(input('Введите номер: '))
dct = {0:'Ноль', 1:'Один', 2:'Два', 3:'Три', 4:'Четыре', 5:'Пять', 6:'Шесть', 7:'Семь', 8:'Восемь', 9:'Девять'}
def switch_it_up(number:int):
  j = dct.get(number)
  return j
print(switch_it_up(number))
pass

   
# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
#foo("Привет! Здравствуйте!») -> "Привет, привет"
#foo("") -> ""
#foo("О, нет!!!") -> "О, нет"

s = input ('Введите текст: ')
def remove_exclamation_marks(s):
  print(s.replace('!',''))
remove_exclamation_marks(s)


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Привет!") == "Привет"
# remove("Привет!!!") == "Привет!!"
# remove("! Привет") == "! Привет"

s = input('Введите текст: ')
def remove_last_em(s):
  print(s[:-1])
remove_last_em(s)

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Привет!") === ""
# удалить("Привет! Привет!») === ""
# удалить("Привет! Привет! Привет!») === ""
# remove("Привет, привет! Привет!») === "Привет"
# удалить("Привет! ! ! Привет, привет!») === ""
# удалить("Привет! Привет!! Привет!») === "Привет!!"
# удалить("Привет! ! ! Привет! Привет!») === "! Привет!


    
    


    

