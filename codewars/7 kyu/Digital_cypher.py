message = ["a", "b", "c", "d", "e", "f"]
output = []
key = [100]
pie_key = key[0].split()
print(pie_key)
# pie_key = [int(item) for item in str(key)]
# print(pie_key)

for character in message:
    number = ord(character) - 96
    output.append(number)

output_result = list(map(lambda x, y: x + y, pie_key, output))
print(output_result)