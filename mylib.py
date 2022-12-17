import pygame

pygame.init()
screen = pygame.display.set_mode([860, 600])


def any_key():
    for event in pygame.event.get():
        if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.QUIT):
            return False
    return True
    # Нажата любая клавиша


def draw_text(text, x, y, color, size):
    font = pygame.font.SysFont("Times New Roman", size)  # задаем шрифт
    tt = font.render(text, True, color)
    screen.blit(tt, [x, y])


def home_screen(zast):
    screen.blit(zast, [0, 0])  # Нужна фотография для заставки
    draw_text("Обед для Шрека", 160, 60, [0, 100, 0], 90)
    draw_text("Press any key", 410, 560, [0, 0, 0], 30)
    pygame.display.flip()
    running = True
    while running:
        running = any_key()
