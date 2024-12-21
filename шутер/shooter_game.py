
from pygame import *
from random import randint

wn = display.set_mode((700,500))
display.set_caption('shooter')


fon = transform.scale(image.load('galaxy.jpg'),(700,500))
fps = 60
finish = 0
clock = time.Clock()
game = 1
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
class Player(sprite.Sprite):
    def __init__(self, image_player,x,y,size_x,size_y,speed,life):
        super().__init__()
        self.image= transform.scale(image.load(image_player),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life
        
    def show(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
        
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] :
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed


class Enemy(Player):
    def update(self):

        self.rect.y += self.speed
        if self.rect.y> 500:
            self.rect.y = -10

rocket = Player("rocket.png",300,400, 60,130,5,5)
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png',randint(0,650),0,60,60,randint(1,5),0)
    monsters.add(enemy)
while game:
    for e in event.get():
            if e.type == QUIT:
                game = 0

    if not finish:
        wn.blit(fon,(0,0))
        rocket.draw()
        rocket.update()
        


    display.update()
    clock.tick(fps)            































































































































































