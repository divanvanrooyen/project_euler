# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

num = 2**1000
sum_digits = 0

for i in range(0, len(str(num))):
    num_str = (str(num)[i])
    sum_digits += int(num_str)

print(f"Sum of digits:", sum_digits)
