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

# list1000 = list(range(1, 1001))

# for number in list1000:
#     if number > 599:
#         break
#     print(number)

# list100 = list(range(1,1001))

# for numbers in list100:
#     if 300 <= numbers <= 500:
#         continue
#     print(numbers)



applicants_for_credit = ["Alice", "Bob", "Charlie", "David", "Eve"]
credit_scores = [720, 680, 590, 610, 750]
# zip the two lists together and print
# each applicant'S NAME along with their credit scores
# if the score is below 600, skip over that applicant
# and approve their credit.
for applicant, score in zip(applicants_for_credit, credit_scores):
    if score < 600:
        continue
    print(applicant + " approved for credit score " + str(score))




# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
# subjects = ["Math", "Science", "History", "Art"]
# for index in range(len(subjects)-1):
#     print('Subject ' + str(index) + ": " + subject[index])

# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
total = 0
for number in numbers:
    # add each number to total
    total += number
    # shorthand for total = total + number
print("total: " , total)


new_numbers = list(range(1, 261))
total_1 = 0
# this creates a list of numbers 1from 1 to 260
# Challenge: sum up all numbers from 1 to 260
# amd print the total
for numbers in new_numbers:
    total_1 += numbers
print("the total sum from 1 to 260: ", total_1)