import time

arr = [1, 1]

MY_CACHE: dict[str, str] = {}

def fibonacci(position):
    if position in MY_CACHE:
        return MY_CACHE[position]
    
    elif position <= len(arr) and position > 0:
        time.sleep(2)
        print(arr[position -1])
        
    elif position < 1:
        print("Недопустимое значение!")
        
    else:
        arr.append(arr[-2] + arr[-1])
        return fibonacci(position)
    
    MY_CACHE[position] = arr[position - 1]


if __name__ == "__main__":
    print('Какое число вы хотите получить по его номеру в последовательности?: ')
    position = int(input())
    
    fibonacci(position)
    
    print(f"{MY_CACHE=}")