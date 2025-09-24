N = int(input('Какое число вы хотите получить по его номеру в последовательности?: '))

arr = [1, 1]
i = 1

def fibonacci():
    global i
    if N <= len(arr) and N > 0:
        print(arr[N - 1])
    elif N < 1:
        print("Недопустимое значение!")
    else:
        arr.append(arr[i - 1] + arr[i])
        i += 1
        fibonacci()
        
fibonacci()