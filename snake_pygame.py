import pygame
import random
pygame.init()


red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
width , height = 900 , 600

gamewindow = pygame.display.set_mode((width,height))
pygame.display.set_caption('SNAKE GAME')
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

def screen(text, color, x,y):
    text = font.render(text, True, color)
    gamewindow.blit(text, [x,y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])
        
def game_loop():
    exit_game = False
    game_over = False
    pos_x = 25
    pos_y = 50
    snake_size = 20
    fps = 50
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(0,width)
    food_y = random.randint(0,height)
    score = 0

    with open('hiscore.txt','r') as f:
        hiscore = f.read()

    snk_list = []
    snk_length = 1

    while not exit_game:
        if game_over:
            gamewindow.fill(white)
            screen('GAME OVER! press ENTER to continue',red,width/12,height/12 )
            with open('hiscore.txt','w') as f:
                f.write(str(hiscore))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()    
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =  init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x =  -init_velocity
                        velocity_y =  0
                    if event.key == pygame.K_UP:
                        velocity_y =  -init_velocity
                        velocity_x =  0
                    if event.key == pygame.K_DOWN:
                        velocity_y =  init_velocity
                        velocity_x =  0
                
            pos_x += velocity_x
            pos_y += velocity_y
            if abs(pos_x - food_x) < 8 and abs(pos_y - food_y) <8:
                score += 10
                snk_length += 5
                food_x = random.randint(0,width/2)
                food_y = random.randint(0,height/2)
                if score > int(hiscore):
                    hiscore = score
                
            gamewindow.fill(white)
            screen('SCORE:'+str(score)+'  HIGH SCORE:'+str(hiscore),red,5,5 )
            #pygame.draw.rect(gamewindow, black, [pos_x, pos_y, snake_size, snake_size])
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.extend([pos_x,pos_y])
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del(snk_list[0])

            if head in snk_list[:-1]:
                game_over = True

            if pos_x < 0 or pos_x > width or pos_y < 0 or pos_y > height:
                game_over = True

            plot_snake(gamewindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

game_loop()