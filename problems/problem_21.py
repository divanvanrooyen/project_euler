# let d(n) be defined as the sum of proper divisors of n (number less than n which divide evenly into n)
# if d(a) = b and d(b) = a where a != b, then a and b are an amicable pair and each of a and b are called 
# amicable numbers

# for example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220

# Evanluate the sum of all the amicable numbers under 10,000

def isAmicable(n):    
    a = n
    sum_a = 0
    
    for i in range(1, a):
        if i < a and a % i == 0:
            # print(f"i ({i}) less than a and evenly divisible")
            sum_a += i

    b = sum_a 
    sum_b = 0

    for n in range(1, b):
        if n < b and b % n == 0:
            # print(f"n ({n}) less than b and evenly divisable")
            sum_b += n

    if sum_a == b and sum_b == a and a != b:
        print(f"Amicable Match - A: {a}, Sum a: {sum_a} and B: {b} Sum b: {sum_b}")
        return True
    else:
        return False

amicable_sum = 0
for i in range(10000):
    if isAmicable(i): amicable_sum += i

print(f"Amicable Sum: {amicable_sum}")