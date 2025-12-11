# 10 001st Prime

# By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

prime_count = 10001 
count = 1
num = 3
primes = [2]

while count < prime_count:
    is_prime = True
    for i in range(3, int(math.sqrt(num) + 1), 2):
        if num % i == 0:
            is_prime = False

    if is_prime:
        primes += [num]
        count += 1

    num += 2

print(primes[-1])