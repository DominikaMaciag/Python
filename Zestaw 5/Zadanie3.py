import pygame
import os
from random import randint

pygame.init()

CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

class Rakietka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
           self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 550:
           self.rect.x = 550



class Pilka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(4, 8), randint(-8, 8)] 

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[0] = randint(-8,8)


# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")


# tworzymy rakietkę i piłkę
rakietka = Rakietka(BIALY, 150, 10)
rakietka.rect.x = 250
rakietka.rect.y = 470

pileczka = Pilka(BIALY,10,10)
pileczka.rect.x = randint(0,680)
print ("-->", pileczka.rect.x )
pileczka.rect.y = 0

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie rakietki i piłeczki do listy
all_sprites_list.add(rakietka)
all_sprites_list.add(pileczka)

# zaczynamy właściwy blok programu
kontynuuj = True

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()

# Początkowe wyniki graczy
score = 0
best_score = 0 # to chcemy przeczytać z pliku i go uaktualniać

# -------- GLÓWNA PĘTLA PROGRAMU -----------
while kontynuuj:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False

    # ruchy rakiety
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rakietka.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        rakietka.moveRight(5)

    # aktualizacja listy duszków
    all_sprites_list.update()

    # sprawdzenie czy piłeczka nie uderza w którąś ścianę
    # zamknięcie programu gdy zderzy się z "podłogą"
    if pileczka.rect.x>=690: # jeśli dotknie lewej ściany
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.x<=0: # jeśli dotknie prawej ściany 
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.y>490: # jeśli dotknie dołu 
        # pygame.quit()
        print("score: ", score)
        break
    if pileczka.rect.y<0: # jeśli dotknie góry 
        pileczka.velocity[1] = -pileczka.velocity[1]

    # sprawdzenie kolizji piłeczki z rakietką
    if pygame.sprite.collide_mask(pileczka, rakietka):
        pileczka.bounce()
        score += 1

    # RYSOWANIE
    # czarny ekran
    screen.fill(CZARNY)

    # narysowanie obiektów
    all_sprites_list.draw(screen)

    # wyświetlanie wyników
    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, BIALY)
    screen.blit(text, (340,10))

    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)


# otwieranie pliku i wypisywanie wartosci
score_s = ""
print("---> size: ", os.path.getsize('best.txt'))

if os.path.getsize('best.txt') == 0:
    # print("if size 0 został wywołany!")
    file0 = open('best.txt', 'w')
    file0.write(str(score))
    file0.close()

else:
    file = open('best.txt', 'r') 
    while True:
        char = file.read(1)   
        score_s += char      
        if not char:
            break
    # print("score z pliku to: " + score_s)
    file.close()

    file1 = open('best.txt','w')
    # sprawdzamy czy obecny score jest większy od highest score
    if ( score > int(score_s)):
        best_score = score
        file1.write(str(best_score))
    else:
        best_score = score_s
        file1.write(str(best_score))
    file1.close()


while kontynuuj:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False

    screen.fill(CZARNY)

    # wyświetlanie wyników
    font = pygame.font.Font(None, 50)
    text0 = font.render("GAME OVER", 1, BIALY)
    screen.blit(text0, (250,10))
    text = font.render("Your score: " + str(score), 1, BIALY)
    screen.blit(text, (50,100))
    text2 = font.render("Best score: " + str(best_score), 1, BIALY)
    screen.blit(text2, (400,100))

    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)

# koniec
pygame.quit()


