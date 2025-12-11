# Summation of Primes

# The sum of the primes below 10 is 2 +3 +5 +7 =17.

# Find the sum of all the primes below two million.

import math

threshold = 2000000
sum_primes = 0

for i in range(2, threshold):
    if all (i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)):
        print(f"prime: ", i)
        if i > threshold:
            break
        else:
            sum_primes += i

print(f"Sum of Primes:", sum_primes)