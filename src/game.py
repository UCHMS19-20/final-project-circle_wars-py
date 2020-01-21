import pygame
import math
pygame.init()
pygame.mouse.set_visible(False)
screen_width = 800
screen_height = 600
win = pygame.display.set_mode((screen_width,screen_height), pygame.RESIZABLE)
class character:
    def __init__(self, x_diameter, y_diameter, x_pos, y_pos, x_vel, x_accel, y_vel, y_accel,jumping, jumps, hitbox, dead, facing_right, facing_left):
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
      self.hitbox = pygame.Rect(round(self.x_pos), round(self.y_pos), round(self.x_diameter), round(self.y_diameter))
      self.dead = False
      self.facing_right = True
      self.facing_left = False
reaper = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\reaper.png")
knight = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\knight.png")
scythe = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\scythe.png")
sword = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\sword.png")
start_screen = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\StartScreen.png")
P1 = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\P1.png")
P2 = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\P2.png")
cursor = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\cursor.png")
stage_y = screen_height/1.25
stage_x = screen_width/8
p1 = character(screen_width/10, screen_height/10, stage_x, stage_y-screen_height/10, 0, 0, 0, -screen_height/50, 0, 2, 0, False, True, False)
p2 = character(screen_width/10, screen_height/10, screen_width*0.875-screen_width/10, stage_y-screen_height/10, 0, 0, 0, -screen_height/50, 0, 2, 0, False, False, True)
p1_sprite = reaper
p2_sprite = reaper
p1_weapon = scythe
p2_weapon = scythe
p1_char = reaper
p2_char = reaper
p1_weapon_x = 1
p1_weapon_y = 1
p2_weapon_x = 1
p2_weapon_y = 1
P1_x = screen_width*0.25-screen_width/30
P1_y = screen_height*0.9
P2_x = screen_width*0.75-screen_width/30
P2_y = screen_height*0.9
cursor = pygame.transform.rotozoom(cursor, 45, 1)
game_start = False
player_1_dead = False
player_2_dead = False
player_dead = False
character_1_selected = False
character_2_selected = False
mouse_down = False
p2.facing_left = True
p2.facing_right = False
while True:
    restart = False
    while game_start == False:
        pygame.time.delay(25)
        win.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                game_start = True
            if event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                p1.x_pos = p1.x_pos * event.w/screen_width
                p1.y_pos = p1.y_pos * event.h/screen_height
                p2.x_pos = p2.x_pos * event.w/screen_width
                p2.y_pos = p2.y_pos * event.h/screen_height
                P1_x = P1_x * event.w/screen_width
                P1_y = P1_y * event.h/screen_height
                P2_x = P2_x * event.w/screen_width
                P2_y = P2_y * event.h/screen_height
                screen_width = event.w
                screen_height = event.h
                p1.x_diameter = screen_width/10
                p1.y_diameter = screen_height/10
                p1.y_accel = -screen_height/50
                p1.x_vel = screen_width/150
                p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))
                p2.x_diameter = screen_width/10
                p2.y_diameter = screen_height/10
                p2.y_accel = -screen_height/50
                p2.x_vel = screen_width/150
                p2.hitbox = pygame.Rect(round(p2.x_pos), round(p2.y_pos), round(p2.x_diameter), round(p2.y_diameter))
                stage_y = screen_height/1.25
                stage_x = screen_width/8

        win.blit(pygame.transform.scale(start_screen, (screen_width, screen_height)), (0, 0))
        pygame.display.update()
    
    while character_1_selected == False or character_2_selected == False:
        pygame.time.delay(10)
        win.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                p1.x_pos = p1.x_pos * event.w/screen_width
                p1.y_pos = p1.y_pos * event.h/screen_height
                p2.x_pos = p2.x_pos * event.w/screen_width
                p2.y_pos = p2.y_pos * event.h/screen_height
                P1_x = P1_x * event.w/screen_width
                P1_y = P1_y * event.h/screen_height
                P2_x = P2_x * event.w/screen_width
                P2_y = P2_y * event.h/screen_height
                screen_width = event.w
                screen_height = event.h
                p1.x_diameter = screen_width/10
                p1.y_diameter = screen_height/10
                p1.y_accel = -screen_height/50
                p1.x_vel = screen_width/150
                p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))
                p2.x_diameter = screen_width/10
                p2.y_diameter = screen_height/10
                p2.y_accel = -screen_height/50
                p2.x_vel = screen_width/150
                p2.hitbox = pygame.Rect(round(p2.x_pos), round(p2.y_pos), round(p2.x_diameter), round(p2.y_diameter))
                stage_y = screen_height/1.25
                stage_x = screen_width/8
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if reaper_hitbox.colliderect(P1_hitbox):
                    p1_sprite = reaper
                    p1_char = reaper
                    p1_weapon = scythe
                    p1_weapon = pygame.transform.rotozoom(p1_weapon, -45, 1)
                    p1_weapon_x = p1.x_pos + p1.x_diameter * 0.75
                    character_1_selected = True
                if reaper_hitbox.colliderect(P2_hitbox):
                    p2_sprite = reaper
                    p2_char = reaper
                    p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                    p2_weapon = scythe
                    p2_weapon = pygame.transform.rotozoom(p2_weapon, -45, 1)
                    p2_weapon = pygame.transform.flip(p2_weapon, 1, 0)
                    p2_weapon_x = p2.x_pos - p2.x_diameter * 0.25
                    character_2_selected = True
                if knight_hitbox.colliderect(P1_hitbox):
                    p1_sprite = knight
                    p1_char = knight
                    p1_weapon = sword
                    p1_weapon = pygame.transform.rotozoom(p1_weapon, -45, 1)
                    p1_weapon_y = p1.y_pos - p1.y_diameter/4
                    p1_weapon_x = p1.x_pos + p1.x_diameter * 0.9
                    character_1_selected = True
                if knight_hitbox.colliderect(P2_hitbox):
                    p2_sprite = knight
                    p2_char = knight
                    p2_weapon = sword
                    p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                    p2_weapon = pygame.transform.rotozoom(p2_weapon, -45, 1)
                    p2_weapon = pygame.transform.flip(p2_weapon, 1, 0)
                    p2_weapon_y = p2.y_pos - p2.y_diameter/4
                    p2_weapon_x = p2.x_pos - p2.x_diameter * 0.4
                    character_2_selected = True
                mouse_down = False
        if mouse_down == True:
            if P1_hitbox.colliderect(cursor_hitbox):
                P1_x = mouse_x - screen_width/30
                P1_y = mouse_y - screen_height/30
            if P2_hitbox.colliderect(cursor_hitbox):
                P2_x = mouse_x - screen_width/30
                P2_y = mouse_y - screen_height/30
        mouse_x, mouse_y = pygame.mouse.get_pos()
        P1_hitbox = pygame.Rect(round(P1_x), round(P1_y), round(screen_width/15), round(screen_height/15))
        P2_hitbox = pygame.Rect(round(P2_x), round(P2_y), round(screen_width/15), round(screen_height/15))
        reaper_hitbox = pygame.Rect(round(screen_width/10), round(screen_height/10), round(screen_width/8), round(screen_height/6))
        knight_hitbox = pygame.Rect(round(screen_width/10 + screen_width/7), round(screen_height/10), round(screen_width/8), round(screen_height/6))
        cursor_hitbox = pygame.Rect(mouse_x, mouse_y, 1, 1)
        win.blit(cursor, pygame.mouse.get_pos())
        pygame.draw.rect(win, (128, 128, 128), reaper_hitbox)
        pygame.draw.rect(win, (128, 128, 128), knight_hitbox)
        win.blit(pygame.transform.scale(reaper, (round(screen_width/8), round(screen_height/6))), (round(screen_width/10), round(screen_height/10)))
        win.blit(pygame.transform.scale(knight, (round(screen_width/8), round(screen_height/6))), (round(screen_width/10 + screen_width/7), round(screen_height/10)))
        win.blit(pygame.transform.scale(P1, (round(screen_width/15), round(screen_height/15))), (round(P1_x), round(P1_y)))
        win.blit(pygame.transform.scale(P2, (round(screen_width/15), round(screen_height/15))), (round(P2_x), round(P2_y)))
        pygame.display.update()
 
    while player_dead == False:
        pygame.time.delay(25)
        win.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                p1.x_pos = p1.x_pos * event.w/screen_width
                p1.y_pos = p1.y_pos * event.h/screen_height
                p2.x_pos = p2.x_pos * event.w/screen_width
                p2.y_pos = p2.y_pos * event.h/screen_height
                p1_weapon_x = p1_weapon_x * event.w/screen_width
                p1_weapon_y = p1_weapon_y * event.h/screen_height
                p2_weapon_x = p2_weapon_x * event.w/screen_width
                p2_weapon_y = p2_weapon_y * event.h/screen_height
                screen_width = event.w
                screen_height = event.h
                p1.x_diameter = screen_width/10
                p1.y_diameter = screen_height/10
                p1.y_accel = -screen_height/50
                p1.x_vel = screen_width/150
                p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))
                p2.x_diameter = screen_width/10
                p2.y_diameter = screen_height/10
                p2.y_accel = -screen_height/50
                p2.x_vel = screen_width/150
                p2.hitbox = pygame.Rect(round(p2.x_pos), round(p2.y_pos), round(p2.x_diameter), round(p2.y_diameter))
                stage_y = screen_height/1.25
                stage_x = screen_width/8

        stage_hitbox = pygame.draw.rect(win, (0, 0, 0), [round(stage_x), round(stage_y), round(screen_width*0.75), round(screen_height/5)])
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            p1.y_accel -= screen_height/50
        
        if keys[pygame.K_w] and p1.jumping == 0 and p1.jumps > 0:
            p1.y_vel = screen_height/2.5
            p1.y_accel = -screen_height/50
            p1.jumping = 1
        
        if keys[pygame.K_w] == False and p1.jumping == 1:
            p1.jumping = 0
            p1.jumps -= 1
        
        p1.y_vel += p1.y_accel
        p1.y_pos -= p1.y_vel/20
        p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))
        
        if p1.hitbox.colliderect(stage_hitbox):
            if p1.x_pos > stage_x - p1.x_diameter and p1.x_pos < screen_width*0.875:
                p1.y_pos = stage_y - p1.y_diameter + 1
                p1.y_vel = 0
                p1.y_accel = -screen_height/50
                p1.jumps = 2
                p1.jumping = 0
        
        if keys[pygame.K_a] and keys[pygame.K_d] == False:
            if p1.facing_right == True:
                p1_sprite = pygame.transform.flip(p1_sprite, 1, 0)
                p1_weapon = pygame.transform.flip(p1_weapon, 1, 0)
                p1.facing_right = False
                p1.facing_left = True
            if p1_char == reaper:
                p1_weapon_x = p1.x_pos - p1.x_diameter*0.25
            if p1_char == knight:
                p1_weapon_x = p1.x_pos - p1.x_diameter*0.4
            p1.x_vel = screen_width/150
            p1.x_pos -= p1.x_vel
        else:
            p1.x_vel = 0
            
        if keys[pygame.K_d] and keys[pygame.K_a] == False:
            if p1.facing_left == True:
                p1_sprite = pygame.transform.flip(p1_sprite, 1, 0)
                p1_weapon = pygame.transform.flip(p1_weapon, 1, 0)
                p1.facing_left = False
                p1.facing_right = True
            if p1_char == reaper:
                p1_weapon_x = p1.x_pos + p1.x_diameter*0.75
            if p1_char == knight:
                p1_weapon_x = p1.x_pos + p1.x_diameter*0.9
            p1.x_vel = screen_width/150
            p1.x_pos += p1.x_vel
        else:
            p1.x_vel = 0
        
        p1.y_pos -= 2
        p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))
        
        if p1.hitbox.colliderect(stage_hitbox):
            if keys[pygame.K_a]:
                if p1.y_pos > (stage_y)-(screen_height/10):
                    p1.x_pos = screen_width*0.875
            elif keys[pygame.K_d]:
                if p1.y_pos > (stage_y)-(screen_height/10):
                    p1.x_pos = stage_x - p1.x_diameter
        p1.y_pos += 2
        p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))

        if keys[pygame.K_DOWN]:
            p2.y_accel -= screen_height/50
        
        if keys[pygame.K_UP] and p2.jumping == 0 and p2.jumps > 0:
            p2.y_vel = screen_height/2.5
            p2.y_accel = -screen_height/50
            p2.jumping = 1
        
        if keys[pygame.K_UP] == False and p2.jumping == 1:
            p2.jumping = 0
            p2.jumps -= 1
        
        p2.y_vel += p2.y_accel
        p2.y_pos -= p2.y_vel/20
        p2.hitbox = pygame.Rect(round(p2.x_pos), round(p2.y_pos), round(p2.x_diameter), round(p2.y_diameter))
        
        if p2.hitbox.colliderect(stage_hitbox):
            if p2.x_pos > stage_x - p2.x_diameter and p2.x_pos < screen_width*0.875:
                p2.y_pos = stage_y - p2.y_diameter + 1
                p2.y_vel = 0
                p2.y_accel = -screen_height/50
                p2.jumps = 2
                p2.jumping = 0
        
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] == False:
            if p2.facing_right == True:
                p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                p2_weapon = pygame.transform.flip(p2_weapon, 1, 0)
                p2.facing_right = False
                p2.facing_left = True
            if p2_char == knight:
                p2_weapon_x = p2.x_pos - p2.x_diameter*0.4
            if p2_char == reaper:
                p2_weapon_x = p2.x_pos - p2.x_diameter*0.25
            p2.x_vel = screen_width/150
            p2.x_pos -= p2.x_vel
        else:
            p2.x_vel = 0
            
        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] == False:
            if p2.facing_left == True:
                p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                p2_weapon = pygame.transform.flip(p2_weapon, 1, 0)
                p2.facing_left = False
                p2.facing_right = True
            if p2_char == knight:
                p2_weapon_x = p2.x_pos + p2.x_diameter*0.9
            if p2_char == reaper:
                p2_weapon_x = p2.x_pos + p2.x_diameter*0.75
            p2.x_vel = screen_width/150
            p2.x_pos += p2.x_vel
        else:
            p2.x_vel = 0
        
        p2.y_pos -= 2
        p2.hitbox = pygame.Rect(round(p2.x_pos), round(p2.y_pos), round(p2.x_diameter), round(p2.y_diameter))
        
        if p2.hitbox.colliderect(stage_hitbox):
            if keys[pygame.K_LEFT]:
                if p2.y_pos > (stage_y)-(screen_height/10):
                    p2.x_pos = screen_width*0.875
            elif keys[pygame.K_RIGHT]:
                if p2.y_pos > (stage_y)-(screen_height/10):
                    p2.x_pos = stage_x - p1.x_diameter
        p2.y_pos += 2
        p2.hitbox = pygame.Rect(round(p2.x_pos), round(p2.y_pos), round(p2.x_diameter), round(p2.y_diameter))

        if p1_char == reaper:
            p1_weapon_y = p1.y_pos
        if p2_char == reaper:
            p2_weapon_y = p2.y_pos
        if p1_char == knight:
            p1_weapon_y = p1.y_pos - p1.y_diameter/4
        if p2_char == knight:
            p2_weapon_y = p2.y_pos - p2.y_diameter/4

        pygame.draw.rect(win, (255, 0, 0), p1.hitbox)
        pygame.draw.rect(win, (255, 0, 0), p2.hitbox)
        pygame.draw.rect(win, (0, 0, 0), [round(stage_x), round(stage_y), round(screen_width*0.75), round(screen_height/5)])
        win.blit(pygame.transform.scale(p1_sprite, (round(p1.x_diameter), round(p1.y_diameter))), (round(p1.x_pos), round(p1.y_pos)))
        win.blit(pygame.transform.scale(p1_weapon, (round(p1.x_diameter/2), round(p1.y_diameter))), (round(p1_weapon_x), round(p1_weapon_y)))
        win.blit(pygame.transform.scale(p2_sprite, (round(p2.x_diameter), round(p2.y_diameter))), (round(p2.x_pos), round(p2.y_pos)))
        win.blit(pygame.transform.scale(p2_weapon, (round(p2.x_diameter/2), round(p2.y_diameter))), (round(p2_weapon_x), round(p2_weapon_y)))
        
        if p1.x_pos <= -p1.x_diameter or p1.x_pos >= screen_width or p1.y_pos <= -p1.y_diameter or p1.y_pos >= screen_height:
            player_1_dead = True
            player_dead = True
            p1.dead = True
        if p2.x_pos <= -p2.x_diameter or p2.x_pos >= screen_width or p2.y_pos <= -p2.y_diameter or p2.y_pos >= screen_height:
            player_2_dead = True
            player_dead = True
            p2.dead = True
        pygame.display.update()
 
    while restart == False:
        pygame.time.delay(25)
        win.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                p1.x_pos = p1.x_pos * event.w/screen_width
                p1.y_pos = p1.y_pos * event.h/screen_height
                p2.x_pos = p2.x_pos * event.w/screen_width
                p2.y_pos = p2.y_pos * event.h/screen_height
                P1_x = P1_x * event.w/screen_width
                P1_y = P1_y * event.h/screen_height
                P2_x = P2_x * event.w/screen_width
                P2_y = P2_y * event.h/screen_height
                screen_width = event.w
                screen_height = event.h
                p1.x_diameter = screen_width/10
                p1.y_diameter = screen_height/10
                p1.y_accel = -screen_height/50
                p1.x_vel = screen_width/150
                p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))
                p2.x_diameter = screen_width/10
                p2.y_diameter = screen_height/10
                p2.y_accel = -screen_height/50
                p2.x_vel = screen_width/150
                p2.hitbox = pygame.Rect(round(p2.x_pos), round(p2.y_pos), round(p2.x_diameter), round(p2.y_diameter))
                stage_y = screen_height/1.25
                stage_x = screen_width/8

        font = pygame.font.SysFont("Times New Roman", round(screen_width/10))
        if player_1_dead == True:
            text = font.render("Player 2 wins!", True, (0, 0, 0) )
        if player_2_dead == True:
            text = font.render("Player 1 wins!", True, (0, 0, 0) )
        win.blit(text, ((0), (0)))
        win.blit(font.render("Press r to restart", True, (0, 0, 0) ), ((0), (round(screen_width/10))))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            stage_y = screen_height/1.25
            stage_x = screen_width/8
            if p1.facing_left == True:
                p1_sprite = pygame.transform.flip(p1_sprite, 1, 0)
                p1_weapon = pygame.transform.flip(p1_weapon, 1, 0)
                p1.facing_left = False
                p1.facing_right = True
            if p2.facing_right == True:
                p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                p2_weapon = pygame.transform.flip(p2_weapon, 1, 0)
            p1 = character(screen_width/10, screen_height/10, stage_x, stage_y-screen_height/10, 0, 0, 0, -screen_height/50, 0, 2, 0, False, True, False)
            p2 = character(screen_width/10, screen_height/10, screen_width*0.875-screen_width/10, stage_y-screen_height/10, 0, 0, 0, -screen_height/50, 0, 2, 0, False, False, True)
            P1_x = screen_width*0.25-screen_width/30
            P1_y = screen_height*0.9
            P2_x = screen_width*0.75-screen_width/30
            P2_y = screen_height*0.9
            restart = True
            game_start = False
            player_1_dead = False
            player_2_dead = False
            player_dead = False
            character_1_selected = False
            character_2_selected = False
            mouse_down = False
            p2.facing_left = True
            p2.facing_right = False
        pygame.display.update()