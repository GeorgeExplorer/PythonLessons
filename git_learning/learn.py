import locale #импортировать библиотеку по работе с локалями
loc = locale.getlocale() #запомнить текущую локаль
locale.setlocale(locale.LC_ALL, "Russian_Russia.1251") #изменить локаль
locale.setlocale(locale.LC_ALL, loc) #вернуть локаль
print("%.2f", any value)