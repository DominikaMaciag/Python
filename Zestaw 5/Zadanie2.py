# Zadanie 2 - symulacja ruchu w polu grawitacyjnym. 

import math
import pygame, sys
pygame.init()

def main():
    clock = pygame.time.Clock()

    pygame.display.set_caption('Nasze okienko')
    icon = pygame.image.load('moon.jpg')
    pygame.display.set_icon(icon)

    pygame.mixer.music.load(r'music.mp3')
    pygame.mixer.music.play(1) 

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    x_0 = 0.25 # x początkowe
    y_0 = 0.25 # y początkowe
    speed = [x_0,y_0] # ustalamy początkową prędkość
    accel = [0.25, 0.25]
    g = [0, 9.81] # przyspieszenie ziemskie

    image = pygame.image.load(r'moon.jpg')
    image = pygame.transform.scale(image, size)

    surf_center = (
        (width-image.get_width())/2,
        (height-image.get_height())/2
    )

    screen.blit(image, surf_center)
    ball = pygame.image.load('ball.gif')
    ball = pygame.transform.scale(ball, (ball.get_width()//2, ball.get_height()//2))
    
    screen.blit(ball, (width/2, height/2))
    ballrect = ball.get_rect(center=(width/2, height/2)) 
    pygame.display.flip()
    energia_calkowita = ((accel[1])*(height-ballrect.bottom))+ (1.39*speed[1]*speed[1]/2)

    while True:
        t = clock.tick(120) *0.001
        # pygame.time.delay(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
   
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: sys.exit()

        # poruszanie dla testów
        if keys[pygame.K_UP]:
            speed[1] -= accel[1]*000000.1
        elif keys[pygame.K_DOWN]:
            speed[1] += accel[1]*000000.1
        elif keys[pygame.K_LEFT]:
            speed[0] -= accel[0]*000000.1
        elif keys[pygame.K_RIGHT]:
            speed[0] += accel[0]*000000.1
        
        while ((g[1])*(height-ballrect.bottom)*38.44)+ (1.39*speed[1]*speed[1]/2) < energia_calkowita:
            ballrect = ballrect.move([0,-5])

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
            
        speed[1] += g[1]*t

                 
        screen.blit(image,surf_center)
        screen.blit(ball,ballrect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
