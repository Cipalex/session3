class car:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __repr__(self):
        """This is called when print of class is executed"""
        return f'Car with name {self.name} made in {self.year}'


c1 = car('Dacia', 1990)
c2 = car('Opel', 1999)
print(c1.name, c1.year)
print(c1)
print(c2)

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'{self.fname} {self.lname}'


p1 = Person('Oliver', 'Stone')
print(p1)

"""Exemplu mostenire"""
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'{self.fname} {self.lname}'


class Student(Person):
    """In paranteza scriem clasa pe care o mosteneste"""
    pass

p1 = Person('Oliver', 'Stone')
print(p1)

s = Student('Oliver', 'Stone Jr.')
print(s)

"""Generator: """
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('abc'):
    print(char)


""" Pentru a avea iterator, treuie sa ai metodele iter si next. In next trebuie sa avem Stop iteration
Codul de mai jos ruleaza la nesfarsit"""
class repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        if True:
            return self.value
        else:
            raise StopIteration


rep = repeater([1,2,3])

for item in rep:
    print(item)


"""Generator: """
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('abc'):
    print(char)