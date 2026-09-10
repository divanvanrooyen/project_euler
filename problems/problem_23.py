# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant 
# if this sum exceeds .

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of 
# two abundant numbers. 
# 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the 
# greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def calc_sumDiv(n):
    sum_div = 0
    for i in range(1, n):
        if i > n/2: break
        if n % i == 0: sum_div += i
    return sum_div

def check_abundant(sum_div, n):
    if sum_div > n:
        return True
    return False

# ------
upper_limit = 28123
print("getting all abundant numbers below 28,123...")
abundant_numbers = []
for i in range(upper_limit + 1):
    sum_of_divisors = calc_sumDiv(i)
    if check_abundant(sum_of_divisors, i):
        abundant_numbers.append(i)
print(f"Amount of abundant numbers: {len(abundant_numbers)}")

# DEBUG: print(abundant_numbers[0:100])

# ------
print("getting the sums of all abundant number combinations below 28,123...")
sums_of_abundant_numbers = []
for i in abundant_numbers:
    for x in abundant_numbers:
        if x + i <= upper_limit:
            sums_of_abundant_numbers.append((i + x))

sums_of_abundant_numbers = list(set(sums_of_abundant_numbers))
largest_abundant_sum = max(sums_of_abundant_numbers)
print(f"largest abundant sum: {largest_abundant_sum} - (Should technically be ~28,123*2)")
print(f"Amount of sums of abundant numbers: {len(sums_of_abundant_numbers)}")

# DEBUG: print(sums_of_abundant_numbers[0:100])

# ------
print("checking if any given number exists in the sums of all the abundant numbers...")
calc_sum = 0
for i in range(upper_limit):
    if i not in sums_of_abundant_numbers:
        # print(f"NOT SUM OF ABUNDANT NUMBERS: {i}")
        calc_sum += i

print(f"Sum of all the positive integers which cannot be written as the sum of two abundant numbers: {calc_sum}")