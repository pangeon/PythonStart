# przykład listy w języku Python:
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# lista pewien uporządkowany to zbiór danych, numerowanych od 0 zera, 
# każdy indeks listy odwołuje się do jednej porcji danych
# w opisanym przypadku mamy do czynienia z nazwami planet, które są napisami
# lista może różne typy danych: liczba, napis, inny obiekt, inna lista
# Dokumentacja: https://docs.python.org/pl/3/tutorial/datastructures.html

# wydruk całej listy i dodanie znaku końca linii
print(planets, "\n") 

# wydruk wybranych elementów listy odwołujemy się do nich po indeksach lista[pozycja numer]
# parametr sep pozwala określić rodzaj separatora w naszym przypadku " | "
print('1. The biggest planets in solar system are', planets[4], planets[5], sep=" | ")

# indeksy listy są numerowane od zera
# wpisując 2 w kwadratowe nawiasy odwołamy się do trzeciego elementu
# kolejno 0... 1... 2...
print('2. Third planet in solar system is: ' + planets[2]) 

# zapis pozwala na wydruk kolejnych elementów list 
# poczynając od wybranego [3]'Mars', [4]'Jupiter', [5]'Saturn', [6]'Uranus', [7]'Neptune'
print('3. Planets after Earth: ', planets[3:])

# analogicznie odwrotny zapis pozwala na wydruk kolejnych elementów do wybranego
# [0]'Mercury', [1]'Venus', [2]'Earth'
# Mars ma indeks 3 jest czarty z kolei
print('4. Three planets before: ', planets[3], 'are', planets[:3])

# metoda len w skrócie length po ang. pozwala określić m.in długość napisu
# planeta o indeksie 4 to 'Jupiter', 7 znaków
print('5. Name', planets[4], 'has', len(planets[4]), 'letters') 

# do obsługi list używamy "pętli for in" 
# co pozwala uzyskać dostęp kolejno do wszystkich elementów listy
print("6.I display planets with using \"loop for\" in:")
for planet in planets: # tymczasowa zmienna planet pobiera nazwę każdej planety z listy planets
    print(planet, end=" :: ") # nazwa planety zostaje wyświetlona wraz ze znakami " :: "

