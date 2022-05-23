# More info abou types: https://www.w3schools.com/python/python_datatypes.asp

variable = input("Enter sample text or number: ")
var_type = input("Whats is your variable type ? (int, str, float): ")

if(var_type == "int"):
    variable = int(variable) # More info about casting: https://www.w3schools.com/python/python_casting.asp
    
elif(var_type == "str"):
    variable = str(variable)

elif(var_type == "float"):
    variable = float(variable)

else:
    print("Data type is incorrect")

print('You just wrote:', variable)
print('Type of your variable is:', type(variable))