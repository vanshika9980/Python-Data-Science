s = input("Enter a string: ")

if len(s) > 0 and s[0] == 'x':
    s = s[1:]

if len(s) > 0 and s[-1] == 'x':
    s = s[:-1]

print(s)