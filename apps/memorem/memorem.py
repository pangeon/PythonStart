# memorem 0.1 by Kamil Cecherz #
# TODO: Something is wrong. Encoding is not correct.
print("** Witaj w programie memorem **")
operation = None

while(operation != "exit"):

    print("exit - wyjście z programu")
    print("open - przegląd bazy słówek")
    print("write - edycja bazy słówek")

    operation = input("Wydaj polecenie: ")
    if(operation == "exit"):
        print("\nZakończenie programu:")
    elif(operation == "open"):
        print("Otwarto bazę słówek")
        basefile = open("txt/baza.txt", "r")

        i = 0
        for line in basefile:
            print(str(i) + ". " + line)
            i += 1

        basefile.close()

    elif(operation == "write"):
        print("Zapis słówek do bazy:")
        basefile_user = open("txt/user_base.txt", "w")
        basefile_user.write((input(
            "Wpisz nową notakę i zatwierdź (ENTER):\n Poprzedni plik zostanie nadpisany.")))
        basefile_user = open("txt/user_base.txt", "r")
        i = 0
        for line in basefile_user:
            print(str(i) + ". " + line)
            i += 1

        print("Dadano nową notatkę !")
        basefile_user.close()
