def even_numbers(lst):
    result = []

    for i in lst:
        if i % 2 == 0:
            result.append(i)

    return result

numbers = [1,2,3,4,5,6,7,8,9]
print(even_numbers(numbers))