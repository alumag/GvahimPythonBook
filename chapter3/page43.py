a = 0
b = 1

print(a)
print(b)

while True:
    temp = a + b
    if temp >= 10000:
        break

    print(temp)
    # cool python trick!
    # READ MORE: https://goo.gl/AeeufN
    a, b = b, temp
