# n! means n * (n-1) * ... * 3 * 2 * 1

# for exmaple 10! = 10 * 9 * ... * 3 * 2 * 1 = 3,628,800
# and the sum of the digites in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

# find the sum of the digits in the number 100!

n = 100
product = 1
sum = 0

for x in range(n):
    product *= (n - x)

print(f"Product: {product}")
product_string = str(product)
print(f"Product: {product}")

for i in product_string:
    sum += int(i)

print(f"Sum of Digits: {sum}")