# Разработай свою игру в этом файле!
import pygame
import random

pygame.init()

WIDTH = 880
HEIGHT = 720
#цвета
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#окно
window = pygame.display.set_mode((WIDTH, HEIGHT))
#загрузка фона
BG = pygame.image.load('BG2.jpg')
#масштабирование изоражения фона
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

#игровые часы
clock = pygame.time.Clock()



class Sprite(pygame.sprite.Sprite):
    def __init__ (self, image, x, y):
        super().__init__()
        #загрузка и масштабирование изображения
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (40, 40))
        #получение хитбокса
        self.rect = self.image.get_rect()
        #указать координаты
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Sprite2(pygame.sprite.Sprite):
    def __init__ (self, image, x, y):
        super().__init__()
        #загрузка и масштабирование изображения
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (60, 40))
        #получение хитбокса
        self.rect = self.image.get_rect()
        #указать координаты
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))     

class Player(Sprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 4
        elif keys[pygame.K_s]:
            self.rect.y += 4
        elif keys[pygame.K_d]:
            self.rect.x += 4
        elif keys[pygame.K_w]:
            self.rect.y -= 4
        elif keys[pygame.K_DOWN]:
            self.rect.y += 4
        elif keys[pygame.K_UP]:
            self.rect.y -= 4
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 4
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 4

#1-ый противник
class Enemy(Sprite):
    def update(self):
        self.rect.x += self.dx
        if self.rect.x <= 160 or self.rect.x >= 365:
            self.dx = -self.dx

#2-ой противник
class Enemy2(Sprite):
    def update(self):
        self.rect.x += self.dx
        if self.rect.x <= 410 or self.rect.x >= 610:
            self.dx = -self.dx

#3-ий противник
class Enemy3(Sprite):
    def update(self):
        self.rect.y += self.dy
        if self.rect.y <= 250 or self.rect.y >= 680:
            self.dy = -self.dy

#4-ый противник
class Enemy4(Sprite):
    def update(self):
        self.rect.x += self.dx   
        if self.rect.x <= 170 or self.rect.x >= 680:
            self.dx = -self.dx

#5-ый противник
class Enemy5(Sprite):
    def update(self):
        self.rect.y += self.dy
        if self.rect.y <= 165 or self.rect.y >= 360:
            self.dy = -self.dy

#6-ой противник
class Enemy6(Sprite):
    def update(self):
        self.rect.x += self.dx
        if self.rect.x <= 10 or self.rect.x >= 440:
            self.dx = -self.dx

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        #создание поверхности
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)
        #ХИТБОКС (rect)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rext.y))

enemies = pygame.sprite.Group()
walls = pygame.sprite.Group()
#стены границ
walls.add(Wall(-10, -10, 5000, 10))
walls.add(Wall(-10, 0, 10, 1000))
walls.add(Wall(880, 0, 10, 1000))
walls.add(Wall(0, 720, 5000, 10))

#number = random.randint(1,2)
#number = 1
number = 2
if number == 1:
    #стена-№1
    walls.add(Wall(100, 580, 100, 10))
    walls.add(Wall(100, 590, 10, 100))
    walls.add(Wall(300, 460, 10, 130))
    walls.add(Wall(400, 590, 10, 100))

    walls.add(Wall(100, 0, 450, 10))
    walls.add(Wall(100, 460, 350, 10))
    walls.add(Wall(100, 0, 10, 380))
    walls.add(Wall(200, 90, 10, 370))
    walls.add(Wall(450, 110, 10, 360))
    walls.add(Wall(300, 0, 10, 350))
    walls.add(Wall(390, 100, 130, 10))

elif number == 2:
    #стена-№2
        #горизонт
    walls.add(Wall(480, 480, 90, 10))
    walls.add(Wall(640, 160, 90, 10))
    walls.add(Wall(560, 240, 90, 10))
    walls.add(Wall(560, 80, 240, 10))
    walls.add(Wall(80, 240, 80, 10))
    walls.add(Wall(160, 400, 260, 10))
    walls.add(Wall(160, 80, 240, 10))
    walls.add(Wall(320, 160, 80, 10))
    walls.add(Wall(160, 640, 160, 10))
    walls.add(Wall(160, 480, 320, 10))
    walls.add(Wall(240, 560, 480, 10))
    walls.add(Wall(240, 240, 240, 10))
    walls.add(Wall(400, 320, 170, 10))
    walls.add(Wall(560, 400, 410, 10))
    walls.add(Wall(640, 480, 80, 10))
    walls.add(Wall(480, 640, 320, 10))

        #вертикаль
    walls.add(Wall(800, 400, 10, 250))
    walls.add(Wall(720, 480, 10, 90))
    walls.add(Wall(720, 160, 10, 250))
    walls.add(Wall(640, 320, 10, 80))
    walls.add(Wall(800, 80, 10, 250))
    walls.add(Wall(560, 400, 10, 90))
    walls.add(Wall(560, 80, 10, 260))
    walls.add(Wall(400, 320, 10, 90))
    walls.add(Wall(320, 240, 10, 90))
    walls.add(Wall(240, 160, 10, 170))
    walls.add(Wall(400, 80, 10, 90))
    walls.add(Wall(80, 80, 10, 980))
    walls.add(Wall(160, 80, 10, 320))
    walls.add(Wall(160, 480, 10, 160))
    walls.add(Wall(480, 0, 10, 250))
    walls.add(Wall(400, 560, 10, 250))

