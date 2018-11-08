import random

class Cypher:
    def __init__(self, arg):
        self.arg = arg
    def __getitem__(self, index):
        return self.arg[random.randint(0,index-1)]
    def __len__(self):
        return len(self.arg)

base_code = Cypher(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O", "P","R","S","T","U","W","Y","Z","0","1","2","3","4","5","6","7","8","9"])

r_index = len(base_code)

print("Number of indexes :" + str(r_index))

def get_code():
    i = 0
    while(i < r_index): 
        print(base_code[r_index], end='')
        i += 1
    print()

print("Your generated code:")  
i = 0
j = int(input("Enter the number of times you want to repeat the procedure:\n"))
print("Your generated code:")  
while(i < j):
    get_code()
    i += 1
