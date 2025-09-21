a: list = [1, 2]
b: tuple = (3, 4)
c1: set = {'how', 'are', 'you'}
c2: set = {'fine', 'and', 'you'}
d1: dict = {'my_key': 'value1'}
d2: dict = {'my_new_key': 'value2'}



# a[0] = 11
# a[-1] = 32
# print(a)

#b[0] = 33

a.append(3)
a.append(3)
a.append(3)
# print(a)
a.pop(3)
a.pop(3)
a.pop(0)
# print(a)

g = [1, 2, 3]

# print(g + [2, 3])

print(c1 - c2)
print(c1 | c2)
print(c1.difference(c2))
print(c2.difference(c1))
print(c1.intersection(c2))