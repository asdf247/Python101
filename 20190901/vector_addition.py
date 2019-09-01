def vector_addition(l, m):
    common_length = min(len(l), len(m))
    result = []
    for i in range(common_length):
        result.append(l[i] + m[i])

    return result

v1 = [1, 2, 3]
v2 = [3, 2, 1]

v_resultant = vector_addition(v1, v2)
print(v_resultant)

# rewrite this program
# 1. Match the length
# 2. use list comprehension for result
# 3. use map function for this operation