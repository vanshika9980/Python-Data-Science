filename = input("Enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

print(lines)