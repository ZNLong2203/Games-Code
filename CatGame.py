import pygame,sys
from pygame.locals import *
pygame.init()
#set up window
size=(600,300)
form=pygame.display.set_mode(size)
white=(255,255,255)
catimg=pygame.image.load('cat.png')
x=0
y=0
p=(x,y)
h='phai'
while True:
                form.fill(white)
                if (h=='phai'):
                                x=x+1
                                p=(x,y)
                                if (x==size[0]-catimg.get_width()):
                                                h='xuong'
                if (h=='xuong'):
                                 y=y+1
                                 p=(x,y)
                                 if (y==size[1]-catimg.get_height()):
                                                 h='trai'
                if (h=='trai'):
                                x=x-1
                                p=(x,y)
                                if (x==0):
                                                h='len'
                if (h=='len'):
                                y=y-1
                                p=(x,y)
                                if (y==0):
                                                h='phai'
                form.blit(catimg,p)
                for e in pygame.event.get():
                                if e.type==QUIT:
                                                pygame.quit()
                                                sys.exit()
                pygame.display.update()
