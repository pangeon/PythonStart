words = ["Kamil", "Radek", "Ola", "Agnieszka", "Kuba", "Zosia"]
counter = 0
max_index = len(words) # 6

while counter < max_index:
   word = words[counter] # [0:5] < 6 
   print(str(counter + 1) + ". " + word) # [0:6] + str
   counter = counter + 1 # [0:5]

print("\n")

counter = 0
for word in words:
    print(str(counter + 1) + ". " + word)
    counter += 1
