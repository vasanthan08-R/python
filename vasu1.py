# Task 1: Find last digit of the number
print("\n1. Find last digit of the number")
num1 = int(input("Enter a number: "))
last_digit = num1 % 10
print("Task 1: Last digit is", last_digit)

# Task 2: Remove last digit of the number
print("\n2. Remove last digit of the number")
num2 = int(input("Enter a number: "))
removed_last = num2 // 10
print("Task 2: After removing last digit:", removed_last)

# Task 3: Find last 2 digits of the given number
print("\n3. Find last 2 digits of the given number")
num3 = int(input("Enter a number: "))
last_two = num3 % 100
print("Task 3: Last 2 digits are:", last_two)

# Task 4: Square the middle digit of a five-digit number
print("\n4. Square the middle digit of a five-digit number")
num4 = int(input("Enter a 5-digit number: "))
middle_digit = (num4 // 100) % 10
sq_middle = middle_digit ** 2
print("Task 4: Middle digit square:", sq_middle)

# Task 5: BMI Calculator
print("\n5. BMI Calculator")
weight = float(input("Enter weight in kg: "))
height_cm = float(input("Enter height in cm: "))
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
print("Task 5: Calculated BMI is", bmi)

# Task 6: Expand the 4-digit number
print("\n6. Expand the 4-digit number")
num6 = int(input("Enter a 4-digit number: "))
a = (num6 // 1000) * 1000
b = ((num6 // 100) % 10) * 100
c = ((num6 // 10) % 10) * 10
d = num6 % 10
print("Task 6:", a, "+", b, "+", c, "+", d)

# Task 7: Volume of Cylinder
print("\n7. Volume of Cylinder")
r = float(input("Enter radius: "))
h = float(input("Enter height: "))
vol_cyl = 3.14 * r * r * h
print("Task 7: Volume of Cylinder is", vol_cyl)

# Task 8: Volume of Cuboid
print("\n8. Volume of Cuboid")
l = float(input("Enter length: "))
b_cub = float(input("Enter breadth: "))
h_cub = float(input("Enter height: "))
vol_cub = l * b_cub * h_cub
print("Task 8: Volume of Cuboid is", vol_cub)

# Task 9: Convert centimeter to meter
print("\n9. Convert centimeter to meter")
cm = float(input("Enter length in cm: "))
m = cm / 100
print("Task 9:", cm, "cm =", m, "meters")

# Task 10: Calculate speed (S = D / T)
print("\n10. Calculate speed (S = D / T)")
distance = float(input("Enter distance: "))
time_val = float(input("Enter time: "))
speed = distance / time_val
print("Task 10: Calculated Speed is", speed)
