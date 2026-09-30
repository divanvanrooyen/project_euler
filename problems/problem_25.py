# The Fibonacci sequence is defined by the recurrence relation

# Fn =  Fn-1 + Fn-2 where F1 = 1 and F2 = 1

# The 12th term, f12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000
# digits?

digit_len = 0
idx, grandparent, parent, child = 2, 1, 1, 0

while True:

    if digit_len >= 1000: break
    else: idx += 1

    child = parent + grandparent
    grandparent = parent
    parent = child
    digit_len = len(str(child))

print(idx, child)