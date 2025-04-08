import pygame

pygame.init()

pygame.display.set_mode((500,500))

running = True

while running :
    mouse = pygame.mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT :  # fenêtre fermée
            running = False
        if event.type == pygame.KEYDOWN:  # touche pressée
            if event.key == pygame.K_ESCAPE:  # échap
                running = False

pygame.quit()