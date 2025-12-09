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