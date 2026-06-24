filename = input("Enter file name: ")
n = int(input("Enter n: "))

with open(filename, "r") as file:
    for i in range(n):
        print(file.readline(), end="")