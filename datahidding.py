class Queue:
    def __init__(self, contents):
        self.__secret = list(contents)
    def push(self, value):
        self.__secret.insert(0, value)
    def pop(self):
        return self.__secret.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self.__secret)

q = Queue([1, 8, 9, 44])
print(q)

q.push(0)
print(q)
q.pop()
print(q)

print(q.__secret) #AttributeError: 'Queue' object has no attribute '__secret'



class Secret:
  __hidden = 7
  no_hidden = 0
  def print_hidden(self):
    print(self.__hidden)

s = Secret()
s.print_hidden()
print(s._Secret__hidden)
print(s.no_hidden)
print(s.__hidden) #AttributeError: 'Secret' object has no attribute '__hidden'

