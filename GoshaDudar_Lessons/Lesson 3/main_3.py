print("First", "line", sep=" ") #sep="value" — директива-разделитель между значениями, перечисленными -> см.след.строку
                                # -> в инструкции print(), напр. sep="|" вернет | между значениями (1|2|"hello" etc.)

print("Second line", end="!\n") #end="value" — аргумент, разделяющий строки кода любым символом или -> см.след.строку
                                # -> переносом на новую строку (end="\n")
print("Third line for example 'end' argument from Second line")

print("Special symbol 'backslash' for any symbols like \\ or \'") #обратный слэш позволяет обозначить спец.символ -> см.след.строку
                                                                  # -> внутри строковых кавычек

print("1\n2\n3") #"[value1]\n[value2]\n[value3]" — перенос строковых значений на новую строку через экранированный символ \n

print("One \t Two") #"[value1]\t[value2]" — создание табуляции через экранированный символ \t

print("Arifmetic results: ", 5*5, "|", 125+125, "|", 250-100) #умножение, сложение и вычитание

print("Exponentiation result: ", 2**4) #возведение в степень
print("Exponentiation result another way: ", pow(2, 4)) #другой способ возведения в степень, через аргумент pow(value, value for expon.)

print("Division with integer result: ", 6//4, "|", 6//2) #деление без плавающей точки(запятой) — оно же целочисленное
print("Division with float result: ", 10/4, "|", 6/2) #деление с остатком

print("Arifmetic results with round function: ", round(10/4), "|", round(6+4.5)) #мат.операции с округлением чисел -> см.след.строку
                                                                                 # -> через функцию round(value1+11value2)

print("Finding the min value: ", min(-1, 0, 1, 2, 3, 4)) #нахождение минимального значения из списка
print("Finding the max value: ", max(-1, 0, 1, 2, 3, 4)) #нахождение максимального значения из списка

print("Finding the module of some value: ", abs(-55)) #нахождение модуля числа (у отрицательного - положительное)

input("Continue this expression: 25+25=") #приглашение для ввода входных данных со стороны пользователя
