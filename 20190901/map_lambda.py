l = [1, 2, 3, 4, 5]

# for i in l:
#     print(i**2)

# l_square = [i**2 for i in l]
# print(l_square)

def calc_square(x):
    return x**2

# for i in l:
#     print(calc_square(i))

# l_square = [calc_square(i) for i in l]
# print(l_square)

l_square_map = map(calc_square, l)

# Method 1
# l_square = [i for i in l_square_map]
# print(l_square)

# Method 2
# for i in l:
#  res = next(l_square_map)
#  print(res)

# Method 3
result = list(l_square_map)
print(result)