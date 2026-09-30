# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits.sort()

permutes = []
# n! / (n-k)! when k <= n and 0 when k > n 

def gen_permute(pool, pref=""):
    # print(pool, pref)
    # when do i stop?
    if len(pool) == 0: 
        permutes.append(pref)
        return

    # how do i make the problem slightly smaller and hand it to myself?
    prefix = pref

    for i, x in enumerate(pool): # for every item in the pool
        new_prefix = prefix + str(x) # add the first one to the permute
        new_pool = pool[:i] + pool[i + 1:]  #remove the item from the pool
        gen_permute(i, new_pool, new_prefix) # call again with 'new' pool


gen_permute(0, digits,"")
print(permutes[999999])

    