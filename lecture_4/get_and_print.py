a: Ellipsis = ...
b: complex = complex(real=3, imag=-2)
c: list = [a, b, 3, 4, a, b, 3, 4, a, b, 3, 4]
d: tuple = (b, 2, 3, 4)
e: set = {'bob', 'hello', 'how', 'are', 'you','bob'}
f: dict = {1: '11', 2: '22', 3: '33', 4: '44', 'bob': 'durak'}

print(
    c[2], c[0]
)

print(
    c[1:3],
    c[1:46],
    c[1:],
    c[:],
    sep='\n'
)

print('-' * 15)
print(
    c[0:46],
    c[::2],
    c[::-1],
    sep='\n'
)

print(e)
print(
    set(c)
)

print('-' * 15)
print(
    f[1], f['bob']
)

print(f.keys())
print(f.values())

print(
    tuple(f.keys())
)

print(
    list(f.values())
)