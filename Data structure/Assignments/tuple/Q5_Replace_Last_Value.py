lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

result = []

for item in lst:
    new_tuple = item[:-1] + (100,)
    result.append(new_tuple)

print(result)