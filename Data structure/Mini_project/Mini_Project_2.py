n = int(input("Enter number of scores: "))

scores = []

for i in range(n):
    scores.append(int(input()))

scores = list(set(scores))
scores.sort()

print(scores[-2])