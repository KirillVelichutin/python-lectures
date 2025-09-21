# дан регион [-1000; -1000]
# пользователь загадал какое-то число
# задача программы -- замучать пользователя вопросами в виде:
# взять середину региона и спросить больше или меньше заданного числа
# и так в цикле делить регион пополам, сужая область поиска
# и так до конца пока не найдём нужное число

upper_border = int(input('Введи верхний предел: '))
lower_border = int(input('Введи нижний предел: '))

while True:
    guessed = (upper_border + lower_border) // 2
    answer = input(f'{guessed} - твоё число? [Да/Нет]: ')
    
    if answer.lower() == 'да':
        break
    
    elif answer.lower() == 'нет':
        answer = input(f'{guessed} больше или меньше загаданного тобой числа? [Больше/Меньше]: ')
        if answer.lower() == 'меньше':
            lower_border = guessed
        elif answer.lower() == 'больше':
            upper_border = guessed
        else:
            print('Сам понял, что сказал?')
            
    else:
        print('Сам понял, что сказал?')