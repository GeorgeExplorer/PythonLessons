import locale #импортировать библиотеку по работе с локалями
loc = locale.getlocale() #запомнить текущую локаль
locale.setlocale(locale.LC_ALL, "Russian_Russia.1251") #изменить локаль
locale.setlocale(locale.LC_ALL, loc) #вернуть локаль

number = 5 # создание переменной с любым числом (отрицательное, положительное и т.п)
print(number)

number = 2 # изменение действующей переменной, при помощи её повторного использования
print(number)

del number # удаление действующей переменной
# print(number) # попытка использования удаленной переменной, как рез-т — ошибка возвращения строки

digit = 4
print(digit)