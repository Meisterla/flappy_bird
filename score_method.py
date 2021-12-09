import pygame
import os

W = 800
H = 600

SCREEN = pygame.display.set_mode((W, H))
CLOCK = pygame.time.Clock()

IMAGES = {}
for image in os.listdir('assets/sprites'):
    name, extension = os.path.splitext(image)
    path = os.path.join('assets/sprites', image)
    IMAGES[name] = pygame.image.load(path)


area1 = pygame.Surface(size=(800, 300))
area2 = pygame.Surface(size=(800, 300))
area1.fill((155, 0, 0))
area2.fill((0, 0, 155))
SCREEN.blit(area1, (0, 0))
SCREEN.blit(area2, (0, 300))


def show_score(score, rate=1, size=(0, 0)):
    number_screen = pygame.image.load('assets/sprites/Empty.png')
    score_str = str(score)
    n = len(score_str)
    w = IMAGES['0'].get_width()
    h = IMAGES['0'].get_height()
    if size is not (0, 0):
        rate_w = size[0]/w
        rate_h = size[1]/h
    else:
        rate_w = rate
        rate_h = rate
    x = (number_screen.get_width() - n * w + w * 0.5) * 0.5
    y = (number_screen.get_height() - h * 0.5) * 0.5
    for number in score_str:
        image_number = IMAGES[number]
        image_number = pygame.transform.scale(image_number,
                                              (image_number.get_width() * rate_w, image_number.get_height() * rate_h))
        number_screen.blit(image_number, (x, y))
        x += w * rate_w
    return number_screen


def show_bar(num, num_max, size=(0, 0)):
    surface_base_bar = pygame.image.load('assets/sprites/Empty.png')
    w = size[0]
    h = size[1]
    w2 = w * num / num_max
    surface_current_bar = pygame.Surface(size=(w2, h))
    surface_current_bar.fill((255, 0, 0))
    surface_base_bar.blit(surface_current_bar, (0, 0))
    return surface_base_bar


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        else:
            SCREEN.blit(show_score(2323, rate=0.6), (300, 200))
            SCREEN.blit(show_bar(num=90, num_max=100, size=(200, 20)), (200, 500))
        pygame.display.update()
    CLOCK.tick(30)
