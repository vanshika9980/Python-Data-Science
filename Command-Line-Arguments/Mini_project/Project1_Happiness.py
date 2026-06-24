import sys

liked = sys.argv[1].split("-")
disliked = sys.argv[2].split("-")
numbers = sys.argv[3].split("-")

happiness = 0

for num in numbers:
    if num in liked:
        happiness += 1
    elif num in disliked:
        happiness -= 1

print(happiness)