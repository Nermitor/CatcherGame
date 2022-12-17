import game
import myhelp
from myhelp import *


def refresh_screen(space):
    screenX = 760
    screenY = 500
    screen = pygame.display.set_mode([screenX, screenY])
    screen.blit(space, [0, 0])
    pygame.display.flip()

def main():
    pygame.init()
    pygame.font.init()
    space = pygame.image.load("assets/img/заставка.jpg")
    mylib.home_screen(space)  # Функция заставки находится в файле mylib.
    pygame.display.set_caption("Меню")
    top = [100, 200, 300]
    left = 200
    width = 320
    height = 90
    menu_labels = ["Помощь", "Игра", "Выход"]
    n_str = 3  # Три строки в меню

    screen = pygame.display.set_mode([0, 0])

    refresh_screen(space)

    running = True
    while running:
        pygame.display.set_caption("Меню")
        mylib.draw_text("Меню", 290, 10, [34, 139, 34], 60)
        for i in range(n_str):  # рисуем пункты меню
            pygame.draw.rect(screen, [154, 205, 50], [left, top[i], width, height], 0)
            x = left + 40
            y = top[i] + 20  # Расстояние между прямоугольниками 20
            mylib.draw_text(menu_labels[i], x, y, [0, 128, 0], 60)
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x1, y1) = pygame.mouse.get_pos()  # координаты курсора мыши
                for i in range(n_str):
                    if left < x1 < left + width and top[i] < y1 < top[i] + height:
                        break  # Выход из цикла. Уже выбран раздел 1 (Игра)
                if i == 2:
                    running = False  # выход
                if i == 0:
                    myhelp.help()  # Импорт myhelp стоит в первой строке файла
                    # Помощь выводится в окно другого размера, поэтому восстанавливаем окно для меню
                    refresh_screen(space)
                if i == 1:
                    game.run()  # игра
                    # Игра выводится в окно другого размера, поэтому после возврата в меню восстанавливаем окно для меню
                    refresh_screen(space)
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.quit()


if __name__ == '__main__':
    main()
