from pygame import *
from random import *
win = 500
winda = display.set_mode((700,win))
winda

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_sizex,player_sizey,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(50,50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        winda.blit(self.image,(self.rect.x, self.rect.y))
    
        
back = transform.scale(image.load("wow.png"),(700,500))
game = True
class chel(GameSprite):
    def __init__(self,enemy_im,enemy_x,enemy_y,enrect_x,enrect_y):
        self.enemy_im = enemy_im
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        
    def reset():
        winda.blit(self.enemy_im,(self.rect.x, self.rect.y))
class plr(GameSprite):
    def update(self):
        press = key.get_pressed()
        if press[K_w]:
            
            self.rect.y -= self.speed
            
        
        if press[K_s]:
           
            self.rect.y += player.speed

class plr2(GameSprite):
    def update(self):
        press = key.get_pressed()
        if press[K_UP]:
            
            self.rect.y -= self.speed
            
        
        if press[K_DOWN]:
           
            self.rect.y += player.speed
             

class bot(GameSprite):
    def update(self):
        spy = 2
        spx = 2
        s = randint(1,4)
        s2 = randint(1,4)
        press = key.get_pressed()
        
        if self.rect.y != 700 and self.rect.x != 500:
            if s == 1:
                self.rect.y -= spy
            if s == 2:
                self.rect.y += spy
            if s == 3:
                self.rect.y -= spy
            if s == 4:
                self.rect.y += spy

                
            if s2 == 1:
                self.rect.x -= spx
            if s2 == 2:
                self.rect.x += spx
            if s2 == 3:
                self.rect.x -= spx
            if s2 == 4:
                self.rect.x += spx
            if self.rect.y == 700 and self.rect.x == 500: 
                self.rect.y = 350
                self.rect.x = 250
            sprites_lists = sprite.collide_rect(player,bot)
            if sprites_lists == True:
                spx *= -1
            sprites_lists = sprite.collide_rect(player2,bot)
            if sprites_lists == True:
                spx *= -1
        
           
                
             
          
           
    

        
       
figna = False
        
display.set_caption("ладна")
clock = time.Clock()
fps = 60




clock.tick(fps)

player = plr('pi.png',100,400,600,600,3)
player2 = plr2('pi.png',500,400,600,600,3)
bot = bot('boti.png', 350, 250, 150,150,1)
img = 'pi.png'

while game:
    
    winda.blit(back,(0,0))
    
    

    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
        
        
        
    press = key.get_pressed()
    
    
    
   
    if figna == False:
        
        player.reset()
        
        player.update()
        player2.reset()
        
        player2.update()

        bot.update()
        bot.reset()
    else:
        print("ну канава")
    
    display.update()
   
