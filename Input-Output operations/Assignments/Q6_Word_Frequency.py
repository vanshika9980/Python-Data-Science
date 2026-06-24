filename = input("Enter file name: ")
word = input("Enter word: ")

with open(filename, "r") as file:
    content = file.read().lower()

count = content.split().count(word.lower())

print("Frequency:", count)