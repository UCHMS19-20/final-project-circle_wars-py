import pygame

pygame.init()

jump_current = 1

display = {
    "width": 800,
    "height": 600
}

character = {
    "radius": 25,
    "x": 400,
    "y": 525,
    "increment": 5
}

win = pygame.display.set_mode((display["width"], display["height"]))

while True:
    pygame.time.delay(50)
    win.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        character["x"] -= character["increment"]

    if keys[pygame.K_RIGHT]:
        character["x"] += character["increment"]

    if keys[pygame.K_DOWN]:
        character["y"] = 525
        jump_current = 1
    
    if keys[pygame.K_UP] or jump_current > 1:
        if jump_current <= 10:
            character["y"] -= (jump_current ** 2)
            jump_current += 1
        if jump_current > 10:
            character["y"] += ((jump_current-10) ** 2)
            jump_current += 1
        if jump_current > 20:
            jump_current = 1
    
    pygame.draw.rect(win, (0, 0, 0), [100, 550, 600, 50])

    pygame.draw.circle(win, (0, 0, 255), (character["x"], character["y"]), character["radius"])

    pygame.display.update()
