# program zapyta o treść zmiennej variable, pobierze ją z tego co
# wpiszemy do konsoli, dodając wybrany tekst zachęty: "Enter sample text or number: " 
variable = input("Enter sample text or number: ") 


print('You just wrote:', variable) # program wypisze treść zmiennej, powtórzy de facto to co napisaliśmy
print('Type of your variable is:', type(variable)) # metoda type sprawdzi typ zmiennej 

# python - dynamiczny system typów
# c++ - statyczny system typów

# w opisanym przypadku program zawsze wypisze 'Type of your variable is str'