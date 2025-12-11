# Largest Palindrome Product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 =91 ×99.

# Find the largest palindrome made from the product of two 3-digit numbers.

first_half = []
last_half = []

def is_palindrome(num):
    str_num = str(num)
    i = 0
    n = len(str_num)-1
    while i < len(str_num)/2:
        first_half.append(str_num[i])
        i += 1
    
    while n >= len(str_num)/2:
        last_half.append(str_num[n])
        n -= 1
    
    if first_half == last_half:
        print("Is Palindrome")
        return True
    else:
        return False

# is_palindrome(906609)

# 3 Digits, largest Palindrome
largest_palindrome = 0

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        product = x * y
        if str(product) == str(product)[::-1]: # Test for palindrome
            if product > largest_palindrome:
                largest_palindrome = product
    
print(largest_palindrome)

