# Task 1: Find bitwise AND of two numbers
print("\n1. Find bitwise AND of two numbers")
a1 = int(input("Enter first number: "))
b1 = int(input("Enter second number: "))
print(f"Task 1: Bitwise AND of {a1} and {b1} is {a1 & b1}")

# Task 2: Find bitwise OR of two numbers
print("\n2. Find bitwise OR of two numbers")
a2 = int(input("Enter first number: "))
b2 = int(input("Enter second number: "))
print(f"Task 2: Bitwise OR of {a2} and {b2} is {a2 | b2}")

# Task 3: Find bitwise XOR of two numbers
print("\n3. Find bitwise XOR of two numbers")
a3 = int(input("Enter first number: "))
b3 = int(input("Enter second number: "))
print(f"Task 3: Bitwise XOR of {a3} and {b3} is {a3 ^ b3}")

# Task 4: Find bitwise NOT of a number
print("\n4. Find bitwise NOT of a number")
num4 = int(input("Enter a number: "))
print(f"Task 4: Bitwise NOT of {num4} is {~num4}")

# Task 5: Input bill amount, add GST give total amount
print("\n5. Input bill amount, add GST give total amount")
bill = float(input("Enter bill amount: "))
gst_rate = float(input("Enter GST percentage (e.g. 18): "))
total_bill = bill + (bill * gst_rate / 100)
print(f"Task 5: Total amount with GST is {total_bill:.2f}")

# Task 6: Input 5 person weight find average
print("\n6. Input 5 person weight find average")
w1 = float(input("Enter weight 1: "))
w2 = float(input("Enter weight 2: "))
w3 = float(input("Enter weight 3: "))
w4 = float(input("Enter weight 4: "))
w5 = float(input("Enter weight 5: "))
avg_w = (w1 + w2 + w3 + w4 + w5) / 5
print(f"Task 6: Average weight is {avg_w:.2f}")

# Task 7: Check whether a number is even using bitwise operator
print("\n7. Check whether a number is even using bitwise operator")
num7 = int(input("Enter a number: "))
if (num7 & 1) == 0:
    print(f"Task 7: {num7} is Even")
else:
    print(f"Task 7: {num7} is Odd")

# Task 8: Input a number find its square
print("\n8. Input a number find its square")
num8 = float(input("Enter a number: "))
print(f"Task 8: Square of {num8} is {num8**2}")

# Task 9: Input a number find its cube
print("\n9. Input a number find its cube")
num9 = float(input("Enter a number: "))
print(f"Task 9: Cube of {num9} is {num9**3}")

# Task 10: Swap two numbers using XOR operator
print("\n10. Swap two numbers using XOR operator")
swap_a = int(input("Enter first number (A): "))
swap_b = int(input("Enter second number (B): "))
swap_a = swap_a ^ swap_b
swap_b = swap_a ^ swap_b
swap_a = swap_a ^ swap_b
print(f"Task 10: After swapping -> A = {swap_a}, B = {swap_b}")

# Task 11: Compare two numbers and print whether they are equal
print("\n11. Compare two numbers and print whether they are equal")
num11_a = input("Enter first value: ")
num11_b = input("Enter second value: ")
if num11_a == num11_b:
    print(f"Task 11: {num11_a} and {num11_b} are Equal")
else:
    print(f"Task 11: {num11_a} and {num11_b} are NOT Equal")

# Task 12: Check whether first number is greater than second number
print(
    "\n12. Check whether first number is greater than second number"
)
g1 = float(input("Enter first number: "))
g2 = float(input("Enter second number: "))
if g1 > g2:
    print(f"Task 12: {g1} is Greater than {g2}")
else:
    print(f"Task 12: {g1} is NOT Greater than {g2}")

# Task 13: Check whether a number is less than 50
print("\n13. Check whether a number is less than 50")
num13 = float(input("Enter a number: "))
if num13 < 50:
    print(f"Task 13: {num13} is Less than 50")
else:
    print(f"Task 13: {num13} is NOT Less than 50")

# Task 14: Compare two numbers using >= operator
print("\n14. Compare two numbers using >= operator")
ge1 = float(input("Enter first number: "))
ge2 = float(input("Enter second number: "))
if ge1 >= ge2:
    print(f"Task 14: {ge1} is Greater than or Equal to {ge2}")
else:
    print(f"Task 14: {ge1} is NOT Greater than or Equal to {ge2}")

# Task 15: Check whether two values are not equal
print("\n15. Check whether two values are not equal")
neq1 = input("Enter first value: ")
neq2 = input("Enter second value: ")
if neq1 != neq2:
    print(f"Task 15: {neq1} and {neq2} are NOT Equal")
else:
    print(f"Task 15: {neq1} and {neq2} are Equal")

# Task 16: Check whether a number exists in a list
print("\n16. Check whether a number exists in a list")
user_list = [10, 20, 30, 40, 50]
print(f"Sample List: {user_list}")
search_num = int(input("Enter a number to search in list: "))
if search_num in user_list:
    print(f"Task 16: {search_num} Exists in the list")
else:
    print(f"Task 16: {search_num} does NOT exist in the list")

# Task 17: Calculate compound interest
print("\n17. Calculate compound interest")
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (years): "))
ci = principal * ((1 + rate / 100) ** time) - principal
print(f"Task 17: Compound Interest is {ci:.2f}")

# Task 18: Verify whether an element exists in a=[2,3,4,5,6,7] use membership operators
print(
    "\n18. Verify whether an element exists in a=[2,3,4,5,6,7] using membership operators"
)
fixed_a = [2, 3, 4, 5, 6, 7]
elem = int(input("Enter an integer to search in [2, 3, 4, 5, 6, 7]: "))
if elem in fixed_a:
    print(f"Task 18: {elem} is Present in list 'a'")
else:
    print(f"Task 18: {elem} is NOT Present in list 'a'")

# Task 19: Create two variables with same value and check using 'is'
print("\n19. Create two variables with same value and check using 'is'")
val19 = int(input("Enter an integer value for variable X and Y: "))
x = val19
y = val19
print(f"Task 19: Result of (x is y) is {x is y}")

# Task 20: Assign one variable to another and check using 'is not'
print("\n20. Assign one variable to another and check using 'is not'")
var_a = [1, 2, 3]
var_b = var_a  # Reference assignment
print(f"Variables created: var_a = {var_a}, var_b = var_a")
print(f"Task 20: Result of (var_a is not var_b) is {var_a is not var_b}")
