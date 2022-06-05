# example how to use decorator

# lv 1

from functools import wraps


def car_decorator(func):
    def wrapper():
        print(f"{func.__name__} start engine. Its ready to race in:")
        func()
    return wrapper


def Audi():
    print("position 1")


def BMW():
    print("position 2")


def Porsche():
    print("position 3")


Audi = car_decorator(Audi)
BMW = car_decorator(BMW)
Porsche = car_decorator(Porsche)

Audi()
BMW()
Porsche()

# lv 2
print('\nsecond line\n')


@car_decorator
def Toyota():
    print('position 4')


@car_decorator
def Hyundai():
    print('position 5')


@car_decorator
def Kia():
    print('position 6')


Toyota()
Hyundai()
Kia()

# lv 3
print('\nthird line\n')


def car_decorator_with_points(func):
    @wraps(func)  # methood to overwrite func (built-in decorator)
    def wrapper(*args):
        print(f'{func.__name__} start engine on position:')
        return func.__name__ + " " + func(*args)
    return wrapper


@car_decorator_with_points
def Nissan(points):
    print('position 7')
    return f'{points} points from last leap'


@car_decorator_with_points
def Jaguar(points):
    print('position 8')
    return f'{points} points from last leap'


@car_decorator_with_points
def Lexus(points):
    print('position 9')
    return f'{points} points from last leap'


points = [Nissan(-1), Jaguar(2), Lexus(0)]

print(f'Bonus points: {points}')
