import pygame
from PIL import Image

pygame.init()
image = pygame.image.load('data/fon.jpg')
new_image = pygame.transform.scale(image, (1400, 890))

screen = pygame.display.set_mode((1400, 890))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(new_image, (0, 0))

    pygame.display.flip()

pygame.quit()
