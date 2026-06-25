t = (10, 20, 30, 40, 50)

num = int(input("Enter element: "))

if num in t:
    print("Index =", t.index(num))
else:
    print("Element not found")