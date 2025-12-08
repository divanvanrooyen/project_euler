x = 1
y = 2
z = 0

max_val = 4000000
even_val_sum = 2

while x < max_val and y < max_val:
    z = x + y      # work out the next number in Fibonacci Sequence
    if(z%2 == 0):  # Chekck if the next number is even, if so add to the sum
        even_val_sum += z
        # print(f"x = ",x," y = ",y," z = ", z)
    x = y   # swap values around for next interation 
    y = z
    
print(f"sum of the even-valued terms = ", even_val_sum)