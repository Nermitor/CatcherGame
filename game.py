import pygame
import random


def run():
    pygame.init()
    screenX = 1200
    screenY = 800
    screen = pygame.display.set_mode([screenX, screenY])
    screen.fill([255, 255, 255])
    n_file = ["assets/img/ap.png", "assets/img/ba.png", "assets/img/ch.jpg", "assets/img/fi.jpg", "assets/img/to.jpg",
              "assets/img/me.jpg"]
    korz = pygame.image.load("assets/img/осёл.jpg")
    x = []
    y = []
    dy = []
    frukt = []
    fr_scr = []
    n = 6
    x_korz = screenX // 2 - 75
    y_korz = screenY - korz.get_height()
    popal = False
    step = 20
    sm = 0  # Счетчик пойманных фруктов
    popal = False
    for j in range(n):
        fr = pygame.image.load(n_file[j])
        fr.set_colorkey((255, 255, 255))
        frukt += [fr]
        fr_scr += [True]
        x += [random.randint(0, screenX - 32)]
        y += [0]
        dy += [random.randint(2, 10)]
    for j in range(n):
        if fr_scr[j]:
            screen.blit(frukt[j], [x[j], y[j]])
    screen.blit(korz, [x_korz, y_korz])
    font = pygame.font.Font(None, 45)  # задаем шрифт
    text = font.render("Фрукты закончились", True, [0, 255, 255])
    text1 = font.render("Поймал", True, [0, 0, 255])
    pygame.time.delay(400)  # задержка на 40 миллисекунд
    delay = 100
    interval = 10
    pygame.key.set_repeat(delay, interval)
    running = True

    while running:
        screen.fill([255, 255, 255])
        if sm > 0:
            screen.blit(text1, [10, 40])
        if sm == n:
            screen.blit(text, [300, 40])
            pygame.time.delay(400)
        screen.blit(korz, [x_korz, y_korz])
        for j in range(n):
            if fr_scr[j]:
                y[j] = y[j] + dy[j]
                screen.blit(frukt[j], [x[j], y[j]])
                if y[j] >= screenY:
                    # Появляется вверху новый рисунок
                    x[j] = random.randint(0, screenX - 32)
                    y[j] = 0
                    dy[j] = random.randint(2, 10)
                    screen.blit(frukt[j], [x[j], y[j]])
                    # Проверяем, попал ли фрукт в корзину
                if (x[j] >= x_korz) and (x[j] + 40 <= x_korz + 150) and (y[j] >= y_korz):
                    fr_scr[j] = False
                    screen.blit(korz, [x_korz, y_korz])
                    sm = sm + 1  # Подчет очков
                    text1 = font.render(" Очки " + str(sm), True, [0, 0, 255])
                    screen.blit(text1, [10, 40])
                    pygame.time.delay(40)
                    # Вывод счетчика
                    if sm == n:
                        screen.blit(text, [300, 40])
                        pygame.display.flip()
                        pygame.time.delay(4000)
                        running = False
                        break

        if running:         # Вывод Фрукты закончились
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:  # Движение ракетки
                    if event.key in (pygame.K_LEFT, pygame.K_a):  # Нажата стрелка влево
                        if x_korz >= step:
                            x_korz = x_korz - step
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):  # Нажата стрелка вправо
                        if x_korz + 150 <= screenX - step:
                            x_korz = x_korz + step

        pygame.time.delay(10)  # задержка на 10 миллисекунд
        pygame.display.flip()

