# Counter 
# Default dict
f = open('hamlet.txt')
fo = f.read()
f.close()

fo = fo.lower()
words = fo.split()

#print(words[0:10])

from collections import Counter
word_count = Counter(words)

#print(word_count)
print(type(word_count))
print(word_count.most_common(10))

cities = [('MH', 'Mumbai'), ('MH', 'Pune'), ('KA', 'Bangalore')]
cities_dict = dict(cities)
print(cities)
print(cities_dict)

from collections import defaultdict
d = defaultdict(list)
for i, j in cities:
    d[i].append(j)

print(d)