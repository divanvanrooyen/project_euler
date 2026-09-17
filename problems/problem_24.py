# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# n! / (n-k)! when k <= n and 0 when k > n 

def gen_permute(prefix, pool):
    pool = pool[:prefix] + pool[prefix + 1:]
    print(f"PREFIX: {prefix}, POOL: {pool}")

    for n, item in enumerate(pool):
        if len(pool) > 0:
            # print(f"NEW ITER POOL: {pool}")
            gen_permute(n, pool)

for prefix, digit in enumerate(digits):
    # print(digits[prefix], gen_permute(prefix, digits))
    gen_permute(prefix, digits)
    
