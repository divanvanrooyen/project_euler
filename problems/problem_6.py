
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