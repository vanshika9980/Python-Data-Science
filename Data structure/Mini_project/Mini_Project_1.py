people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original Dictionary:\n")

for name, fact in people.items():
    print(f"{name}: {fact}")

# Change one fact
people["Jeff"] = "Is afraid of heights."

# Add a new person
people["Jill"] = "Can hula dance."

print("\nUpdated Dictionary:\n")

for name, fact in people.items():
    print(f"{name}: {fact}")