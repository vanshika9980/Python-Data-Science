lst = [10, 20, 30, 20, 40]

element = int(input("Enter element: "))

if element in lst:
    lst.remove(element)
    print(lst)
else:
    print("Element not found")