name: str = 'Kir'

for i in range(10, 0, -2):
    print(
        f'Hello {name}! {i}'
    )
    
my_range: range = range(5, 10, 1)

print(my_range)

def my_range(start, stop, step):
    i = start
    if i > stop:
        return
    yield 1
    i += step

sentence: str = "Hello, Bob! How are you?"
splitted_sentence: list = sentence.split()

for part in splitted_sentence:
    print(part)