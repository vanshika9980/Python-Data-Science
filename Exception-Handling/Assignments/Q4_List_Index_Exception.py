numbers = [10, -5, 20, -8, 15, -12, 7, -3, 25, -30]

try:
    index = int(input("Enter index (0-9): "))

    if numbers[index] >= 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Error: Invalid Index")

except ValueError:
    print("Error: Please enter a valid integer")