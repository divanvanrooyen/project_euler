
# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1

# Where 0.1(6) means 0.16666.., and has a 1 digit recurring cycle. It can be seen that 1/7 has a 6 digit recurring cycle.
# find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal franction part.

longest_repitition_len = 0
longest_repitition_fraction = 1

for i in range(1, 1000):
    repitition_len = 0

    step = 0
    remainder_lkp = {}
    remainder_lkp[step] = 1 * 10  % i
    
    while True:        
        remainder = remainder_lkp[step] * 10 % i

        if remainder == 0:
            break

        id = next((k for k, v in remainder_lkp.items() if v == remainder), None)

        if id is None or remainder_lkp[id] == 0:
            # print(i, remainder_lkp[step], remainder)
            remainder_lkp[step + 1] = remainder
        else:
            first_id = id
            repitition_len = step + 1 - first_id
            break

        step += 1

    # print(repitition_len)
    if repitition_len > longest_repitition_len:
        longest_repitition_fraction = i
        longest_repitition_len = step + 1

print(f"longest d: {longest_repitition_fraction}: {longest_repitition_len}")
