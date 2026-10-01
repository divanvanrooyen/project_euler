# Euler discovered the remarkable quadratic formula:

#  n^2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, 
# when n = 40, 4-^2 + 40 + 41 = (40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. 
# The product of the coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form: 
#       n^2 + an + b, where abs(a) < 1000 and abs(b) <= 1000
#       where abs(n) is die modulus / absolute value of n
#       eg. |11| = 11 and |-4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import math

def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # Exclude all other even numbers
    if n % 2 == 0:
        return False
    
    # Check odd factors up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
            
    return True

# Initial thoughs from what i can see is, b needs to end in a 1 / be an odd number
# in the first formula a = 1 and b = 41
# in the second formula a = -79 and b = 1601

# if you carry on over to make b even, the relastionship between abs(a) and abs(b) is 1:20
# abs(1)  + (1)     = 2, and; 
# abs(41) - (1)     = 40
# 40 / 2            = 20 
# a, b = 1, 41

# abs(-79)  + (1)   = 80, and; 
# abs(1601) - (1)   = 1600
# 1600 / 80         = 20         
# a, b = -79, 1601

# doesn't feel like coincidence
# combinations where this rule holds?:
# a) 9 & 201    =  doesn't hold
# b) 19 & 401   =  doesn't hold
# c) 29 & 601   =  doesn't hold
# Theory dies, also logically, if the next Euler's formula is a = 79 & b = 1601, it's likely the next fit

# however can't go unnoticed that n = 39 in formula 1 = 1601, i.e. last possible n = b in formula 2
# if we plug 79 into formula 2, i.e last possible n for formula 2, we get 1601 as well? 
# Okay, looks like for the 80 consecutive primes, the first half and the second half is the same, ex: 1, 2, 3, 3, 2, 1
# But its not the same for the 40 consecutive primes, those climb to 1601

# looks like b is always primes in both formulas... there are 168 prime numbers between 0 and 1000
primes = []
for n in range(0,1001):
    if is_prime(n): 
        # print(n)
        primes.append(n)

a, b = 1, 41


