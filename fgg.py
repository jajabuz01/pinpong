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