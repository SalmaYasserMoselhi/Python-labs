# Tasks
# Task 1: Logical Operators
# Use logical operators to determine if a number is within a specified range.
# Write code to check if the variable number is between start and end (inclusive). Print True if it is, and False otherwise.
num = 10
start = 5
end = 15
print(start <= num <= end)


# Task 2: Logical AND, OR, NOT
# Use logical operators to check multiple conditions.
# Write code to determine if a person is eligible for a discount based on their age and whether they have_coupon. A person is eligible if they are either under 18 or over 65, or if they have a coupon. Print True if they are eligible, and False otherwise.
age = 17
have_coupon = False
print(age < 18 or age > 65 or have_coupon)


# Task 3: String Concatenation
# Combine strings to form a complete sentence.
# Write code to create a greeting message using the variable name. The greeting should be in the format: "Hello, Name!".
name = "Salma"
print("Hello, " + name)


# Task 4: String Slicing
# Extract specific parts of a string.
# Write code to get the initials of a person using the variable full_name. The initials should be the first letter of the first name and the first letter of the last name.
full_name = "Salma Yasser"
names = full_name.split(" ")
first_initial = names[0][0]
last_initial = names[1][0]
print(first_initial + last_initial)

# Task 5: String Formatting
# Format strings using different methods.
# Write code to create a sentence using the variables name and age. The sentence should be in the format: "Name is Age years old."
name = "Salma"
age = 22
print(f"{name} is {age} years old")
print("%s is %d years old" % (name, age))
print("{} is {} years old".format(name, age))