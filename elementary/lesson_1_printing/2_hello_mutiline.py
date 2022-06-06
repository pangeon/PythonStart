# Więcej informacji w linku poniżej jest to też przykład komentarza wielolinijkowego

"""
More info on page: https://docs.python.org/3/library/functions.html#print
Pattern: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
"""

print("Hello World")                                # standardowy sposób działania metody print domyślnie dodaje znak końca linii \n 

print('You are learning', end=": ")                 # nie wstawi entera, domyślny parametr z end="\n" został zmieniony na "; "

print('Python', end='\n\n****\n\n')                 # po słowie Python dodane zostają dwa znaki końca linii ozndobnik 
                                                    # po czym kolejne dwa znaki końca linii \n
 
print("This is a" + "simple programming language.") # napisy sklejane są za pomocą operatora "+" (konktenacja)

print("Was created in " + str(1991));               # metoda str powoduje zmianę typu (rzutowanie) 
                                                    # w tym przypadku liczby 1991 na napis o tej samej treści
                                                    # napisy sklejane są za pomocą operatora "+" (konktenacja)

