while (True):
    try:
        x = int(input('Enter first parameter: '))
        y = int(input('Enter second parameter: '))
        break
    except (ValueError):
        print("You enter invalid parameters")

print("1. Addiction result is:", x+y)
print("2. Subtraction result is:", x-y)
print("3. Multiplication result is:", x*y)
print("4. Division result is:", x/y)
print("5. Exponentiation result is:", x**y)
print("6. Modulo result is:", x%y)