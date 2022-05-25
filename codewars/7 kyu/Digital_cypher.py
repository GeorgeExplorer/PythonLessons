message = ["a", "b", "c", "d", "e", "f"]
output = []
key = 100
output_result = []
pie_key = [int(item) for item in str(key)]
print(pie_key)

for character in message:
    number = ord(character) - 96
    output.append(number)

for value in output:
    new_value = value + value in pie_key
    output_result.append(new_value)
# print(output_result)