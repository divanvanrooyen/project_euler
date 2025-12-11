# Smallest Multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

divisible = True

uppr_lim = 21
low_lim = 2

num = 0
count = uppr_lim

while count > 0:
    for i in range(uppr_lim, low_lim, -1):
        if(count % i != 0):
            divisible = False
            break
        else:
            divisible = True

    if divisible == False:
        print(count)
        count += 20
    else:
        break

print (count)
print (time.process_time)

# while divisible
# run through every number
    # check if num has a factor 1 - 10/20 (use uppr & low)
        # true = new number
        # false = move on to next number