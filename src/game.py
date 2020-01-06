import pygame

pygame.init()

width = 800
height = 600

stage_y = height/1.25
stage_x = width/8

character = {
    "diameter_x": width/25,
    "diameter_y": height/25,
    "x": (stage_x),
    "y": (stage_y)-(height/25),
    "increment": width/150,
    "y_acceleration": -height/50,
    "y_velocity": 0,
    "x_velocity": width/150,
    "jumping": 0,
    "jumps" : 2
}

win = pygame.display.set_mode((width,height), pygame.RESIZABLE)

while True:
    pygame.time.delay(25)
    win.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    if event.type == pygame.VIDEORESIZE:
        surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        character["x"] = character["x"] * event.w/width
        character["y"] = character["y"] * event.h/height
        width = event.w
        height = event.h
        character["diameter_x"] = width/25
        character["diameter_y"] = height/25
        character["y_acceleration"] = height/50
        character["x_velocity"] = width/150
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        character["y_acceleration"] -= height/50
    
    if keys[pygame.K_UP] and character["jumping"] == 0 and character["jumps"] > 0:
        character["y_velocity"] = height/2.5
        character["y_acceleration"] = -height/50
        character["jumping"] = 1
    
    if keys[pygame.K_UP] == False and character["jumping"] == 1:
        character["jumping"] = 0
        character["jumps"] -= 1

    character["y_velocity"] += character["y_acceleration"]
    
    if character["x"] > stage_x - character["diameter_x"] and character["x"] < width*0.875:
        if character["y"] - character["y_velocity"]/20 >= (stage_y)-(height/25) and character["y"] <= (stage_y)-(height/25):
            character["y"] = (stage_y)-(height/25)
            character["y_velocity"] = 0
            character["y_acceleration"] = -height/50
            character["jumps"] = 2
            character["jumping"] = 0
    else:
        if character["y"] >= height:
            character["y"] = height
            character["y_velocity"] = 0
            character["y_aceleration"] = -height/50
            character["jumps"] = 2
            character["jumping"] = 0

    character["y"] -= round(character["y_velocity"]/20)

    if keys[pygame.K_LEFT]:
        if character["x"] > stage_x - character["diameter_x"] and character["x"] < width*0.875:
            character["x"] -= character["x_velocity"]
        else:
            if character["y"] + character["diameter_y"] <= stage_y:
                character["x"] -= character["x_velocity"]
            if character["y"] + character["diameter_y"] > stage_y:
                if character["x"] - character["x_velocity"] > width*0.875:
                    character["x"] -= character["x_velocity"]
                elif character["x"] - character["diameter_x"] >= stage_x:
                    character["x"] = width*0.875
    
    if keys[pygame.K_RIGHT]:
        if character["x"] > stage_x - character["diameter_x"] and character["x"] < width*0.875:
            character["x"] += character["x_velocity"]
        else:
            if character["y"] + character["diameter_y"] <= stage_y:
                character["x"] += character["x_velocity"]
            if character["y"] + character["diameter_y"] > stage_y:
                if character["x"] + character["x_velocity"] < stage_x - character["diameter_x"]:
                    character["x"] += character["x_velocity"]
                elif character["x"] < width*0.875:
                    character["x"] = stage_x - character["diameter_x"]



    pygame.draw.rect(win, (0, 0, 0), [stage_x, stage_y, width*0.75, height/5])
    pygame.draw.ellipse(win, (0, 0, 255), (character["x"], character["y"], character["diameter_x"], character["diameter_y"]), width == 0)
    
    font = pygame.font.SysFont("Times New Roman", round(width/10))
    if character["x"] <= -character["diameter_x"] or character["x"] >= width or character["y"] <= -character["diameter_y"] or character["y"] >= height:
        text = font.render("Character died!", True, (0, 0, 0) )
        win.blit(text, ((0), (0)))
    pygame.display.update()