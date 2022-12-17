import mylib
import pygame


def help():
    X = 730  # Размеры окна для помощи
    Y = 300
    screen1 = pygame.display.set_mode([X, Y])
    pygame.display.set_caption("Помощь")
    screen1.fill([154, 205, 50])
    ft = open('Помощь.txt', 'r')
    lines = ft.readlines()
    ft.close()
    y = 40
    x = 30
    for i in range(len(lines)):
        ln = lines[i]  # i-я строка
        dl = len(ln) - 1  # Уменьшаем число символов строки на единицу
        ln = ln[0:dl]  # Удаляем символ конца строки,
        # то есть в ln пишем все символы из lines[i] кроме последнего
        mylib.draw_text(ln, x, y, [0, 128, 0], 30)
        y = y + 30
    pygame.display.flip()
    running = True
    while running:
        running = mylib.any_key()
