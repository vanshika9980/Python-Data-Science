try:
    filename = input("Enter file name: ")

    file = open(filename, "r")

    content = file.read()

    print(content.title())

    file.close()

except FileNotFoundError:
    print("Error: File does not exist")