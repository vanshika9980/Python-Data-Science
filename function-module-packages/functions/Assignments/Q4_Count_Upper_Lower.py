def count_case(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Upper case letters =", upper)
    print("Lower case letters =", lower)

text = input("Enter string: ")
count_case(text)