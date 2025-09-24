from rich import print as rprint

name = input('Введите ваше имя: ')

def change_name():
    res = ''
    for letter in name:
        if (name.index(letter) - 1) % 2 == 0:
            res += letter.upper()
        else:
            res += letter.lower()
            
    print(res)


def greet():
    rprint(f'Hello [bold italic underline red]{name}[/bold italic underline red]!')
    
    
change_name()
greet()