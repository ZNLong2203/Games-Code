#Code và ảnh đặt trong phần mô tả, các bạn có thể tải về
import pygame,sys
from pygame.locals import *
pygame.init()
#set up window
size=(1280,720) #HD display
form=pygame.display.set_mode(size)
white=(255,255,255)
cat2p=pygame.image.load('cat2p.png')
cat2t=pygame.image.load('cat2t.png')
cat=cat2p #init image
x=0
y=0
p=(x,y)
while True:
                form.fill(white)                     
                form.blit(cat,p)
                for e in pygame.event.get():
                                if e.type==QUIT:
                                                pygame.quit()
                                                sys.exit()
                                if e.type==KEYDOWN:
                                              if  e.key== 275: #right
                                                              x=x+50
                                                              p=(x,y)
                                                              cat=cat2t
                                                              form.blit(cat,p)
                                              if e.key==276: #left
                                                              x=x-50
                                                              p=(x,y)
                                                              cat=cat2p
                                                              form.blit(cat,p)
                                              if e.key==274: #bottom
                                                               y=y+50
                                                               p=(x,y)
                                                               form.blit(cat,p)
                                              if e.key==273: #top
                                                                y=y-50
                                                                p=(x,y)
                                                                form.blit(cat,p)
                                
                                               
                pygame.display.update()
