import pygame

pygame.init()

jump_current = 1

width = 800
height = 600

character = {
    "diameter_x": width/25,
    "diameter_y": height/25,
    "x": (width*0.125),
    "y": (height*0.9)-(height/25),
    "increment": width/150
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
        character["x"] = character["x"] * event.w/width
        character["y"] = character["y"] * event.h/height
        width = event.w
        height = event.h
        character["diameter_x"] = width/25
        character["diameter_y"] = height/25
        character["increment"] = width/150

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        character["x"] -= character["increment"]

    if keys[pygame.K_RIGHT]:
        character["x"] += character["increment"]

    if keys[pygame.K_DOWN]:
        if character["x"] > width*0.125 - character["diameter_x"] and character["x"] < width*0.875:
            character["y"] = (height*0.9)-(height/25)
            jump_current = 1
        else:
            character["y"] = height
    
    if keys[pygame.K_UP] or jump_current > 1:
        if jump_current <= 25:
            character["y"] -= round(height/1000*jump_current ** 2 * 0.05)
            jump_current += 1
        if jump_current > 25:
            character["y"] += round(height/1000*(jump_current-25) ** 2 * 0.05)
            jump_current += 1
        if jump_current > 50:
            jump_current = 1
    
    pygame.draw.rect(win, (0, 0, 0), [width*0.125, height*0.9, width*0.75, height*0.1])

    pygame.draw.ellipse(win, (0, 0, 255), (character["x"], character["y"], character["diameter_x"], character["diameter_y"]), width == 0)
    font = pygame.font.SysFont("Times New Roman", round(width/10))
    if character["x"] <= -character["diameter_x"] or character["x"] >= width or character["y"] <= -character["diameter_y"] or character["y"] >= height:
        text = font.render("Character died!", True, (0, 0, 0) )
        win.blit(text, ((0), (0)))
    print(character["x"])
    pygame.display.update()