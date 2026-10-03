# 1. Print first N natural numbers
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(i, end=" ")
print()

# 2. Print first N even natural numbers
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(2 * i, end=" ")
print()

# 3. Print first N odd natural numbers
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(2 * i - 1, end=" ")
print()

# 4. Print first N multiples of 3
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(3 * i, end=" ")
print()

# 5. Print first N multiples of 5
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(5 * i, end=" ")
print()

# 6. Print all multiples of 2 till N
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 7. Print all numbers which are multiples of either 2 or 3 till N
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0:
        print(i, end=" ")
print()
'''
# 8. Print all numbers which are multiples of either 2, 5, or 7 till N
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    if i % 2 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
print()
'''
'''# 9. Print first N multiples of either 3, 5, or 7
n = int(input("Enter the number: "))
count = 0
num = 1
while count < n:
    if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print(num, end=" ")
        count += 1
    num += 1
print()'''

# 10. Sum of all digits in a positive integer
num = int(input("Enter the number: "))
total_sum = 0
temp = num
while temp > 0:
    total_sum += temp % 10
    temp //= 10
print(total_sum)

# 11. Count the number of digits in a positive integer
num = int(input("Enter the number: "))
count = 0
temp = num
while temp > 0:
    count += 1
    temp //= 10
print(count)

# 12. Find factors of a given number
num = int(input("Enter the number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()

# 13. Count factors of a given number
num = int(input("Enter the number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print(count)

# 14. Check whether given number is prime or not
num = int(input("Enter the number: "))
if num < 2:
    print("No")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    print("Yes" if is_prime else "No")

# 15. Print all prime numbers from 2 up to and including 'n'
n = int(input("Enter the number: "))
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# 16. Find the greatest common factor (GCF/GCD) of 2 integers
a, b = map(int, input("Enter two numbers: ").split())
while b:
    a, b = b, a % b
print(a)

# 17. Print common factors of two positive integers n and m
n, m = map(int, input("Enter two numbers: ").split())
for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        print(i, end=" ")
print()

# 18. Fibonacci series between 0 to 50
a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b
print()

# 19. Find the factorial of a given number
num = int(input("Enter the number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)

# 20. Read a set of integers and print the sum of even and odd integers
numbers = list(map(int, input("Enter integers separated by space: ").split()))
even_sum = sum(x for x in numbers if x % 2 == 0)
odd_sum = sum(x for x in numbers if x % 2 != 0)
print(f"Sum of Even: {even_sum}, Sum of Odd: {odd_sum}")

# 21. Check whether given number is Palindrome or not
num = int(input("Enter the number: "))
temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if num == rev:
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is not a Palindrome")

# 22. Check whether a number is an Armstrong number or not
num = int(input("Enter the number: "))
num_str = str(num)
power = len(num_str)
armstrong_sum = sum(int(digit) ** power for digit in num_str)

if armstrong_sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
