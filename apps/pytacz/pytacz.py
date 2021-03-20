# TODO: Add a new language for capitals names
import random

print("** Pytacz version 1.1 by Kamil Cecherz **")
print("info: Enter the names of the countries in capital letters in Polish.")

my_file = open("capitals.txt", "r", encoding="utf8").read()
basefile = my_file.split("\n")

rand = random.randint(1, 52)

question = basefile[rand].split(": ")

flag = False

while(flag == False):
    print("What is the capital of the country " + question[0] + ":\n")
    answer = input("My answer is: ")

    if(question[1] == answer):
        print("Good. Bravo.")
        flag = True
    else:
        print("Unfortunately your answer is wrong !")
