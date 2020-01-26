import pygame
import math
pygame.init()
#Makes mouse invisible so that it can be replaced with a cursor sprite
pygame.mouse.set_visible(False)
#defines initial screen dimentions and makes it resizable
screen_width = 800
screen_height = 600
win = pygame.display.set_mode((screen_width,screen_height), pygame.RESIZABLE)
#creates a class called character that will be used to make objects p1 and p2
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
#load images
reaper = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\reaper.png")
knight = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\knight.png")
sword = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\sword.png")
start_screen = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\StartScreen.png")
P1 = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\P1.png")
P2 = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\P2.png")
cursor = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\cursor.png")
scythe = pygame.image.load(r"C:\Users\21kch\OneDrive\Documents\GitHub\final-project-circle_wars-py\src\img\scythe2.png")
#sets initial positions of stage, character, player icons, etc.
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
p1_attack_frame = 0
p2_attack_frame = 0
P1_x = screen_width*0.25-screen_width/30
P1_y = screen_height*0.9
P2_x = screen_width*0.75-screen_width/30
P2_y = screen_height*0.9
cursor = pygame.transform.rotozoom(cursor, 45, 1)
#define variables to be given values later
p1_attacking = False
p2_attacking = False
game_start = False
player_1_dead = False
player_2_dead = False
player_dead = False
character_1_selected = False
character_2_selected = False
mouse_down = False
p2.facing_left = True
p2.facing_right = False
p2_damage = 0
p2_hitstun = 0
p1_damage = 0
p1_hitstun = 0
p1_was_right = False
p1_was_left = False
p2_was_right = False
p2_was_left = False
while True:
    #sets restart back to false so you can restart more than once
    restart = False
    #occurs until you press a key
    while game_start == False:
        #fps
        pygame.time.delay(25)
        #refills window to prevent image being drawn over itself
        win.fill((255, 255, 255))
        #exit button, video resize, and checks if key pressed
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
    #occurs until both players selected a character
    while character_1_selected == False or character_2_selected == False:
        pygame.time.delay(5)
        win.fill((255, 255, 255))
        #gets position of mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #defines hitboxes for all sprites
        P1_hitbox = pygame.Rect(round(P1_x), round(P1_y), round(screen_width/15), round(screen_height/15))
        P2_hitbox = pygame.Rect(round(P2_x), round(P2_y), round(screen_width/15), round(screen_height/15))
        reaper_hitbox = pygame.Rect(round(screen_width/10), round(screen_height/10), round(screen_width/8), round(screen_height/6))
        knight_hitbox = pygame.Rect(round(screen_width/10 + screen_width/7), round(screen_height/10), round(screen_width/8), round(screen_height/6))
        cursor_hitbox = pygame.Rect(mouse_x, mouse_y, 1, 1)
        #exit button and window resize
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
            #since event is only checked for one frame when you click, a variable is made for if the mouse is held down instead
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                #sets position depending on character selected
                if reaper_hitbox.colliderect(P1_hitbox):
                    p1_sprite = reaper
                    p1_char = reaper
                    p1_weapon = scythe
                    p1_weapon_rotate = p1_weapon
                    p1_weapon_x = p1.x_pos - p2.x_diameter*0.25
                    character_1_selected = True
                if reaper_hitbox.colliderect(P2_hitbox):
                    p2_sprite = reaper
                    p2_char = reaper
                    p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                    p2_weapon = scythe
                    p2_weapon_rotate = p2_weapon
                    p2_weapon_rotate = pygame.transform.flip(p2_weapon_rotate, 1, 0)
                    p2_weapon_x = p2.x_pos + p2.x_diameter*0.25
                    character_2_selected = True
                if knight_hitbox.colliderect(P1_hitbox):
                    p1_sprite = knight
                    p1_char = knight
                    p1_weapon = sword
                    p1_weapon_rotate = pygame.transform.rotozoom(p1_weapon, -45, 1)
                    p1_weapon_x = p1.x_pos + p1.x_diameter * 0.9
                    character_1_selected = True
                if knight_hitbox.colliderect(P2_hitbox):
                    p2_sprite = knight
                    p2_char = knight
                    p2_weapon = sword
                    p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                    p2_weapon_rotate = pygame.transform.rotozoom(p2_weapon, -45, 1)
                    p2_weapon_rotate = pygame.transform.flip(p2_weapon_rotate, 1, 0)
                    p2_weapon_x = p2.x_pos - p2.x_diameter * 0.4
                    character_2_selected = True
                #checks for if a character has been selected
                if reaper_hitbox.colliderect(P1_hitbox) == False and knight_hitbox.colliderect(P1_hitbox) == False:
                    character_1_selected = False
                if reaper_hitbox.colliderect(P2_hitbox) == False and knight_hitbox.colliderect(P2_hitbox) == False:
                    character_2_selected = False
                #says you are no longer holding down the mouse
                mouse_down = False
        if mouse_down == True:
            #while mouse is held down, if cursor is collided with player icon, move player icon to mouse position
            if P1_hitbox.colliderect(cursor_hitbox):
                P1_x = mouse_x - screen_width/30
                P1_y = mouse_y - screen_height/30
            if P2_hitbox.colliderect(cursor_hitbox):
                P2_x = mouse_x - screen_width/30
                P2_y = mouse_y - screen_height/30
        #draws all sprites to screen
        win.blit(cursor, pygame.mouse.get_pos())
        pygame.draw.rect(win, (128, 128, 128), reaper_hitbox)
        pygame.draw.rect(win, (128, 128, 128), knight_hitbox)
        win.blit(pygame.transform.scale(reaper, (round(screen_width/8), round(screen_height/6))), (round(screen_width/10), round(screen_height/10)))
        win.blit(pygame.transform.scale(knight, (round(screen_width/8), round(screen_height/6))), (round(screen_width/10 + screen_width/7), round(screen_height/10)))
        win.blit(pygame.transform.scale(P1, (round(screen_width/15), round(screen_height/15))), (round(P1_x), round(P1_y)))
        win.blit(pygame.transform.scale(P2, (round(screen_width/15), round(screen_height/15))), (round(P2_x), round(P2_y)))
        pygame.display.update()
    #occurs until a player is knocked offscreen
    while player_dead == False:
        pygame.time.delay(25)
        win.fill((255, 255, 255))
        #exit button and resize
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
        #creates hitbox for stage
        stage_hitbox = pygame.draw.rect(win, (0, 0, 0), [round(stage_x), round(stage_y), round(screen_width*0.75), round(screen_height/5)])
        #creates weapon size based on character chosen
        if p1_char == reaper:
            p1_weapon_diameter_x = p1.x_diameter
            p1_weapon_diameter_y = p1.y_diameter
        if p2_char == reaper:
            p2_weapon_diameter_x = p2.x_diameter
            p2_weapon_diameter_y = p2.y_diameter
        if p1_char == knight:
            p1_weapon_diameter_x = p1.x_diameter/2
            p1_weapon_diameter_y = p1.y_diameter
        if p2_char == knight:
            p2_weapon_diameter_x = p2.x_diameter/2
            p2_weapon_diameter_y = p2.y_diameter

        keys = pygame.key.get_pressed()
        #if you are not in the middle of an attack, makes you attack
        if keys[pygame.K_f] and p1_attacking == False and p1_hitstun == 0:
            p1_attacking = True
        if p1_attacking == True:
            p1_attack_frame += 1
        #rotates and moves weapon based for an attack animation
        if p1_char == reaper:
            if p1.facing_right == True:
                #move startup animation
                if p1_attack_frame > 0 and p1_attack_frame < 5:
                    p1_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p1_weapon, -90), 0, 1)
                    p1_weapon_x = p1.x_pos + 0.75*p1.x_diameter
                #move attack animation
                if p1_attack_frame >= 5 and p1_attack_frame < 15:
                    p1_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p1_weapon, -90 + -15*(p1_attack_frame-4)), 0, 1)
                    p1_weapon_x = p1.x_pos + 0.75*p1.x_diameter
                if p1_attack_frame >= 15 and p1_attack_frame < 25:
                    p1_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p1_weapon, -90 + -100 + 15*(p1_attack_frame-14)), 0, 1)
                    p1_weapon_x = p1.x_pos + 0.75*p1.x_diameter
                #move end(recovery) animation
                if p1_attack_frame == 25:
                    p1_attacking = False
                    p1_attack_frame = 0
                    p1_weapon_rotate = p1_weapon
                    p1_weapon_x = p1.x_pos - p1.x_diameter*0.25
            #same attack, but for when facing left
            if p1.facing_left == True:
                if p1_attack_frame > 0 and p1_attack_frame < 5:
                    p1_weapon_rotate = pygame.transform.rotate(p1_weapon, 90)
                    p1_weapon_x = p1.x_pos - 0.75*p1.x_diameter
                if p1_attack_frame >= 5 and p1_attack_frame < 15:
                    p1_weapon_rotate = pygame.transform.rotate(p1_weapon, 90 + -15*(p1_attack_frame-4))
                    p1_weapon_x = p1.x_pos - 0.75*p1.x_diameter
                if p1_attack_frame >= 15 and p1_attack_frame < 25:
                    p1_weapon_rotate = pygame.transform.rotate(p1_weapon, 90 + -100 + 15*(p1_attack_frame-14))
                    p1_weapon_x = p1.x_pos - 0.75*p1.x_diameter
                if p1_attack_frame == 25:
                    p1_attacking = False
                    p1_attack_frame = 0
                    p1_weapon_rotate = p1_weapon
                    p1_weapon_x = p1.x_pos + p1.x_diameter*0.25
                    if p1.facing_left == True:
                        p1_weapon_rotate = pygame.transform.flip(p1_weapon, 1, 0)
        if p1_char == knight:
            if p1.facing_right == True:
                if p1_attack_frame > 0 and p1_attack_frame < 5:
                    pass
                if p1_attack_frame >= 5 and p1_attack_frame < 15:
                    p1_weapon_rotate = pygame.transform.rotate(p1_weapon, -10*(p1_attack_frame-4))
                if p1_attack_frame >= 15 and p1_attack_frame < 25:
                    p1_weapon_rotate = pygame.transform.rotate(p1_weapon, -100 + 10*(p1_attack_frame-14))
                if p1_attack_frame == 25:
                    p1_attacking = False
                    p1_attack_frame = 0
                    p1_weapon_rotate = pygame.transform.rotozoom(p1_weapon, -45, 1)
                    p1_weapon_x = p1.x_pos + p1.x_diameter*0.75
            
            if p1.facing_left == True:
                if p1_attack_frame > 0 and p1_attack_frame < 5:
                    p1_weapon_x = p1.x_pos - p1.x_diameter*0.4
                if p1_attack_frame >= 5 and p1_attack_frame < 15:
                    p1_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p1_weapon, -10*(p1_attack_frame-4)), 1, 0)
                    p1_weapon_x = p1.x_pos - p1.x_diameter*0.4
                if p1_attack_frame >= 15 and p1_attack_frame < 25:
                    p1_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p1_weapon, 90 - 100 - 10*(p1_attack_frame-14)), 1, 0)
                    p1_weapon_x = p1.x_pos - p1.x_diameter*0.4
                if p1_attack_frame == 25:
                    p1_attacking = False
                    p1_attack_frame = 0
                    p1_weapon_rotate = pygame.transform.flip(pygame.transform.rotozoom(p1_weapon, -45, 1), 1, 0)
                    p1_weapon_x = p1.x_pos - p1.x_diameter*0.4
        #player 2 attack
        if keys[pygame.K_k] and p2_attacking == False and p2_hitstun == 0:
            p2_attacking = True
        if p2_attacking == True:
            p2_attack_frame += 1
        if p2_char == reaper:
            if p2.facing_right == True:
                if p2_attack_frame > 0 and p2_attack_frame < 5:
                    p2_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p2_weapon, -90), 0, 1)
                    p2_weapon_x = p2.x_pos + 0.75*p2.x_diameter
                if p2_attack_frame >= 5 and p2_attack_frame < 15:
                    p2_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p2_weapon, -90 + -15*(p2_attack_frame-4)), 0, 1)
                    p2_weapon_x = p2.x_pos + 0.75*p2.x_diameter
                if p2_attack_frame >= 15 and p2_attack_frame < 25:
                    p2_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p2_weapon, -90 + -100 + 15*(p1_attack_frame-14)), 0, 1)
                    p2_weapon_x = p2.x_pos + 0.75*p2.x_diameter
                if p1_attack_frame == 25:
                    p2_attacking = False
                    p2_attack_frame = 0
                    p2_weapon_rotate = p2_weapon
                    p2_weapon_x = p2.x_pos - p2.x_diameter*0.25
            
            if p2.facing_left == True:
                if p2_attack_frame > 0 and p2_attack_frame < 5:
                    p2_weapon_rotate = pygame.transform.rotate(p2_weapon, 90)
                    p2_weapon_x = p2.x_pos - 0.75*p2.x_diameter
                if p2_attack_frame >= 5 and p2_attack_frame < 15:
                    p2_weapon_rotate = pygame.transform.rotate(p2_weapon, 90 + -15*(p2_attack_frame-4))
                    p2_weapon_x = p2.x_pos - 0.75*p2.x_diameter
                if p2_attack_frame >= 15 and p2_attack_frame < 25:
                    p2_weapon_rotate = pygame.transform.rotate(p2_weapon, 90 + -100 + 15*(p2_attack_frame-14))
                    p2_weapon_x = p2.x_pos - 0.75*p2.x_diameter
                if p2_attack_frame == 25:
                    p2_attacking = False
                    p2_attack_frame = 0
                    p2_weapon_rotate = p2_weapon
                    p2_weapon_x = p2.x_pos + p2.x_diameter*0.25
                    if p2.facing_left == True:
                        p2_weapon_rotate = pygame.transform.flip(p2_weapon, 1, 0)
        if p2_char == knight:
            if p2.facing_right == True:
                if p2_attack_frame > 0 and p2_attack_frame < 5:
                    pass
                if p2_attack_frame >= 5 and p2_attack_frame < 15:
                    p2_weapon_rotate = pygame.transform.rotate(p2_weapon, -10*(p2_attack_frame-4))
                if p2_attack_frame >= 15 and p2_attack_frame < 25:
                    p2_weapon_rotate = pygame.transform.rotate(p2_weapon, -100 + 10*(p2_attack_frame-14))
                if p2_attack_frame == 25:
                    p2_attacking = False
                    p2_attack_frame = 0
                    p2_weapon_rotate = pygame.transform.rotozoom(p2_weapon, -45, 1)
                    p2_weapon_x = p2.x_pos + p2.x_diameter*0.75
            
            if p2.facing_left == True:
                if p2_attack_frame > 0 and p2_attack_frame < 5:
                    p2_weapon_x = p2.x_pos - p2.x_diameter*0.4
                if p2_attack_frame >= 5 and p2_attack_frame < 15:
                    p2_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p2_weapon, -10*(p2_attack_frame-4)), 1, 0)
                    p2_weapon_x = p2.x_pos - p2.x_diameter*0.4
                if p2_attack_frame >= 15 and p2_attack_frame < 25:
                    p2_weapon_rotate = pygame.transform.flip(pygame.transform.rotate(p2_weapon, 90 - 100 - 10*(p2_attack_frame-14)), 1, 0)
                    p2_weapon_x = p2.x_pos - p2.x_diameter*0.4
                if p2_attack_frame == 25:
                    p2_attacking = False
                    p2_attack_frame = 0
                    p2_weapon_rotate = pygame.transform.flip(pygame.transform.rotozoom(p2_weapon, -45, 1), 1, 0)
                    p2_weapon_x = p2.x_pos - p2.x_diameter*0.4
        #creates weapon hitbox
        p1_weapon_hitbox = pygame.Rect(round(p1_weapon_x), round(p1_weapon_y), round(p1_weapon_diameter_x), round(p1_weapon_diameter_y))
        p2_weapon_hitbox = pygame.Rect(round(p2_weapon_x), round(p2_weapon_y), round(p2_weapon_diameter_x), round(p2_weapon_diameter_y))
        #checks for if player 2 has been attacked and which way they should be sent
        if p1_weapon_hitbox.colliderect(p2.hitbox) and p1_attacking == True:
            p2_hitstun = 5
            p2_damage += 5
            if p1.facing_right == True:
                p1_was_right = True
                p1_was_left = False
                p2.x_pos += p1_weapon_diameter_x
            if p1.facing_left == True:
                p1_was_left = True
                p1_was_right = False
                p2.x_pos -= p1_weapon_diameter_x
        if p2_hitstun > 0:
            p2_hitstun -= 1
            if p1_was_right == True:
                #knocks back player based on damage
                p2.x_vel = p2_damage*screen_width/500
            if p1_was_left == True:
                p2.x_vel = -p2_damage*screen_width/500
            p2.x_pos += p2.x_vel
        #checks for if player 1 has been attacked
        if p2_weapon_hitbox.colliderect(p1.hitbox) and p2_attacking == True:
            p1_hitstun = 5
            p1_damage += 5
            if p2.facing_right == True:
                p2_was_right = True
                p2_was_left = False
                p1.x_pos += p2_weapon_diameter_x
            if p2.facing_left == True:
                p2_was_left = True
                p2_was_right = False
                p1.x_pos -= p2_weapon_diameter_x
        if p1_hitstun > 0:
            p1_hitstun -= 1
            if p2_was_right == True:
                p1.x_vel = p1_damage*screen_width/500
            if p2_was_left == True:
                p1.x_vel = -p1_damage*screen_width/500
            p1.x_pos += p1.x_vel
        #resets values after attack ends
        if p1_hitstun == 0:
            p1.x_vel = screen_width/150
            p1.x_accel = 0
        if p2_hitstun == 0:
            p2.x_vel = screen_width/150
            p1.x_accel = 0
        #player 1 fast fall
        if keys[pygame.K_s]:
            #increases downwards acceleration for faster fall
            p1.y_accel -= screen_height/50
        #player 1 jump
        if keys[pygame.K_w] and p1.jumping == 0 and p1.jumps > 0 and p1_attacking == False:
            #creates initial velocity and downwards acceleration for projectile motion
            p1.y_vel = screen_height/2.5
            p1.y_accel = -screen_height/50
            p1.jumping = 1
        #takes away a jump
        if keys[pygame.K_w] == False and p1.jumping == 1:
            #causes if statement to not run next time which would take away multiple jumps
            p1.jumping = 0
            p1.jumps -= 1
        #moves player
        p1.y_vel += p1.y_accel
        p1.y_pos -= p1.y_vel/20
        #creates player hitbox
        p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))   
        if p1.hitbox.colliderect(stage_hitbox):
            #if player 1 falls through the stage, push them out and reset jumps
            if p1.x_pos > stage_x - p1.x_diameter and p1.x_pos < screen_width*0.875:
                p1.y_pos = stage_y - p1.y_diameter + 1
                p1.y_vel = 0
                p1.y_accel = -screen_height/50
                p1.jumps = 2
                p1.jumping = 0
        #player 1 left
        if keys[pygame.K_a] and keys[pygame.K_d] == False and p1_attacking == False and p1_hitstun == 0:
            #turns player 1 and weapon to the left
            if p1.facing_right == True:
                p1_sprite = pygame.transform.flip(p1_sprite, 1, 0)
                p1_weapon_rotate = pygame.transform.flip(p1_weapon_rotate, 1, 0)
                p1.facing_right = False
                p1.facing_left = True
            #moves player 1
            p1.x_vel = screen_width/150
            p1.x_pos -= p1.x_vel
        else:
            p1.x_vel = 0
        #player 1 right
        if keys[pygame.K_d] and keys[pygame.K_a] == False and p1_attacking == False and p1_hitstun == 0:
            #turns player 1 and weapon to the right
            if p1.facing_left == True:
                p1_sprite = pygame.transform.flip(p1_sprite, 1, 0)
                p1_weapon_rotate = pygame.transform.flip(p1_weapon_rotate, 1, 0)
                p1.facing_left = False
                p1.facing_right = True
            p1.x_vel = screen_width/150
            p1.x_pos += p1.x_vel
        else:
            p1.x_vel = 0
        #makes it so that player is not collided with stage in y axis(allowing x axis collision to be checked)
        p1.y_pos -= 2
        p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))
        #checks if player is collided with sides of stage
        if p1.hitbox.colliderect(stage_hitbox):
            #if player 1 is moving left when collided with stage, push them to right side of stage
            if keys[pygame.K_a]:
                if p1.y_pos > (stage_y)-(screen_height/10):
                    p1.x_pos = screen_width*0.875
            #if player 1 is moving right when collided with stage, push them to left side of stage
            elif keys[pygame.K_d]:
                if p1.y_pos > (stage_y)-(screen_height/10):
                    p1.x_pos = stage_x - p1.x_diameter
        #sets player y position back to normal
        p1.y_pos += 2
        #redefines new player hitbox
        p1.hitbox = pygame.Rect(round(p1.x_pos), round(p1.y_pos), round(p1.x_diameter), round(p1.y_diameter))
        #movement for player 2
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
        
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] == False and p2_attacking == 0 and p2_hitstun == 0:
            if p2.facing_right == True:
                p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                p2_weapon_rotate = pygame.transform.flip(p2_weapon_rotate, 1, 0)
                p2.facing_right = False
                p2.facing_left = True
            p2.x_vel = screen_width/150
            p2.x_pos -= p2.x_vel
        else:
            p2.x_vel = 0
            
        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] == False and p2_attacking == 0 and p2_hitstun == 0:
            if p2.facing_left == True:
                p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                p2_weapon_rotate = pygame.transform.flip(p2_weapon_rotate, 1, 0)
                p2.facing_left = False
                p2.facing_right = True
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
        #changes weapon position relative to character
        if p1_char == reaper:
            p1_weapon_y = p1.y_pos - p1.y_diameter*0.1
            if p1_attacking == 0:
                if p1.facing_right == True:
                    p1_weapon_x = p1.x_pos - p1.x_diameter*0.25 
                if p1.facing_left == True:
                    p1_weapon_x = p1.x_pos  + p1.x_diameter*0.25
        if p2_char == reaper:
            p2_weapon_y = p2.y_pos - p2.y_diameter*0.1
            if p2_attacking == 0:
                if p2.facing_right == True:
                    p2_weapon_x = p2.x_pos - p2.x_diameter*0.25 
                if p2.facing_left == True:
                    p2_weapon_x = p2.x_pos  + p2.x_diameter*0.25
        if p1_char == knight:
            p1_weapon_y = p1.y_pos - p1.y_diameter/4
            if p1_attacking == 0:
                if p1.facing_right == True:
                    p1_weapon_x = p1.x_pos + p1.x_diameter*0.9
                if p1.facing_left == True:
                    p1_weapon_x = p1.x_pos - p1.x_diameter*0.4
        if p2_char == knight:
            p2_weapon_y = p2.y_pos - p2.y_diameter/4
            if p2_attacking == 0:
                if p2.facing_right == True:
                    p2_weapon_x = p2.x_pos + p2.x_diameter*0.9
                if p2.facing_left == True:
                    p2_weapon_x = p2.x_pos - p2.x_diameter*0.4
        #displays damage of both players
        font = pygame.font.SysFont("Times New Roman", round(screen_width/50))
        text = font.render("Player 1 damage:", True, (0, 0, 0) )
        win.blit(text, ((0), (0)))
        text = font.render("Player 2 damage:", True, (0, 0, 0) )
        win.blit(text, ((0), (round(screen_width/50))))
        text = font.render("{0}".format(p1_damage), True, (0, 0, 0) )
        win.blit(text, ((round(screen_width/2)), (0)))
        text = font.render("{0}".format(p2_damage), True, (0, 0, 0) )
        win.blit(text, ((round(screen_width/2)), (round(screen_width/50))))
        #draws all sprites
        pygame.draw.rect(win, (0, 0, 0), [round(stage_x), round(stage_y), round(screen_width*0.75), round(screen_height/5)])
        win.blit(pygame.transform.scale(p1_sprite, (round(p1.x_diameter), round(p1.y_diameter))), (round(p1.x_pos), round(p1.y_pos)))
        win.blit(pygame.transform.scale(p1_weapon_rotate, (round(p1_weapon_diameter_x), round(p1_weapon_diameter_y))), (round(p1_weapon_x), round(p1_weapon_y)))
        win.blit(pygame.transform.scale(p2_sprite, (round(p2.x_diameter), round(p2.y_diameter))), (round(p2.x_pos), round(p2.y_pos)))
        win.blit(pygame.transform.scale(p2_weapon_rotate, (round(p2_weapon_diameter_x), round(p2_weapon_diameter_y))), (round(p2_weapon_x), round(p2_weapon_y)))
        #checks if a player is out of bounds. If so, ends loop
        if p1.x_pos <= -p1.x_diameter or p1.x_pos >= screen_width or p1.y_pos <= -p1.y_diameter or p1.y_pos >= screen_height:
            player_1_dead = True
            player_dead = True
            p1.dead = True
        if p2.x_pos <= -p2.x_diameter or p2.x_pos >= screen_width or p2.y_pos <= -p2.y_diameter or p2.y_pos >= screen_height:
            player_2_dead = True
            player_dead = True
            p2.dead = True
        pygame.display.update()
    #occurs until r has been pressed
    while restart == False:
        pygame.time.delay(25)
        win.fill((255, 255, 255))
        #exit button and window resize
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
        #displays which player lose based on which character went offscreen
        font = pygame.font.SysFont("Times New Roman", round(screen_width/10))
        if player_1_dead == True:
            text = font.render("Player 2 wins!", True, (0, 0, 0) )
        if player_2_dead == True:
            text = font.render("Player 1 wins!", True, (0, 0, 0) )
        win.blit(text, ((0), (0)))
        win.blit(font.render("Press r to restart", True, (0, 0, 0) ), ((0), (round(screen_width/10))))

        keys = pygame.key.get_pressed()
        #resets all relevant values to what they originally were when r is pressed
        if keys[pygame.K_r]:
            stage_y = screen_height/1.25
            stage_x = screen_width/8
            if p1.facing_left == True:
                p1_sprite = pygame.transform.flip(p1_sprite, 1, 0)
                p1_weapon_rotate = pygame.transform.flip(p1_weapon, 1, 0)
                p1.facing_left = False
                p1.facing_right = True
            if p2.facing_right == True:
                p2_sprite = pygame.transform.flip(p2_sprite, 1, 0)
                p2_weapon_rotate = pygame.transform.flip(p2_weapon, 1, 0)
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
            p2_damage = 0
            p2_hitstun = 0
            p1_damage = 0
            p1_hitstun = 0
            p1_was_right = False
            p1_was_left = False
            p2_was_right = False
            p2_was_left = False
        pygame.display.update()