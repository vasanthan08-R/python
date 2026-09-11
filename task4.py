# 1. Electricity Bill
units = float(input("1. Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print(f"Total Electricity Bill: ${bill:.2f}\n")


# 2. Online Shopping Discount
amount = float(input("2. Enter total purchase amount: "))
if amount >= 500:
    discount = 0.20
elif amount >= 200:
    discount = 0.10
else:
    discount = 0.0
final_price = amount * (1 - discount)
print(f"Final Price after discount: ${final_price:.2f}\n")


# 3. ATM Withdrawal Simulation
balance = 1000.0  # Sample account balance
withdraw = float(input("3. Enter withdrawal amount: "))
if withdraw <= 0:
    print("Invalid amount!")
elif withdraw <= balance:
    balance -= withdraw
    print(f"Withdrawal successful! Remaining balance: ${balance:.2f}\n")
else:
    print("Insufficient funds!\n")


# 4. Student Grade Calculator
marks = float(input("4. Enter student marks (0-100): "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}\n")


# 5. Traffic Signal Simulation
color = input("5. Enter signal color (Red/Yellow/Green): ").strip().lower()
if color == "red":
    print("Action: STOP\n")
elif color == "yellow":
    print("Action: SLOW DOWN / PREPARE TO STOP\n")
elif color == "green":
    print("Action: GO\n")
else:
    print("Invalid Signal Color!\n")


# 6. Temperature Monitor
temp = float(input("6. Enter current temperature (°C): "))
if temp >= 40:
    print("ALERT: Critical high temperature level detected!\n")
else:
    print("Temperature is within normal range.\n")


# 7. Login System (3 Attempts)
correct_password = "python123"
attempts = 3
while attempts > 0:
    pwd = input("7. Enter password: ")
    if pwd == correct_password:
        print("Login Successful!\n")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. Attempts left: {attempts}")
if attempts == 0:
    print("Account Locked!\n")


# 8. Multiplication Table (1 to 10)
num = int(input("8. Enter number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()


# 9. Mobile Data Usage Monitor
daily_limit = 2.0  # Limit in GB per day
total_data = 0
for day in range(1, 8):
    usage = float(input(f"9. Enter GB used on Day {day}: "))
    if usage > daily_limit:
        print(f"   --> ALERT: Daily limit of {daily_limit} GB exceeded on Day {day}!")
    total_data += usage
avg_data = total_data / 7
print(f"Total Usage: {total_data:.2f} GB | Average Daily Usage: {avg_data:.2f} GB\n")


# 10. Parking Charge Calculator
hours = float(input("10. Enter parking hours: "))
if hours <= 1:
    charge = 5
elif hours <= 5:
    charge = 5 + (hours - 1) * 3
else:
    charge = 5 + (4 * 3) + (hours - 5) * 2
print(f"Total Parking Charges: ${charge:.2f}\n")


# 11. Prime Number Check
n = int(input("11. Enter number to check if prime: "))
if n > 1:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a Prime Number.\n")
    else:
        print(f"{n} is NOT a Prime Number.\n")
else:
    print(f"{n} is NOT a Prime Number.\n")


# 12. Food Ordering System
total_cost = 0
menu = {1: ("Burger", 5.0), 2: ("Pizza", 8.0), 3: ("Soda", 2.0)}
while True:
    print("Menu: 1. Burger ($5) | 2. Pizza ($8) | 3. Soda ($2) | 0. Exit")
    choice = int(input("Select option: "))
    if choice == 0:
        break
    elif choice in menu:
        item, price = menu[choice]
        total_cost += price
        print(f"Added {item}. Current Total: ${total_cost}")
    else:
        print("Invalid Choice")
print(f"Final Order Bill: ${total_cost:.2f}\n")


# 13. Attendance Tracker (10 Employees)
present_count = 0
absent_count = 0
print("13. Record Attendance (P for Present, A for Absent):")
for i in range(1, 11):
    status = input(f"Employee {i}: ").strip().upper()
    if status == 'P':
        present_count += 1
    else:
        absent_count += 1
print(f"Present: {present_count} | Absent: {absent_count}\n")


# 14. Fuel Bill Calculator
rate_per_liter = 1.5
while True:
    qty = float(input("14. Enter fuel quantity in liters (0 to stop): "))
    if qty == 0:
        break
    print(f"   Fuel Bill: ${qty * rate_per_liter:.2f}")
print("Fuel billing closed.\n")


# 15. Bus Ticket Charges by Age
while True:
    age = int(input("15. Enter passenger age (0 to stop): "))
    if age == 0:
        break
    if age < 5:
        ticket = 0  # Free
    elif age <= 60:
        ticket = 20
    else:
        ticket = 10  # Senior discount
    print(f"   Ticket Price: ${ticket}")
print("Ticketing process completed.\n")


# 16. Number Pattern (Descending length)
print("16. Pattern:")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()


# 17. Diamond Pattern
print("17. Diamond Pattern:")
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
print()


# 18. Hollow Pyramid Pattern
print("18. Hollow Pyramid Pattern:")
n = 5
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()


# 19. Alphabet Pattern
print("19. Alphabet Pattern:")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
print()


# 20. Inverted Pyramid Pattern
print("20. Inverted Pyramid Pattern:")
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * (2 * i - 1))
