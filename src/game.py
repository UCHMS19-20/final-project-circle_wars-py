import pygame

pygame.init()

jump_current = 1

width = 800
height = 600

character = {
    "radius_x": width/25,
    "radius_y": height/25,
    "x": (width*0.25)-(width/25),
    "y": (height*0.9)-(height/25),
    "increment": 5
}

win = pygame.display.set_mode((width,height), pygame.RESIZABLE)

while True:
    pygame.time.delay(25)
    win.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    if event.type == pygame.VIDEORESIZE:
        surface = pygame.display.set_mode((event.w, event.h),
            pygame.RESIZABLE)
        width = event.w
        height = event.h
        character = {
            "radius_x": width/25,
            "radius_y": height/25,
            "x": (width*0.25)-(width/25),
            "y": (height*0.9)-(height/25),
            "increment": 5
        }

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        character["x"] -= character["increment"]

    if keys[pygame.K_RIGHT]:
        character["x"] += character["increment"]

    if keys[pygame.K_DOWN]:
        character["y"] = (height*0.9)-(height/25)
        jump_current = 1
    
    if keys[pygame.K_UP] or jump_current > 1:
        if jump_current <= 10:
            character["y"] -= round((jump_current ** 2) * 0.5)
            jump_current += 1
        if jump_current > 10:
            character["y"] += round(((jump_current-10) ** 2) *0.5)
            jump_current += 1
        if jump_current > 20:
            jump_current = 1
    
    pygame.draw.rect(win, (0, 0, 0), [width*0.125, height*0.9, width*0.75, height*0.1])

    pygame.draw.ellipse(win, (0, 0, 255), (character["x"], character["y"], character["radius_x"], character["radius_y"]), width == 0)

    pygame.display.update()