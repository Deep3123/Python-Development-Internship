# Q1 Write a Python program that prints "Hello, World!" to the console.
print("Hello, World!")



# Q2. Create variables to store your name, age, and favorite hobby. Print these variables.
name = "Deep"
age = 20
favorite_hobby = "Reading"
print("Name:", name)
print("Age:", age)
print("Favorite Hobby:", favorite_hobby)



# Q3 Add comments to your code explaining what each line does.
# This line prints "Hello, World!" to the console.
print("Hello, World!")

# Creating a variable to store the name.
name = "Your Name"
# Creating a variable to store the age.
age = 25
# Creating a variable to store the favorite hobby.
favorite_hobby = "Reading"
# Printing the name variable.
print("Name:", name)
# Printing the age variable.
print("Age:", age)
# Printing the favorite hobby variable.
print("Favorite Hobby:", favorite_hobby)



# Q4. Write a Python program that takes an integer input from the user and prints whether the number is positive, negative, or zero.
number = int(input("Enter an integer: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# Q5. Create a program that checks if a given year is a leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")



# Q6. Write a Python program to print the first 10 natural numbers using a for loop.
for i in range(1, 11):
    print(i)



# Q7 Create a program that prints the multiplication table of a given number using a while loop.
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1



# Q8. Write a Python program that iterates through numbers 1 to 10 and prints each number. Use the continue statement to skip numbers that are divisible by 3.
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)



# Q9 Create a program that stops printing numbers when it encounters a number greater than 5 using the break statement.
for i in range(1, 11):
    if i > 5:
        break
    print(i)



# Q10 Define a function called greet that takes a name as an argument and prints "Hello, [name]!".
def greet(name):
    print(f"Hello, {name}!")



# Q11. Create a function that takes two numbers as arguments and returns their sum.
def add_numbers(a, b):
    return a + b

# Test the functions
greet("Alice")
print("Sum:", add_numbers(3, 5))