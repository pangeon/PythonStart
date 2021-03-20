operation = input(
    "\n-sum (sum)"
    + "\n-min (sustraction)"
    + "\n-mult (multiplication)"
    + "\n-div (division)"
    + "\n-pow (exponentiation)\n")
print("You choose operation: " + operation + "(x, y)")

while(operation):
    x = int(input("Enter first argument\n"))
    y = int(input("Enter second argument\n"))
    print("The arguments given are:\nx = " + str(x) + " y = " + str(y))
    print("The result of the operation " + operation +
          "(" + str(x) + "," + str(y) + ") to:")

    if (operation == "sum"):
        print(x + y)
        break
    elif (operation == "min"):
        print(x - y)
        break
    elif (operation == "mult"):
        print(x * y)
        break
    elif (operation == "div"):
        if not (y == 0):
            print(x / y)
            break
        else:
            print("Division by zero is impossible")
            break
    elif (operation == "pow"):
        print(x ** y)
        break
    else:
        print("Operation " + operation + " not exist")
        operation = input(
            "\n-sum (sum)"
            + "\n-min (sustraction)"
            + "\n-mult (multiplication)"
            + "\n-div (division)"
            + "\n-pow (exponentiation)\n")
        print("You choose operation: " + operation + "(x, y)")
