# memorem 0.1 by Kamil Cecherz #
print("** Welcome in Memorem App **")
operation = None

while(operation != "exit"):

    print("exit - leave program")
    print("open - show word base")
    print("write - add new note")

    operation = input("Give the command: ")
    if(operation == "exit"):
        print("\nEnd program:")
    elif(operation == "open"):
        print("You opened words base")
        basefile = open("txt/words_base.txt", "r", encoding="utf-8")

        i = 0
        for line in basefile:
            print(str(i) + ". " + line)
            i += 1

        basefile.close()

    elif(operation == "write"):
        print("Writing notes into the file:")
        basefile_user = open("txt/notes_base.txt", "w", encoding="utf-8")
        basefile_user.write((input(
            "Type in a new note and confirm (ENTER): \n"
            + "The previous file will be overwritten.\n")))
        basefile_user = open("txt/notes_base.txt", "r", encoding="utf-8")
        i = 0
        for line in basefile_user:
            print(str(i) + ". " + line)
            i += 1

        print("Add new note !")
        basefile_user.close()
