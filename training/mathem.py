# TODO: I don't understand programme destination

def foo(x):
    return x**2+2*x+10

x = 0
list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while (x <= 10):
    list[x] = foo(x)
    x += 1

print(list)
