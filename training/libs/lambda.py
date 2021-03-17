# TODO: Programs looks like lib
from itertools import count

def pow_4(func, arg):
    return func(func(arg))

def pow_2(x):
    return x**2

def printpow():
    print(pow_4(pow_2, 10))

def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)
    print(pure_function(3, 4))
    print(pure_function(10, 4))

def polynomial(x):
    return x**2 + 5*x + 4

def lamb():
    print((lambda x: x**2 + 5*x + 4)(-4))
    print("x**1 + x**2 + x**3 + x**4 + x**5")
    g = 1
    while(g < 10):
        print((lambda g: g**1 + g**2 + g**3 + g**4 + g**5)(g))
        g += 1

def mult_two(x):
    return x*2

def filt():
    nums = list(range(10))
    result_1 = list(map(mult_two, nums))
    result_2 = list(filter(lambda x: x % 3 == 0, nums))
    print(result_1)
    print(result_2)

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

def fixedfunc(func):
    def wrap():
        print("=========")
        func()
        print("=========")
    return wrap

def other_func():
    print("other_func()")
    return pow_2(4)

func_var = fixedfunc(other_func)

@fixedfunc
def print_text():
    print("Hello world!")

def newton(x):
    if x == 1:
        return 1
    else:
        return x * newton(x-1)

def probability(n, k):
    message = "Ilość podzbiorów " + \
        str(k) + "-elementowych w zbiorze " + str(n) + "-elementowym"
    print(message)
    z = int(newton(n - k))
    n = int(newton(n))
    k = int(newton(k))
    P = int(n / (k * z))
    print(str(n) + " / " + str(k) + " * " + str(z) + "\n")
    print("Ilość kombinacji: " + str(P))

def prob_test():
    n = int(input("Podaj parametr n:\n"))
    k = int(input("Podaj parametr k:\n"))
    s = (probability(n, k))
    return s

def loop(x, y):
    for i in count(x):
        print(list(range(x, i)))
        if i == y:
            break
