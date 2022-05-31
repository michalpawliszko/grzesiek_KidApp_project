import pygame
import random

pygame.init()
# 1)
BG_COLOR = (76,77,75)
SNAKE_COLOR = (12, 205, 30)
FOOD_COLOR = (234, 0, 0)
TEXT_COLOR = (250, 208, 204)

#################################################
WIDTH = 700
HEIGHT = 500
SIZE = [WIDTH, HEIGHT]
window = pygame.display.set_mode(SIZE)


class Pixel:
   def __init__(self, color, x, y, width, height):
       self.color = color
       self.x = x
       self.y = y
       self.width = width
       self.height = height

   def draw(self):
       self.rect = pygame.draw.rect(window, self.color, [self.x, self.y, self.width, self.height])




pygame.display.set_caption("SNAKE")
font_name = pygame.font.match_font('agency fb')


def draw_text(surf, text, size, x, y, color):
   font = pygame.font.Font(font_name, size)
   text_surface = font.render(text, True, color)
   text_rect = text_surface.get_rect()
   text_rect.midtop = (x, y)
   surf.blit(text_surface, text_rect)


clock = pygame.time.Clock()
fps = 60
####################################################

snake = Pixel(SNAKE_COLOR, 350 ,250, 30, 30)

speed_x = 0
speed_y = -5

random_x = random.randint(0, WIDTH - 30)
random_y = random.randint(0, HEIGHT - 30)

food = Pixel(FOOD_COLOR,random_x ,random_y ,30, 30)


tail = []
snake_lenght = 1
score = 0
Game_over = False
run = True
while run:

   if Game_over == False:
       for  event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False

           elif event.type == pygame.KEYDOWN:

               if event.key == pygame.K_LEFT and speed_x == 0:
                   speed_x = -5
                   speed_y = 0

               if event.key == pygame.K_RIGHT and speed_x == 0:
                   speed_x = 5
                   speed_y = 0

               if event.key == pygame.K_UP and speed_y == 0:
                   speed_x = 0
                   speed_y = -5

               if event.key == pygame.K_DOWN and speed_y == 0:
                   speed_x = 0
                   speed_y = 5


       window.fill(BG_COLOR)
       food.draw()
       snake.draw()

       snake.x += speed_x
       snake.y += speed_y

       if pygame.sprite.collide_rect(snake, food):
           food.x = random.randint(0, WIDTH - 30)
           food.y = random.randint(0, HEIGHT - 30)
           snake_lenght += 3
           score += 1

       head = []
       head.append(snake.x)
       head.append(snake.y)


       tail.append(head)


       for part in tail:
           pygame.draw.rect(window, SNAKE_COLOR, [part[0], part[1], snake.width, snake.height])

       if len(tail) > snake_lenght:
           del tail[0]

       draw_text(window, f"SCORE: {score}", 40, 80, 30, (255, 255, 255))

       if snake.x >= WIDTH or snake.x <0 or snake.y >= HEIGHT or snake.y < 0:
           Game_over = True

       for part in tail[:-1]:
           if part == head:
               Game_over = True
   else:
       for  event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
           elif event.type == pygame.MOUSEBUTTONDOWN:

               score = 0
               food.x = random.randint(0, WIDTH - 30)
               food.y = random.randint(0, HEIGHT - 30)
               snake.x = 350
               snake.y = 250
               tail.clear()
               snake_lenght = 1
               Game_over = False
               speed_x = 0
               speed_y = -5
       window.fill(BG_COLOR)

       draw_text(window, "GAME-OVER", 100, 350, 50, (255, 255, 255))
       draw_text(window, f"YOUR SCORE: {score}", 50, 350, 200, (255, 255, 255))
       draw_text(window, f"Click To Play Again", 60, 350, 350, (255, 255, 255))

   clock.tick(fps)
   pygame.display.update()
