numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]


name = "stephen"
new_name = [letter for letter in name]


number = range(1, 5)
new_number = [n * 2 for n in number]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)


num = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square = [pow(n, 2) for n in num]
# print(square)


list_of_strings = ["1", "1", "2", "3", "5", "8", "13", "21", "34", "55"]
new = [int(n) for n in list_of_strings]
result = [num for num in new if num % 2 == 0]
print(num)
