def ispalindrome(name):
    s = name.replace(" ", "").lower()

    if s == s[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."


def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in name:
        if ch in vowels:
            count += 1

    return count


def frequency_of_letters(name):
    freq = {}

    for ch in name.lower():
        if ch != " ":
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

    result = []

    for key in freq:
        result.append(f"{key}-{freq[key]}")

    return ", ".join(result)