
is_square = 0
square_count = 0
square_sum = 0

i = 0
n = 0

while square_count < 981000:
    if i%2 != 0:            #check if sqrt is odd
        n = i*i             #calculate sqrt
        square_sum += n     #add sqrt to sum of odd sqrts
    
    square_count += 1
    i += 1

print (f"Square number count = ", square_count, "| Odd square sum = ", square_sum)

