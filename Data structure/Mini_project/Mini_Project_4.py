text = input("Enter the string: ")

words = text.split()
count = 0

for word in words:
    word = word.strip(".,!?;:").lower()
    if "alex" in word:
        count += 1

print(count)