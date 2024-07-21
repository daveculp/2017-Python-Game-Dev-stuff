import random, pygame, sys

#FUNCTIONS SECTION
def draw_frame():
    screen.fill( (0,0,0) )
    draw_fields()
    draw_game_text()

def draw_game_text():
    game_score_text = font.render("score: "+str(player_score), True, (128, 255, 0))
    energy_text = font.render("energy: "+str(player_energy), True, (255, 64, 32))
    bomb_text = font.render("Smart Bombs: "+str(player_smart_bombs), True, (64, 0, 255))

    screen.blit(game_score_text, (0, 0))
    screen.blit(bomb_text, ((SCREEN_WIDTH/2) - (bomb_text.get_width()/2), 0))
    screen.blit(energy_text, (SCREEN_WIDTH-energy_text.get_width(), 0))
    
    pygame.draw.line(screen, (0, 255, 0), (0, game_score_text.get_height()+2), (SCREEN_WIDTH, game_score_text.get_height()+2), 3)

    
def draw_fields():
    for pos,color in zip(far_field_pos, far_field_color):
        screen.set_at( (pos[0],pos[1]), color )
        #pygame.draw.circle(screen, color, (pos[0],pos[1]), 1, 0)

    for pos,color in zip(med_field_pos, med_field_color):
        #screen.set_at( (pos[0],pos[1]), color )
        pygame.draw.circle(screen, color, (pos[0],pos[1]), 2, 0)

    for pos,color in zip(near_field_pos, near_field_color):
        #screen.set_at( (pos[0],pos[1]), color )
        pygame.draw.circle(screen, color, (pos[0],pos[1]), 4, 0)        

def move_fields():
    for num in range(0, len(far_field_pos) ):
        y=far_field_pos[num][1]
        y+=1
        if y>=SCREEN_HEIGHT: y = (SCREEN_HEIGHT-y)
        far_field_pos[num][1] = y

    for num in range(0, len(med_field_pos) ):
        y=med_field_pos[num][1]
        y+= med_field_vel
        if y>=SCREEN_HEIGHT: y = (SCREEN_HEIGHT-y)
        med_field_pos[num][1] = y

    for num in range(0, len(near_field_pos) ):
        y=near_field_pos[num][1]
        y+= near_field_vel
        if y>=SCREEN_HEIGHT: y = (SCREEN_HEIGHT-y)
        near_field_pos[num][1] = y

def generate_fields():
    #generate far field
    for x in range(0, far_field_num):
        point = [random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) ]
        col = (random.randint(0,255), random.randint(0,255), random.randint(0,255) )
        far_field_pos.append(point)
        far_field_color.append(col)

    for x in range(0, med_field_num):
        point = [random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) ]
        col = (random.randint(0,255), random.randint(0,255), random.randint(0,255) )
        med_field_pos.append(point)
        med_field_color.append(col)

    for x in range(0, near_field_num):
        point = [random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) ]
        col = (random.randint(0,255), random.randint(0,255), random.randint(0,255) )
        near_field_pos.append(point)
        near_field_color.append(col)

def reset_game():
    global player_score, player_energy, player_smart_bombs
    player_score = 0
    player_energy = 100
    player_smart_bombs = 2
    
#START CONTANTS AND VARIABLES SECTION
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

far_field_pos = list()
far_field_color = list()
far_field_num = 2000
far_field_vel = 1

med_field_pos = list()
med_field_color = list()
med_field_num = 10
med_field_vel = 2

near_field_pos = list()
near_field_color = list()
near_field_num = 50
near_field_vel = 4


#INIT SECTION
generate_fields()
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#clock to keep track of framerate
clock = pygame.time.Clock()

#font items
font = pygame.font.Font("./media/fonts/zorque.ttf", 24, bold=True)
player_score = 0
player_energy = 0
player_smart_bombs = 0

reset_game()
#MAIN GAME LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
    move_fields()
    draw_frame()  
    pygame.display.update()
    clock.tick(30)
