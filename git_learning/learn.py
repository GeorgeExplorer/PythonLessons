import locale #импортировать библиотеку по работе с локалями
loc = locale.getlocale() #запомнить текущую локаль
locale.setlocale(locale.LC_ALL, "Russian_Russia.1251") #изменить локаль
salary = 50000.0
print("Ваша ЗП на сегодня ", locale.format_string("%.2f", salary, grouping=True), sep="")
#locale.setlocale(locale.LC_ALL, loc) #вернуть локаль

#input("Введите число: ")
print(5 + 5)

def plus(a, b):
    return a+b
print(plus(10, 10))