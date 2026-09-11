# Task 1: Check Even or Odd
print("\n1. Check Even or Odd")
num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
    print(f"Task 1: {num1} is Even")
else:
    print(f"Task 1: {num1} is Odd")

# Task 2: Check Positive, Negative, or Zero
print("\n2. Check Positive, Negative, or Zero")
num2 = float(input("Enter a number: "))
if num2 > 0:
    print(f"Task 2: {num2} is Positive")
elif num2 < 0:
    print(f"Task 2: {num2} is Negative")
else:
    print("Task 2: The number is Zero")

# Task 3: Check Divisible by both 2 and 5
print("\n3. Check Divisible by both 2 and 5")
num3 = int(input("Enter a number: "))
if num3 % 2 == 0 and num3 % 5 == 0:
    print(f"Task 3: {num3} is divisible by both 2 and 5")
else:
    print(f"Task 3: {num3} is NOT divisible by both 2 and 5")

# Task 4: Student Marks with 5 Grades
print("\n4. Input marks of a student with 5 grades")
marks = float(input("Enter student marks (0-100): "))
if marks >= 90:
    print(f"Task 4: Marks: {marks} -> Grade A")
elif marks >= 80:
    print(f"Task 4: Marks: {marks} -> Grade B")
elif marks >= 70:
    print(f"Task 4: Marks: {marks} -> Grade C")
elif marks >= 60:
    print(f"Task 4: Marks: {marks} -> Grade D")
elif marks >= 0:
    print(f"Task 4: Marks: {marks} -> Grade F")
else:
    print("Task 4: Invalid Marks")

# Task 5: Check Leap Year using Nested Conditions
print("\n5. Check Leap Year using nested conditions")
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Task 5: {year} is a Leap Year")
        else:
            print(f"Task 5: {year} is NOT a Leap Year")
    else:
        print(f"Task 5: {year} is a Leap Year")
else:
    print(f"Task 5: {year} is NOT a Leap Year")

# Task 6: Print Numbers from 1 to 10
print("\n6. Print numbers from 1 to 10")
for i in range(1, 11):
    print(f"Task 6: {i}")

# Task 7: Print Numbers from 1 to 10 and Square Them
print("\n7. Print numbers from 1 to 10 and square them")
for i in range(1, 11):
    print(f"Task 7: Number = {i}, Square = {i**2}")

# Task 8: Print Numbers 10 to 1 in Reverse
print("\n8. Print numbers from 10 to 1 in reverse order")
for i in range(10, 0, -1):
    print(f"Task 8: {i}")

# Task 9: Age Category Classification
print("\n9. Age Category Classification")
age = int(input("Enter age: "))
if 0 <= age <= 12:
    print(f"Task 9: Age {age} -> Child")
elif 13 <= age <= 19:
    print(f"Task 9: Age {age} -> Teen")
elif 20 <= age <= 59:
    print(f"Task 9: Age {age} -> Adult")
elif age >= 60:
    print(f"Task 9: Age {age} -> Senior")
else:
    print("Task 9: Invalid Age")

# Task 10: Check if Cube > 100
print("\n10. Check if cube is greater than 100")
num10 = float(input("Enter a number: "))
cube = num10**3
if cube > 100:
    print(f"Task 10: Cube of {num10} is {cube} (Above 100)")
else:
    print(f"Task 10: Cube of {num10} is {cube} (Below or equal to 100)")

# Task 11: Login System
print("\n11. Login system")
u_name = input("Enter Username: ")
p_word = input("Enter Password: ")
if u_name == "admin":
    if p_word == "python123":
        print("Task 11: Login Successful")
    else:
        print("Task 11: Incorrect Password")
else:
    print("Task 11: Invalid Username")

# Task 12: Check Vowel or Consonant
print("\n12. Check if a character is a vowel or consonant")
char = input("Enter a single character: ")
if char.lower() in "aeiou":
    print(f"Task 12: '{char}' is a Vowel")
else:
    print(f"Task 12: '{char}' is a Consonant")

# Task 13: Print Sum of First N Natural Numbers
print("\n13. Print sum of first n natural numbers")
n = int(input("Enter value for N: "))
total_sum = sum(range(1, n + 1))
print(f"Task 13: Sum of first {n} natural numbers is {total_sum}")

# Task 14: Print A to Z
print("\n14. Print A to Z")
for i in range(65, 91):
    print(f"Task 14: Letter = {chr(i)}")

# Task 15: Print Tables
print("\n15. Print tables")
table_num = int(input("Enter table number: "))
for i in range(1, 11):
    print(f"Task 15: {table_num} x {i} = {table_num * i}")
