# Special Pythagorean Triplet

# A Pythagorean triplet is a set of three natural numbers, 𝑎 <𝑏 <𝑐, for which,
# 𝑎2+𝑏2=𝑐2.

# For example, 32 +42 =9 +16 =25 =52.

# There exists exactly one Pythagorean triplet for which 𝑎 +𝑏 +𝑐 =1000.
# Find the product 𝑎⁢𝑏⁢𝑐.

#  a^2 + b^2 = c^2
#  a + b + c = 1000
#  a < b < c

import time

abc_sum = 1000
abc_product = 0

for a in range(0, abc_sum):
    print(f"A:",a)
    for b in range(a, abc_sum):
        # print(f"B:", b)
        for c in range (b, abc_sum):
            # print(f"C:", c)
            if a + b + c == abc_sum:
                # print (f"Sum of A, B, C:", a+b+c)
                if a**2 + b**2 == c**2:
                    abc_product = a*b*c
                    break
            elif a + b + c > abc_sum:
                continue

print(f"Product of abc:", abc_product)
print(f"Exectution Time:", time.process_time)