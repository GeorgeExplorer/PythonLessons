print("First", "line", sep=" ") #sep="value" — директива-разделитель между значениями, перечисленными -> см.след.строку
                                # -> в инструкции print(), напр. sep="|" вернет | между значениями (1|2|"hello" etc.)

print("Second line", end="!\n") #end="value" — аргумент, разделяющий строки кода любым символом или -> см.след.строку
                               # -> переносом на новую строку (end="\n")
print("Third line for example 'end' argument from Second line")

print("Special symbol 'backslash' for any symbols like \\ or \'") #обратный слэш позволяет обозначить спец.символ -> см.след.строку
                                                                  # -> внутри строковых кавычек

print("1\n2\n3") #"[value1]\n[value2]\n[value3]" — перенос строковых значений на новую строку через экранированный символ \n

print("One \t Two") #"[value1]\t[value2]" — создание табуляции через экранированный символ \t

print("Multiplication result: ", 5*5) #умножение, если будет + или - значит сложение и вычитание, соответственно

print("Exponentiation result: ", 2**4) #возведение в степень

print("Division with integer result: ", 6//4, ",", 6//2) #деление без плавающей точки(запятой) — оно же целочисленное

print("Division with float result: ", 6/4, ",", 6/2) #деление с остатком

print("Looking for min value: ", min(-1, 0, 1, 2, 3, 4)) #нахождение минимального значения из списка