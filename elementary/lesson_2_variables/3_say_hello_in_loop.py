variable = input("Enter sample text or number: ")
var_type = None

while (var_type != "int" or var_type != "str" or var_type != float):
    var_type = input("Whats is your variable type ? (int, str, float): ")

    if(var_type == "int"):
        variable = int(variable)
        break

    elif(var_type == "str"):
        variable = str(variable)
        break

    elif(var_type == "float"):
        variable = float(variable)
        break

    else:
        print("Data type is incorrect")

print('You just wrote:', variable)
print('Type of your variable is:', type(variable))