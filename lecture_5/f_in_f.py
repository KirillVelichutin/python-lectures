def inc_by_10(value: int) -> int:
    value += 10
    return value


def no_return(value: int) -> int | None:
    if value % 2 == 0:
        value *= 10
        if value == 20:
            return
        return value
        print('hello')


def print_to_console(init_value: int) -> None:
    print(init_value)
    init_value += 10
    print('Hello')
    print(init_value)

    

y = 13

def after_return() -> int:
    global y
    return inc_by_10(y)
    print('hello y', y)
    

    
def rec(x: int) -> int:
    print('rec x =', x)
    if x < 100:
        x += 1
        x = rec(x)
    return x



print(__name__)

if __name__ == 'f_in_f':
    print('I was imported')

if __name__ == '__main__':
    print(rec(0))
    print('hello from f_in_f')

#x = 1
# x = inc_by_10(x)
# print(x)
# print(
#     inc_by_10(10)
# )
# print(
#     no_return(10)
# )
# print(
#     after_return()
# )
#print_to_console(x)
#print(x)