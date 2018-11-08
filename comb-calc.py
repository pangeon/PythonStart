#header
def decorator(func):
    def wrap():
        print("===============================================")
        func()
        print("===============================================")
    return wrap 

@decorator
def welcome():
  print("Comb-Calc v 1.0 by Kamil Cecherz")

#body
def newton(x):
    if x == 1:
        return 1
    else:
        return x * newton(x-1)
    
def probability(n, k):
    if n > k:
        message = "Ilość podzbiorów " + str (k) + "-elementowych w zbiorze " + str (n) + "-elementowym"
        print(message)
        z = int (newton(n - k))
        n = int (newton(n))    
        k = int (newton(k))
        P = int (n / (k * z))
        print(str (n) + " / " + str (k) + " * " + str (z) + "\n")
        print("Ilość kombinacji: " + str (P))
    else:
        print("Parametr n musi być większy od parametru k\n")

def prob_test():
      n = int (input("Podaj parametr n:\n"))
      k = int (input("Podaj parametr k:\n"))
      s = (probability(n, k))
      return s

#footer
def end():
    print("Zakończono obliczenia")

#starter
def main():
    welcome()
    prob_test()
    end()
    
main()
