## 04.10.2024, 18.10.2024
## IMPORTS
import pygame
import sys
import random
##

## MAIN

pygame.init()


width = 1000
height = 800

green = (50,130,0)
#image_surface fehlt
player_surf = green

yellow = (240,240,0)
red = (120,0,0)
background = (0,0,0)

rate = 0.1
rate_rdb = 0.5 ## check!

player_size = 40
player_pos = [width/2,height-2*player_size]

#enemy data
enemy_size = 50
enemy_pos = [random.randint(0,width-enemy_size),0]
enemy_list = [enemy_pos]

#reset diff block data
rdb_size = 30
rdb_pos = [random.randint(0,width-rdb_size), 0]
rdb_list = [rdb_pos]

#image_surface = pygame.transform.scale(image_surface, (player_size, player_size)) - does not work yet
screen = pygame.display.set_mode((width, height))




game_over = False
score = 0
level = 0
clock = pygame.time.Clock() #framerate
speed = 2 #game level


myFont=pygame.font.SysFont("aquakana",35, bold=False, italic=False)
mygoFont=pygame.font.SysFont("aquakana",50, bold=True, italic=False)
difficulty = 4

##FUNCTIONS

def set_level(score, speed): #update this
    speed = score/difficulty + difficulty/2
    return speed
    
    
## ENEMIES  

def drop_ens(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < rate:
        x_pos = random.randint(0, width-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos,y_pos])


def draw_ens(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen,red,(enemy_pos[0], enemy_pos[1],enemy_size, enemy_size))


## COLLISION W ENEMIES

def detect_coll(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x+player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
        if (e_y >= p_y and e_y < (p_y+player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
            return True
    return False

def update_en_pos(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < height: #on the screen
            enemy_pos[1] = enemy_pos[1] + speed
        else:
            enemy_list.pop(idx)
            score = score + 1
    return score
 

def coll_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_coll(enemy_pos, player_pos):
            return True
    return False 


## RESET DIFF BLOCKS

def drop_rdbs(rdb_list):
    delay = random.random()
    if len(rdb_list) < 1 and delay < rate_rdb:
        x_pos = random.randint(0, width-rdb_size)
        y_pos = 0
        rdb_list.append([x_pos,y_pos])


def draw_rdbs(rdb_list):
    for  rdb_pos in rdb_list:
        pygame.draw.rect(screen,yellow,(rdb_pos[0], rdb_pos[1],rdb_size, rdb_size))


def update_rdb_pos(rdb_list):
    for idx, rdb_pos in enumerate(rdb_list):
        if rdb_pos[1] >= 0 and rdb_pos[1] < height: #on the screen
            rdb_pos[1] = rdb_pos[1] + speed
        else:
            rdb_list.pop(idx)
 

### COLLECT RESET DIFF BLOCKS

def collection_check(rdb_list, player_pos):
    for rdb_pos in rdb_list:
        if detect_coll(rdb_pos, player_pos): #check
            return True
    return False 


## GAME LOOP
while not game_over:
    
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit

        if event.type == pygame.KEYDOWN:

            x = player_pos[0] #k-coord
            y = player_pos[1] #y-coord

            if event.key == pygame.K_a:
                x = x-player_size
            elif event.key == pygame.K_d:
                x = x+player_size
            elif event.key == pygame.K_w:
                y = y-player_size
            elif event.key == pygame.K_s:
                y = y+player_size
            
            player_pos = [x,y]
                

    screen.fill(background)


   
    ### SCORES
    score = update_en_pos(enemy_list,score)
    speed = set_level(score, speed)

    text1 = "Score:" + str(score)
    label = myFont.render(text1,1,yellow)
    screen.blit(label,(width-190,height-40)) #magic nums

    clock.tick(30)

    
    game_over_w = width-300
    game_over_h = height-120
    delay_num = 400
    drop_ens(enemy_list)
    drop_rdbs(rdb_list)
    update_en_pos(enemy_list, score)
    update_rdb_pos(rdb_list)


    #if collection_check(rdb_list,player_pos):
       # score -= 1

    if coll_check(enemy_list, player_pos):
        text3 = "Game over!"
        label = mygoFont.render(text3,1,yellow)
        screen.blit(label,(game_over_w,game_over_h)) #magic nums

        pygame.time.wait(delay_num) #Delay for game over notification - doesn't work
        game_over = True

        # replay menu

     

    draw_ens(enemy_list)
    draw_rdbs(rdb_list)
    pygame.draw.rect(screen,player_surf,(player_pos[0],player_pos[1],player_size, player_size))  ###change that to other form
    

    pygame.display.update()
    #pygame.display.flip()
