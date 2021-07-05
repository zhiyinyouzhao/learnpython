

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def calc(*numbers):
    print(numbers)
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def enroll(city):
    print(city)
    print('city:', city)


def a(**kwargs):
    enroll(**kwargs)
if __name__ == '__main__':
    # a(city='xian')
    sss = {'sss':111}

