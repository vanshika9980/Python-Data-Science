try:
    filename = input("Enter the file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    with open(filename, "r") as file:
        lines = file.readlines()

    total_items = 0
    free_items = 0
    amount_to_pay = 0
    discount = 0

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        parts = line.split()

        if len(parts) < 2:
            continue

        item = parts[0]
        price = parts[1]

        if item.lower() == "discount":
            discount = int(price)

        elif price.lower() == "free":
            free_items += 1

        else:
            total_items += 1
            amount_to_pay += int(price)

    final_amount = amount_to_pay - discount

    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount_to_pay)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("Error: File not found")

except ValueError:
    print("Error: Invalid data in file")

except Exception as e:
    print("Error:", e)