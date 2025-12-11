# Sum Square Difference

# The sum of the squares of the first ten natural numbers is,

# 12+22+...+102=385.
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)2=552=3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 −385 =2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


count = 100

def sum_of_sqrt(count):
    sum_sqrt = 0
    for i in range(1, count+1):
        sum_sqrt += (i*i)
    
    return sum_sqrt

def sqrt_of_sum(count):
    sqrt_sum = 0
    for i in range(1, count+1):
        sqrt_sum +=i

    sqrt_sum = (sqrt_sum*sqrt_sum)

    return sqrt_sum

def differnce(sum_sqrt, sqrt_sum):
    differnce = sqrt_sum - sum_sqrt
    print(differnce)


sum_sqrt = sum_of_sqrt(count)
sqrt_sum = sqrt_of_sum(count)
differnce(sum_sqrt, sqrt_sum)