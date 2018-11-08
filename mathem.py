## // jak rozwiązań równanie poprzez sprawdzanie wartości w pętli ?? 
#def foo(x):   
#    if (x**2 + 2*x == 8):
#        print("Rozwiązaniem jest liczba: " + x)
#        return x;

#x = 0
#f = foo(2)
#while(f != 0):
#    x += 1

#foo(2)

#if(foo(x) == 8):
#    print(x)
#else:
#    print("Dla podanej całowitej liczby x: \n f(y) = x**2 + 2*x nie posiada rozwiązań."

## // jak przedstawić równanie w układzie współrzędnych

def foo(x):
    #print("Wynik: " + str(x**2+2*x+10))
    return x**2+2*x+10;

x = 0
list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while (x <= 10):    
    list[x] = foo(x)    
    x += 1

#y = input("Sprawdzenie zbioru rozwiązań:\n")

#while(True):
#    if (y == str(foo(x))):
#        print(y)
#        break
 
print(list)


