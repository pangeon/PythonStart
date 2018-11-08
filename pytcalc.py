operation = input("Podaj rodzaj wykonywanej operacji, dostępne:\n-sum (suma) \n-min (odejmowanie) \n-mult (mnożenie) \n-div (dzielenie) \n-pow (potęgowanie)\n")
print("Wybrałeś operacje: " + operation + "(x, y)")

while(operation):
    x = int(input("Wpisz pierwszy argument\n"))
    y = int(input("Wpisz pierwszy argument\n"))
    print("Podane argumenty to:\nx = " + str(x) + " y = " + str(y))
    print("Wynik operacji " + operation + "(" + str(x) + "," + str(y) + ") to:")

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
            print("Dzielenie przez zero jest niemożliwe")
            break
    elif (operation == "pow"):
        print(x ** y)
        break
    else:
        print("Operacja " + operation + " nie istnieje")
        operation = input("Podaj rodzaj wykonywanej operacji, dostępne:\n-sum (suma) \n-min (odejmowanie) \n-mult (mnożenie) \n-div (dzielenie) \n-pow (potęgowanie)\n")
        print("Wybrałeś operacje: " + operation + "(x, y)")



