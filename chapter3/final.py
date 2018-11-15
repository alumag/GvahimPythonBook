for number in range(50 + 1):
    if (number / 10) % 1 == 0:
        # the number if decimal
        print(number // 10)
    else:
        # the number has a floating point
        print(number / 10)