player = Player('Packman.png', 25, 100)

finish = Sprite2('finish.png', 815, 420)

if number == 1:
    bot = Enemy('oinky.png', 160, 340)
    bot2 = Enemy2('oinky.png', 540, 340)
    bot3 = Enemy3('oinky.png', 105, 320)
    bot4 = Enemy4('oinky.png', 300, 510)
    bot5 = Enemy5('oinky.png', 660, 170)
    bot6 = Enemy6('oinky.png', 20, 20)
    bot.dx = 1
    bot2.dx = 1
    bot3.dy = 1
    bot4.dx = 1
    bot5.dy = 1
    bot6.dx = 1

elif number == 2:
    bot = Enemy('plinky.png', 160, 340)
    bot2 = Enemy2('plinky.png', 540, 340)
    bot3 = Enemy3('oinky.png', 105, 320)
    bot4 = Enemy4('rinky.png', 300, 510)
    bot5 = Enemy5('oinky.png', 660, 170)
    bot6 = Enemy6('rinky.png', 20, 20)

    bot.dx = 2
    bot2.dx = 2
    bot3.dy = 3
    bot4.dx = 2
    bot5.dy = 2
    bot6.dx = 2

#перезапуск игры
def restart():
    global paused, final
    player.rect.x = 25
    player.rect.y = 100
    paused = False
    final = False

#управлени игровым циклом
run = True
paused = False
final = False

#звуки

pygame.mixer.music.load ('music.mp3')
pygame.mixer.music.play ()

kick = pygame.mixer.Sound('game_over.ogg')

kick.set_volume(0.2)
#текст

my_font = pygame.font.SysFont('verdana', 70)

text_pause = my_font.render('Pause', True, YELLOW)

text_win = my_font.render('Win', True, YELLOW)

text_lose = my_font.render('GAME OVER', True, YELLOW)

my_font = pygame.font.SysFont('verdana', 35)

text_restart = my_font.render('Press SPACE to restart', True, YELLOW)

text_continue = my_font.render('Press SPACE to continue', True, YELLOW)

#игровой цикл
while run:
    
    #перебор событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and paused and final:
                restart()

            if e.key == pygame.K_SPACE and not final:
                paused = not paused
    #отрисовака фона
    window.blit(BG, (0, 0))  

    #проверка паузы
    if not paused and not final:
        if number == 1:
            #обновление спрайтов
            player.update()
            bot.update()
            bot2.update()
            bot3.update()
            bot4.update()
            bot5.update()
            bot6.update()
            finish.update()
            #отрисовка спрайтов + спрайт
            player.draw()
            bot.draw()
            bot2.draw()
            bot3.draw()
            bot4.draw()
            bot5.draw()
            bot6.draw()
            walls.draw(window)
            finish.draw()
        
        elif number == 2:
            #обновление спрайтов
            player.update()
            bot.update()
            bot2.update()
            bot3.update()
            bot4.update()
            bot5.update()
            bot6.update()
            #отрисовка спрайтов
            player.draw()
            bot.draw()
            bot2.draw()
            bot3.draw()
            bot4.draw()
            bot5.draw()
            bot6.draw()
            walls.draw(window)
            finish.draw()
        #проверка коллизии игрока и стен
        if pygame.sprite.spritecollideany(player, walls) or pygame.sprite.collide_rect(player, bot) or pygame.sprite.collide_rect(player, bot3) or pygame.sprite.collide_rect(player, bot4) or pygame.sprite.collide_rect(player, bot5) or pygame.sprite.collide_rect(player, bot6):
            paused = True
            #BG = pygame.image.load('try_again.png')
            #BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
            final = True
            text_fin = text_lose
            kick.play()
            
        ##победа дыгыдыг
        if pygame.sprite.collide_rect(player, finish):
            paused - True
            BG = pygame.image.load('congratulation.jpg')
            BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
            final = True
            text_fin = text_win
    #game over
    elif paused and final:
        window.fill(BLUE)
        window.blit(text_fin, (225, 200))
        window.blit(text_restart, (240,300)) 
    #обновление состояние ядра
    pygame.display.update()
    #установка тикрейта
    clock.tick(80)