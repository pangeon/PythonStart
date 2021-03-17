class Girl:
    def __init__(self, hair, age):
        self.hair = hair
        self.age = age
    
    def toString(self):
        return str("---hair: " + self.hair + "\n---age: " + str(self.age))

class Woman(Girl):
    def info(self):
        print("Woman... So, an older girl")
   
ann = Girl("ginger", 23)
sue = Girl("blonde", 19)
megan = Girl("black", 22)

print("Ann:\n" + ann.toString())
print("Sue:\n" + sue.toString())
print("Megan:\n" + megan.toString())

print()
alice = Woman("brown", 37)
alice.info()
print("Alice:\n" + alice.toString())

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __pow__(self, other):
        return Vector2D(self.x ** other.x, self.y ** other.y)

first = Vector2D(8, 7)
second = Vector2D(2, 3)
result = first ** second
print(str(result.x) + " " + str(result.y))

class StrConc:
    def __init__(self, string):
        self.string = string
    def __truediv__(self, other):
        line = "=" * len(other.string)
        return "\n".join([self.string, line, other.string])
    def __ne__(self, other):
        for index in range(len(other.string)+1):
            result = other.string[:index] + ">" + self.string
            result += ">" + other.string[index:]
            print(result)
            

name = StrConc("Kamil")
welcome = StrConc("Hello in Python Uniwerse")
print(name / welcome)
print(name != welcome)


    





