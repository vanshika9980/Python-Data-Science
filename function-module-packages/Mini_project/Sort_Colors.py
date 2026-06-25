def sort_colors(color_string):
    colors = color_string.split("-")
    colors.sort()
    return "-".join(colors)

color_input = input("Enter colors separated by hyphen: ")

result = sort_colors(color_input)

print("Sorted colors:", result)