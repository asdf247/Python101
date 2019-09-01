def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'zde'
    except TypeError:
        return 'Invalid types'

x = divide(1, 5)
y = divide(1, 0)
z = divide('a', 5)

print(x, y, z)

