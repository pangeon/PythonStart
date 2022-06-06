# Program prosi o wpisanie czegoś na klawiaturze w konsoli,
# wymyślamy formę pytania ale to być cokolwiek,
# metoda input nadaje zmiennej odpowiedz wartość
odpowiedz = input("Jaka jest stolica Polski") 

# instrukcja if... else sprawdza czy wpisaliśmy Warszawa
# jeśli tak warunek jest prawdziwy, a jeśli jest prawdziwy
# metoda print wyświetli napis "Brawo dobrze"
# jeśli zmienna odpowiedz nie jest słowem Warszawa
# metoda print wyświetli napis "To miasto nie jest stolicą Polski" 
if (odpowiedz == "Warszawa"):
    print("Brawo dobrze")
else:
    print("To miasto nie jest stolicą Polski")