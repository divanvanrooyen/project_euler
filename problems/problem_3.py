prime_factors = []

factor = 2
num = 600851475143

while num >= 2:
    if num % factor == 0:
        prime_factors.append(factor)
        num = num / factor
    else:
        factor += 1

print(prime_factors)