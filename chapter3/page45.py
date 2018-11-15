####################################
#           1 - xrange             #
####################################
# in python3 the function 'xrange' renamed to 'range'
# READ MORE: https://goo.gl/oNzKcj
for number in range(40 + 1):
    print(number)

####################################
#           2 - modulo             #
####################################
for number in range(100 + 1):
    # is the number divide by 7?
    if number % 7 == 0:
        print('BOOM!')
        # the continue statement continues with the next iteration of the loop
        continue

    # is the number contain 7?
    temp_number = number
    while temp_number:
        if temp_number % 10 is 7:
            print('BOOM!')
            break   # break the inner loop
        # in python3, the / operator's output is always a float
        # the new operator // output's is an integer.
        # READ MORE: https://goo.gl/EzsSPK
        temp_number //= 10
    if temp_number is not 0:
        continue

    # finally: the number is not divide or contain 7
    print(number)
