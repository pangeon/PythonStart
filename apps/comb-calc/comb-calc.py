def decorator(func):
    def wrap():
        print("===============================================")
        func()
        print("===============================================")
    return wrap


@decorator
def welcome():
    print("Comb-Calc v 1.0 by Kamil Cecherz")


def newton(x):
    if x == 1:
        return 1
    else:
        return x * newton(x-1)


def probability(n, k):
    if n > k:
        message = "Number of subsets " + \
            str(k) + "-elements in the set " + str(n) + "-elemental"
        print(message)
        z = int(newton(n - k))
        n = int(newton(n))
        k = int(newton(k))
        P = int(n / (k * z))
        print(str(n) + " / " + str(k) + " * " + str(z) + "\n")
        print("Number of combinations: " + str(P))
    else:
        print("The parameter n must be greater than the parameter k\n")


def prob_test():
    n = int(input("Enter the parameter n:\n"))
    k = int(input("Enter the parameter k:\n"))
    s = (probability(n, k))
    return s


def end():
    print("Calculations have been completed")


def main():
    welcome()
    prob_test()
    end()


main()
