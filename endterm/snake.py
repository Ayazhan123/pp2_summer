import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (255, 50, 80)
green = (0, 255, 0)
blue = (50, 155, 215)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score, level):
    value1 = score_font.render("Your Score: " + str(score), True, yellow)
    value2 = score_font.render("Your Level: " + str(level), True, yellow)
    dis.blit(value1, [15, 0])
    dis.blit(value2, [15, 30])
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(30, dis_width - 30 - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(30, dis_height - 30 - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("GAME OVER", red, 100, 100)
            message("Press C-Play Again or Q-Quit", red, 100, 130)
            Your_score(Length_of_snake - 1, Length_of_snake)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width-30 or x1 < 30 or y1 >= dis_height-30 or y1 < 30:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis,red, [0, 0, dis_width, dis_height], 30)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1, Length_of_snake)
 
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(30, dis_width - 30 - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(30, dis_height - 30 - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()