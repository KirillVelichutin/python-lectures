from rich import print as rprint

def change_name(name):
    new_name = ''
    
    for letter in name:
        index = name.index(letter)
        
        if (index - 1) % 2 == 0:
            new_name += letter.upper()
        else:
            new_name += letter.lower()
            
    return new_name
    
def greet(name):
    rprint(f"Hello [bold green]{name}[/bold green]!")