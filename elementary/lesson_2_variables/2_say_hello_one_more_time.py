# More info abou types: https://www.w3schools.com/python/python_datatypes.asp

variable = input("Enter sample text or number: ") # wpisujesz dane
var_type = input("Whats is your variable type ? (int, str, float): ") # określasz typ zmiennej

# konstrukcja if..elif..else pozwala na określenie zachowania się programu w określonej sytuacji
# więcej informacji: https://www.w3schools.com/python/gloss_python_elif.asp

# w zależności od zawartości zmiennej var_type program podejmie decyzję o sposobie rzutowania
# więcej informacji: https://www.w3schools.com/python/python_casting.asp

if(var_type == "int"):
    variable = int(variable)        # rzutowanie na int czyli liczbę całkowitą 
    
elif(var_type == "str"):    
    variable = str(variable)        # rzutowanie na str czyli napis

elif(var_type == "float"): 
    variable = float(variable)      # rzutowanie na float czyli ułamek

else:
    print("Data type is incorrect") # jeśli var_type nie spełni żadnego z warunków if..elif wypisze
                                    # Data type is incorrect

print('You just wrote:', variable)
print('Type of your variable is:', type(variable))

# w opisanym przypadku program wypisze w zależności od podanych danych 
    # 'Type of your variable is int'
    # 'Type of your variable is str'
    # 'Type of your variable is float'