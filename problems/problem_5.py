
divisible = True

uppr_lim = 21
low_lim = 2

num = 0
count = uppr_lim

while count > 0:
    for i in range(uppr_lim, low_lim, -1):
        if(count % i != 0):
            divisible = False
            break
        else:
            divisible = True

    if divisible == False:
        print(count)
        count += 20
    else:
        break

print (count)
# while divisible
# run through every number
    # check if num has a factor 1 - 10/20 (use uppr & low)
        # true = new number
        # false = move on to next number