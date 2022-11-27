# Na bazie powyższego kodu zrobimy symulację ruchu w polu grawitacyjnym. 
# Proszę zatem ustalić jakieś wartości prędkości początkowej piłki, przyspieszenie ma składową pionową (0, 9.81) (składowe x, y). 
# I teraz, jeśli piłka jest nieruchoma na początku – to będzie to spadek swobodny (z przyspieszeniem g = 9.81 m/s2), 
# jeśli "rzucona w górę" (vy > 0), to rzut pionowy, jeśli "rzucona w bok" (vx > 0) to rzut poziomy i ogólnie – rzut ukośny.

# Piłka powinna poruszać się realistycznie 
# (w sensie: należy wyliczać jej prędkości według ruchu przyspieszonego w pionie i jednostajnego w poziomie). 
# Oczywiście, podobnie jak w zadaniu 1, wartość przyspieszenia (numerycznie) może być dowolnie dobrana tak, 
# żeby ruch odbywał się płynnie, nie za wolno i nie za szybko. 
# Proszę odbijać piłkę doskonale sprężyście (bez strat energii! – czyli w sumie w nieskończoność).
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

    x_0 = 0.005 # x początkowe
    y_0 = 0.005 # y początkowe
    speed = [x_0,y_0] # ustalamy początkową prędkość
    accel = [0.025, 0.025]
    g = [0, 9.81] # przyspieszenie ziemskie
    t = 1

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

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
   
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: sys.exit()

        if keys[pygame.K_UP]:
            speed[1] -= accel[1]*t
            t+=0.00001 
        elif keys[pygame.K_DOWN]:
            speed[1] += accel[1]*t
            t+=0.00001
        elif keys[pygame.K_LEFT]:
            speed[0] -= accel[0]
        elif keys[pygame.K_RIGHT]:
            speed[0] += accel[0]
        if (speed == [x_0, y_0]): # jeśli piłka nieruchoma na początku to będzie spadek swobodny
            speed[1] = g[1]*t
            t += 0.0001

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
                 
        screen.blit(image,surf_center)
        screen.blit(ball,ballrect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()