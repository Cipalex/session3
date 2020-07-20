def print_it(name):
    """Print a given parameter
    :param value - value to print
    :returns None
    """
    print(f'Hello {name}')

def add(a,b,f):
    f(a + b)


add(8, 2, print_it)


def test_pass(param):
    param += 1
    print(f'Din functie, param = {param} ')


def by_ref(param):
    param.append(100)
    print(f'Din functie, param = {param} ')


in_test = 1
test_pass(in_test)
print(f'In afara functiei in_test = {in_test}')

in_test_2 = [1, 2, 3]
by_ref(in_test_2)
print((f'In afara functiei in_test = {in_test_2}'))

def do_work(param1, param2=200):
    """Default value for param2 so that this function can be used with only param1
    We can call parameters in any order"""
    print(f'Working with {param1} and {param2}.')


do_work(100)
do_work(1, 2)
do_work(param2='ceva', param1='altceva')

def show_return1():
    pass


print(f'Function is returning {show_return1()}')

def show_return():
    return 1 , 2 , 3, 'ceva'


print(f'Function is returning {show_return()}')
"""Value Unpack is below"""
a, b, c, d = show_return()
print(f'a={a}, b={b}, c={c}, d={d}')
a, b = b, a
print(f'a={a}, b={b}, c={c}, d={d}')

""" Functii lambda"""
x = lambda a: a + 10


def y(a):
    return a + 10


print(f'Lambda {x(10)}')
print(f'Def {y(10)}')

"""Below we can say what type of object we expect, but doesn't mean we will receive that"""
def my_func(p1: int, p2: str) -> str:
    print(f'p1={p1} and p2={p2}')
    return 'second string'


my_func(1,2)