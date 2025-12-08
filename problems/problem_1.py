num = 0
natural_numbers_sum = 0

while num < 1000:
    if num%3 == 0 or num%5 == 0:
        natural_numbers_sum += num

    num += 1

print(f"Sum of all the multiples of 3 or 5 below 1000 = ", natural_numbers_sum)