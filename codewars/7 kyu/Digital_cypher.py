message = ["a", "b", "c", "d", "e", "f"]
output = []
key = 240
i = 0
pie_key = [int(item) for item in str(key)]
print(pie_key)

for character in message:
    number = ord(character) + pie_key[i] - 96
    output.append(number)
    i = (i + 1) % len(pie_key)
print(output)
# output_result = []
# print(output_result)


# b = 0
# n = 0
# while a < len(output):
#     output_result.append(pie_key+output)
#     # b = b + 1
#     # a = a + 1
#     # n = b % 4