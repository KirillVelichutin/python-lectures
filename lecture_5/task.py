import time

arr = [1, 1]

def fibonacci(position):
    
    if position <= len(arr) and position > 0:
        time.sleep(2)
        print(arr[position -1])
        
    elif position < 1:
        print("Недопустимое значение!")
        
    else:
        arr.append(arr[-2] + arr[-1])
        return fibonacci(position)


if __name__ == "__main__":
    position = int(input('Какое число вы хотите получить по его номеру в последовательности?: '))
    fibonacci(position)