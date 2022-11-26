# ------------ PLIK TESTOWY ------------ #

import pygame, sys
pygame.init()

def main():
    clock = pygame.time.Clock()

    pygame.display.set_caption('Nasze okienko :)')
    icon = pygame.image.load('moon.jpg')
    pygame.display.set_icon(icon)

    pygame.mixer.music.load(r'music.mp3')
    pygame.mixer.music.play(1) # -1 nieskończenie wiele, gdy podamy np. 5 to muzyka zostanie oddtworzona 5 razy

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    speed = [0, 0]
    accel = [0.1, 0.1]

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
    ballrect = ball.get_rect(center=(width / 2, height / 2))
    pygame.display.flip()

    while True:
        clock.tick(60)
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: sys.exit()

        if keys[pygame.K_UP]:
            pass # zamienić na jakieś przeliczenie
        elif keys[pygame.K_DOWN]:
            pass
        elif keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.blit(image,surf_center)
        screen.blit(ball,ballrect)
        pygame.display.flip()

    # while True:
    #     # pass 
    #     for event in pygame.event.get():
    #         # print(event) # wypisane zostaną wartości zwiącane z między innymi MouseMotion, MouseButtonDown, MouseButtonUp
    #         if event.type == pygame.QUIT: sys.exit()
    #     clock.tick(60) # ustawiamy fps, ich rzeczywista wartość cały czas się zmienia i jest zbliżona do tej którą podaliśmy
    #     # print(clock.get_fps())
    #     pygame.time.delay(25) #opóźnienie realizacji pętli, dla nawet podanych 200 fpsów z odkomentowanym opóźnieniem pętli wartości odczytane przez get_fps są na poziomie 20 fpsów


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
