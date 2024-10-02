
# rabbit game using directions and with ability to control volumes and speed


import pygame
import sys
import random
import pygame.display
pygame.init()


# Set up the display
#================== to open window=================================
window_width=1100
window_height=550
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
screen.fill(white)
#background = pygame.image.load(r"/games_training/garden.jpg")
background = pygame.image.load("C:\\Users\\Mohamed Emad\\source\\repos\\games_training\\games_training\\grass.jpg")
background = pygame.transform.smoothscale(background, (window_width, window_height))
pygame.display.update()
#==================================================================
#=====================rabbit========================================================================================

def moving_rabbit():
 rabbit_x=window_width//2
 rabbit_y=window_height//2
 rabbit_width=80
 rabbit_height=100
 image_rabbit = pygame.image.load(r"C:\Users\Mohamed Emad\source\repos\games_training\games_training\rabbit.png")
 image_rabbit = pygame.transform.smoothscale(image_rabbit, (rabbit_width, rabbit_height)) 

 carrot_width=60
 carrot_height=85
 image_carrot = pygame.image.load(r"C:\Users\Mohamed Emad\source\repos\games_training\games_training\carrot2.png")
 image_carrot = pygame.transform.smoothscale(image_carrot, (carrot_width, carrot_height)) 
 rabbit_step=3
 jump_height=25
 gravity=1
 is_jumping=False
 last_direction= None
 flag=True

     
     
 carrots_list=[]
 i=1
 while i<=15:
     x=int((random.randint(0,window_width-carrot_width))/20)*20
     y=int((random.randint(0,window_height-carrot_height))/20)*20
     if ([x,y] not in carrots_list):
       carrots_list.append([x,y])
       i+=1

 def jump(x,y):
     start=y
     is_jumping=True
     flag=True
     i=1
     while is_jumping:
         pygame.time.delay(5)
         y -= (jump_height-(gravity*i))  
         screen.blit(background, (0, 0))
         screen.blit(image_rabbit, (x,y))
         for carrot in carrots_list:
          if ((carrot[0]+(carrot_width//2)) in range(x,x+rabbit_width)) and ((carrot[1]+(carrot_height//2)) in range(y,y+rabbit_height)):
            carrots_list.remove(carrot)
         for carrot in carrots_list:
           screen.blit(image_carrot, (carrot[0], carrot[1]))
         pygame.display.update()
         i+=1
         if y==start:
             is_jumping=False

 while flag:
    pygame.time.delay(5)
    for event in pygame.event.get(): 
      if event.type==pygame.QUIT:
          flag=False   
    
    screen.blit(image_rabbit, (rabbit_x, rabbit_y))
    for carrot in carrots_list:
        screen.blit(image_carrot, (carrot[0], carrot[1]))
    pygame.display.update()
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        last_direction = 'left'
    elif keys[pygame.K_RIGHT]:
        last_direction = 'right'
    elif keys[pygame.K_UP]:
        last_direction = 'up'
    elif keys[pygame.K_DOWN]:
        last_direction = 'down'
    elif keys[pygame.K_SPACE]:
        if not is_jumping:
            jump(rabbit_x,rabbit_y)
    else :
        last_direction=None
    
    if last_direction=='left': 
        rabbit_x -= rabbit_step
    if last_direction=='right':
        rabbit_x += rabbit_step
    if last_direction=='up':
        rabbit_y -= rabbit_step
    if last_direction=='down':
        rabbit_y += rabbit_step

    # Ensure the square stays within the window boundaries
    if rabbit_x < 0-rabbit_width:
        rabbit_x = window_width
    if rabbit_x > window_width:
        rabbit_x =0-rabbit_width #window_width-rabbit_width 
    if rabbit_y < 0-rabbit_height:
        rabbit_y = window_height
    if rabbit_y > window_height:
        rabbit_y = 0-rabbit_height 

    for carrot in carrots_list:
        if ((carrot[0]+(carrot_width//2)) in range(rabbit_x,rabbit_x+rabbit_width)) and ((carrot[1]+(carrot_height//2)) in range(rabbit_y,rabbit_y+rabbit_height)):
            carrots_list.remove(carrot)
    
    screen.blit(background, (0, 0))

#===================================================================================================================




    
#moving_square()
moving_rabbit()

pygame.quit()