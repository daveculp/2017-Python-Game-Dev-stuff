import random, pygame, sys

def draw_fields():
    for pos,color in zip(far_field_pos, far_field_color):
        screen.set_at( (pos[0],pos[1]), color )

    for pos,color in zip(med_field_pos, med_field_color):
        #screen.set_at( (pos[0],pos[1]), color )
        pygame.draw.circle(screen, color, (pos[0],pos[1]), med_field_radius, 0)

    for pos,color in zip(near_field_pos, near_field_color):
        #screen.set_at( (pos[0],pos[1]), color )
        pygame.draw.circle(screen, color, (pos[0],pos[1]), near_field_radius, 0)
        
def move_fields():
    #move far_field
    for num in range(0, len(far_field_pos) ):
        y = far_field_pos[num][1]
        y+= far_field_vel
        if y>=SCREEN_HEIGHT: y = (SCREEN_HEIGHT-y)
        far_field_pos[num][1] = y

    for num in range(0, len(med_field_pos) ):
        y = med_field_pos[num][1]
        y+= med_field_vel
        if y>=SCREEN_HEIGHT: y = (SCREEN_HEIGHT-y)
        med_field_pos[num][1] = y

    for num in range(0, len(near_field_pos) ):
        y = near_field_pos[num][1]
        y+= near_field_vel
        if y>=SCREEN_HEIGHT: y = (SCREEN_HEIGHT-y)
        near_field_pos[num][1] = y

def generate_fields():
    #generate far field
    for x in range(0, far_field_num):
        point = [random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) ]
        color = ( random.randint(0,255), random.randint(0,255), random.randint(0,255) )
        far_field_pos.append(point)
        far_field_color.append(color)

    for x in range(0, med_field_num):
        point = [random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) ]
        color = ( random.randint(0,255), random.randint(0,255), random.randint(0,255) )
        med_field_pos.append(point)
        med_field_color.append(color)

    for x in range(0, near_field_num):
        point = [random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) ]
        color = ( random.randint(0,255), random.randint(0,255), random.randint(0,255) )
        near_field_pos.append(point)
        near_field_color.append(color)

    
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

far_field_pos = list()
far_field_color = list()
far_field_num = 2500
far_field_vel = 1
far_field_radius = 1

med_field_pos = list()
med_field_color = list()
med_field_num = 100
med_field_vel = 3
med_field_radius = 2

near_field_pos = list()
near_field_color = list()
near_field_num = 15
near_field_vel = 5
near_field_radius = 5


generate_fields()

pygame.init()
#init screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#clock to keep track of framerate
clock = pygame.time.Clock()

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
    screen.fill( (0,0,0) )
    draw_fields()  
    pygame.display.update()
    clock.tick(30)
