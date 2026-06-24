from collections import Counter
import re

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    num_lines = len(lines)

    # Meeting Time
    if num_lines <= 12:
        meeting_time = f"{num_lines} AM"
    else:
        meeting_time = f"{num_lines - 12} PM"

    # Count word frequency
    text = " ".join(lines).lower()

    words = re.findall(r"[a-zA-Z]+", text)

    frequency = Counter(words)

    place_word = max(frequency, key=frequency.get)

    print("\nMeeting time:", meeting_time)
    print("Meeting place:", place_word.capitalize(), "Street")

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error:", e)