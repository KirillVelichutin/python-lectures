from rich import print as rich_print

rich_print('[bold blue] Привет, дорогой мой друг из Москвы!')
rich_print('Сегодня у нас будет показ фильма [bold red]Дедпул[/bold red]!')
decision: str = input('Пойдёшь со мной? [Да/Нет]: ')

if decision.lower() == 'да':
    age: str = input('Слушай, а сколько тебе лет?: ')
    if age >= 18:
        rich_print('[bold blue]Супер! Пошли с нами!')
    elif age <= 0:
        rich_print('[bold red]Господи...')
    else:
        rich_print('Сорри, малыш, тебе надо подрасти')

elif decision.lower() == 'нет':
    rich_print('[bold yellow]Слава богу, без тебя нам лучше будет!')
else:
    rich_print('[bold red]Кот, блин, уйди с клавы')