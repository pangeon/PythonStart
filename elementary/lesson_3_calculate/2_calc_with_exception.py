try:
    x = int(input('Enter first parameter: '))
    y = int(input('Enter second parameter: '))
except (ValueError):
    print("You enter invalid parameters, I must use default value for its:")
    print("x = 0")
    print("y = 1\n")
    
    x = 0 
    y = 1

print("1. Addiction result is:", x+y)
print("2. Subtraction result is:", x-y)
print("3. Multiplication result is:", x*y)
print("4. Division result is:", x/y)
print("5. Exponentiation result is:", x**y)
print("6. Modulo result is:", x%y)