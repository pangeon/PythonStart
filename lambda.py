def pow_4(func, arg):
    return func(func(arg)) #pow_2(pow_2(10)) = pow2(100) = 100**2 = 10000

def pow_2(x):
    return x**2 # 10**2 = 100

def printpow():
    print(pow_4(pow_2, 10))

def pure_function(x, y):
    temp = x + 2*y 
    # 3 + 2*4 = 3 + 8 = 11
    # 10 + 2*4 = 16 
    return temp / (2*x + y) 
    # 2*3 + 4 = 6 + 4 = 10 | 11/10
    # 2*10 + 4 = 24 | 24/16 = 12/8 = 6/4 = 3/2
    print(pure_function(3,4)) # 1
    print(pure_function(10,4)) # 0

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
def lamb():
    print((lambda x: x**2 + 5*x + 4) (-4))

    print("x**1 + x**2 + x**3 + x**4 + x**5")
    g = 1
    while(g < 10):
        print((lambda g: g**1 + g**2 + g**3 + g**4 + g**5) (g))
        g += 1

#filter, map
def mult_two(x):
    return x*2

def filt():
    nums = list(range(10))
    result_1 = list(map(mult_two, nums))
    result_2 = list(filter(lambda x: x%3 == 0, nums))
    print(result_1) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    print(result_2) # [0, 3, 6, 9]

#generators
def jumper():
    i = 1
    while i < 10:
        yield i
        i += 1

def jumper_2(x):
    for i in range(x):
        if i % 5 == 0:
            yield i

def print_jumper():
    for i in jumper():
        print(i)

def print_jumper_2():
    print(list(jumper_2(100)))

#decorators
def fixedfunc(func):
    def wrap():
        print("=========")
        func()
        print("=========")
    return wrap # return value wrap [not function wrap() !!!]

def other_func():    
    print("other_func()")
    return pow_2(4) # jak zwrócić funkcję z przekazaną wartością ?

func_var = fixedfunc(other_func) # call to function func_var()

@fixedfunc # dekoratorem jest fixedfunc
def print_text():
  print("Hello world!")

#recursion (kombinatoryka)
def newton(x):
    if x == 1:
        return 1
    else:
        return x * newton(x-1)
    
def probability(n, k):
    
    message = "Ilość podzbiorów " + str (k) + "-elementowych w zbiorze " + str (n) + "-elementowym"
    print(message)
    z = int (newton(n - k))
    n = int (newton(n))    
    k = int (newton(k))
    P = int (n / (k * z))
    print(str (n) + " / " + str (k) + " * " + str (z) + "\n")
    print("Ilość kombinacji: " + str (P))

def prob_test():
      n = int (input("Podaj parametr n:\n"))
      k = int (input("Podaj parametr k:\n"))
      s = (probability(n, k))
      return s

#itertools
from itertools import count

def loop(x, y):
    for i in count(x):
        print(list(range(x, i)))
        if i == y:
            break
    #print(l)
         

#starter
def main():
    #printpow()
    #pure_function(5, 9)
    #polynomial(5)
    #lamb()
    #filt()
    #print_jumper()
    #print_jumper_2()
    #func_var()
    #print_text()
    #prob_test()
    loop(1, 20)
    

main()
