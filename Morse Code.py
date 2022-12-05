from ABC import abc

from random import choices
import time

random = choices(list(abc.keys()), k=5)

answers = 0
sec = 0
lak = True

print('Тренажёр передачи сигнала азбукой Морзе \nОлейников production\n')

answer = input('Готов ?\n')
if answer.upper() == 'ДА' or answer.upper() == 'Y':
    tic = time.perf_counter()
    for ran in random:
        print(f'\n{ran}')
        answer = input(': ')
        if answer == abc[ran]:
            answers += 1
            print('Правильно')
        else:
            print('Неверно!')
    toc = time.perf_counter()
    print('Итог:\n')

    if answers < 5:
        print(f'Правильных ответов - {answers}')
    else:
        print('Всё верно!')
        print(f"Вы ввели все буквы за {toc - tic:0.0f} секунд")
