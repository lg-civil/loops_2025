# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# I just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)

# print out each subject but stop when you reach history:
for subject in subjects:
    if subject == "History":
        break
    print(subject)

# skip over Science and print the rest
for subject in subjects:
    if subject == "Science":
        continue
    print(subject)

list1000 = list(range(1, 1001))

for number in list1000:
    if number > 599:
        break
    print(number)

list100 = list(range(1,1001))

for numbers in list100:
    if 300 <= numbers <= 500:
        continue
    print(numbers)
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
