
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

for i in range(6, 7):
    repitition_len = 0

    step = 0
    remainder_lkp = {}
    remainder_lkp[step] = 1 * 10  % i
    first_i = 0
    last_i = 0
    
    while True:        
        remainder = remainder_lkp[step] * 10 % i

        if remainder == 0: 
            last_i = step
            break
        try:
            print(list(remainder_lkp.keys())[list(remainder_lkp.values()).index(remainder)])
            last_i = step
            break
        except:
            print(i, remainder_lkp[step], remainder)
            remainder_lkp[step + 1] = remainder

        step += 1

    print(f"fraction: {i}, repitition length: {last_i}")

    if step > repitition_len:
        repitition_len = step
