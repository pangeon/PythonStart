words = ["Kamil", "Radek", "Ola", "Agnieszka", "Kuba", "Zosia"]
counter = 0
max_index = len(words)

while counter < max_index:
    word = words[counter]
    print(str(counter + 1) + ". " + word)
    counter = counter + 1

print("\n")

counter = 0
for word in words:
    print(str(counter + 1) + ". " + word)
    counter += 1
