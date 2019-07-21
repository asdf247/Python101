l = [2, 4, 5, 6, 7, 8]
l_squares = []
for i in l:
    l_squares.append(i * i)

print(l_squares)

l_squares_2 = [i**2 for i in l]
print(l_squares_2)

def square(num):
    return num * num

l_squared = map(square, l)
print(l_squared)
print(list(l_squared))

t1 = [3, 5, 6]
t2 = [5, 6, 9]
t3 = [1, 4, 6]

8, 11, 15
print(t1 + t2)

def add_x_y(x, y, z):
    return x+y+z

print(add_x_y(4, 5))

vect_addn = map(add_x_y, t1, t2, t3)
print(list(vect_addn))

# Lambda
l = [3, 4, 5, 6]
m = [3, 5, 4, 6]
def square(num):
    return num * num

l_squared = map(lambda x: x*x, l)
print(list(l_squared))

l_m = map(lambda x, y: x+y, l, m)
print(list(l_m))

# Filter

l = [1, 3, 4, 7, 2]
l_odd = []
for i in l:
    if i % 2 != 0:
        l_odd.append(i)

print(l_odd)

def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

print(is_odd(5))
print(is_odd(6))
print(l)
l_odd = filter(is_odd, l)
print(list(l_odd))