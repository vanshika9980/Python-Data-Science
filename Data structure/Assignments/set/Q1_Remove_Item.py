s = {10, 20, 30, 40, 50}

num = int(input("Enter element to remove: "))

if num in s:
    s.remove(num)
    print(s)
else:
    print("Element not found")