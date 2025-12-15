# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# Define rules
def odd_rule(num):
    num = (3*num) + 1
    return num

def even_rule(num):
    num = num / 2
    return num


entry = 2
max_entry = 1000000
max_num = 0
max_chain = 0
num_count = 0


while entry <= max_entry:
    num = entry
    print(f"Num computing:", num)
    while num > 0:
        # print(num)
        if num % 2 == 0:
            # print(f"Even Num:",num)
            num = even_rule(num)
            num_count += 1

        elif num % 2 != 0:
            if num == 1:
                num_count += 1
                break
            else:
                # print(f"Odd Num:",num)
                num = odd_rule(num)
                num_count += 1
        
    print(f"Chain for", entry, ":", num_count)
        
    if num_count > max_chain:
        max_chain = num_count
        max_num = entry
        print(f"New max chain:", max_chain, "for entry:", max_num)
        num_count = 0
    
    num_count = 0
    entry += 1

print(f"Max Chain:", max_chain, "for entry point:", max_num)