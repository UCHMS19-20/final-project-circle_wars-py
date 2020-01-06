import pygame
 
pygame.init()
 
screen_width = 800
screen_height = 600

stage_y = screen_height/1.25
stage_x = screen_width/8

class character:
  def __init__(self, x_diameter, y_diameter, x_pos, y_pos, x_vel, x_accel, y_vel, y_accel,jumping, jumps):
    self.x_diameter = x_diameter
    self.y_diameter = y_diameter
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.x_vel = x_vel
    self.x_accel = x_accel
    self.y_vel = y_vel
    self.y_accel = y_accel
    self.jumping = jumping
    self.jumps = jumps

p1 = character(screen_width/10, screen_width/10, screen_width/8, screen_height/1.25-screen_height/10, screen_width/150, 0, 0, -screen_height/50, 0, 2)
 
win = pygame.display.set_mode((screen_width,screen_height), pygame.RESIZABLE)
p1_sprite = pygame.image.load(r"C:\Users\kcheng\Documents\GitHub\final-project-circle_wars-py\src\img\reaper.png")
while True:
    pygame.time.delay(25)
    win.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    if event.type == pygame.VIDEORESIZE:
        surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        p1.x_pos = p1.x_pos * event.w/screen_width
        p1.y_pos = p1.y_pos * event.h/screen_height
        screen_width = event.w
        screen_height = event.h
        p1.x_diameter = screen_width/10
        p1.y_diameter = screen_height/10
        p1.y_accel = screen_height/50
        p1.x_vel = screen_width/150

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        p1.y_accel -= screen_height/50
    
    if keys[pygame.K_UP] and p1.jumping == 0 and p1.jumps > 0:
        p1.y_vel = screen_height/2.5
        p1.y_accel = -screen_height/50
        p1.jumping = 1
    
    if keys[pygame.K_UP] == False and p1.jumping == 1:
        p1.jumping = 0
        p1.jumps -= 1

    p1.y_vel += p1.y_accel
    
    if p1.x_pos > stage_x - p1.x_diameter and p1.x_pos < screen_width*0.875:
        if p1.y_pos - p1.y_vel/20 >= (stage_y)-(screen_height/10) and p1.y_pos <= (stage_y)-(screen_height/10):
            p1.y_pos = (stage_y)-(screen_height/10)
            p1.y_vel = 0
            p1.y_accel = -screen_height/50
            p1.jumps = 2
            p1.jumping = 0
    else:
        if p1.y_pos >= screen_height:
            p1.y_pos = screen_height
            p1.y_vel = 0
            p1.y_accel = -screen_height/50
            p1.jumps = 2
            p1.jumping = 0

    p1.y_pos -= round(p1.y_vel/20)
    
    if keys[pygame.K_LEFT]:
        p1.x_pos -= p1.x_vel
        
    if keys[pygame.K_RIGHT]:
        p1.x_pos += p1.x_vel
    print(p1.y_vel)
    print(p1.y_accel)

    pygame.draw.rect(win, (0, 0, 0), [stage_x, stage_y, screen_width*0.75, screen_height/5])
    win.blit(pygame.transform.scale(p1_sprite, (round(p1.x_diameter), round(p1.y_diameter))), (p1.x_pos, p1.y_pos))
    pygame.display.update()