# TODO: Something is wrong. Program not running.

import random

print("** Pytacz wersja 1.0 by Kamil Cecherz **")
print("info: Nazwy stolic podawaj z wielkiej litery")

my_file = open("capitals.txt", "r").read()
basefile = my_file.split("\n")

rand = random.randint(1, 52)

question = basefile[rand].split(": ")

flag = False

while(flag == False):
    print("Jaka jest stolica państwa " + question[0] + ":\n")
    answer = input("Moja odpowiedź to: ")

    if(question[1] == answer):
        print("Dobrze brawo")
        flag = True
    else:
        print("Niestety odpowiedź jest błędna")
