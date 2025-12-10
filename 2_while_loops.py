# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
index = 0
while index < len(colors):
    if colors[index] == "yellow":
        break
    print(colors[index])
    index += 1
    # index is shorthand for index = index + 1
# explanation:
# we start with index is less lenght of colors [5]
# while index is less lenght of colors [5]

# 