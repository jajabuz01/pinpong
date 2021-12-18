from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("pinpong")
background = transform.scale(image.load("камино.jpg"), (win_width, win_height))

def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y >5:
        self.rect.y -= self.speed

def update_l(self):
    keys = key.get_pressed()
    if keys[K_s] and self.rect.y >5:
        self.rect.y -= self.speed

def update_l(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y >5:
        self.rect.y -= self.speed

def update_l(self):
    keys = key.get_pressed()
    if keys[K_DOWN] and self.rect.y >5:
        self.rect.y -= self.speed

font1 = font.Font(None,35)
lose1 = font1.render(
    'PLAYER 1 LOSE!',True, (180,0,0))

while game:
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

speed_x = 3
speed_y = 3


while game:
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(racket1,ball)
    or sprite.collide_rect(racket2,ball):
        speed_x *=-1

