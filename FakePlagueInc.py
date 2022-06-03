#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import threading
import random
import pygame

pygame.init()

class Focolaio(threading.Thread):
    def __init__(self, x, y, raggio):
        threading.Thread.__init__(self)
        self.x=x
        self.y=y
        self.raggio=raggio

    def run(self):
        self.spawn()

    def spawn(self):
        global focolai
        focolai-=1
        r=self.raggio+1
        self.confini(self.x, self.y)
        while self.raggio:
            semFocolai.acquire(1)
            pygame.draw.circle(window, (255, 0, 0), [self.x, self.y], r-self.raggio)
            self.raggio-=1
            pygame.display.update()
            semFocolai.release()

    def confini(self, x, y):
        verx=False
        very=False
        continent=random.randint(0, 6)
        while verx==False or very==False:
            # Australia
            if continent==0:
                zona=random.randint(0, 1)
                if zona==0:
                    if x>990 and x<1060:
                        verx=True
                        self.x=x
                    if y>500 and y<550:
                        very=True
                        self.y=y
                if zona==1:
                    if x>930 and x<1060:
                        verx=True
                        self.x=x
                    if y>440 and y<470:
                        very=True
                        self.y=y
            # North America
            if continent==1:
                zona=random.randint(0, 12)
                if zona==0:
                    if x>230 and x<350:
                        verx=True
                        self.x=x
                    if y>250 and y<340:
                        very=True
                        self.y=y
                if zona==1:
                    if x>440 and x<530:
                        verx=True
                        self.x=x
                    if y>100 and y<180:
                        very=True
                        self.y=y
                if zona==2:
                    if x>530 and x<560:
                        verx=True
                        self.x=x
                    if y>200 and y<210:
                        very=True
                        self.y=y
                if zona==3:
                    if x>640 and x<680:
                        verx=True
                        self.x=x
                    if y>110 and y<130:
                        very=True
                        self.y=y
                if zona==4:
                    if x>190 and x<310:
                        verx=True
                        self.x=x
                    if y>180 and y<250:
                        very=True
                        self.y=y
                if zona==5:
                    if x>100 and x<180:
                        verx=True
                        self.x=x
                    if y>180 and y<220:
                        very=True
                        self.y=y
                if zona==6:
                    if x>230 and x<310:
                        verx=True
                        self.x=x
                    if y>130 and y<180:
                        very=True
                        self.y=y
                if zona==7:
                    if x>270 and x<300:
                        verx=True
                        self.x=x
                    if y>350 and y<390:
                        very=True
                        self.y=y
                if zona==8:
                    if x>360 and x<390:
                        verx=True
                        self.x=x
                    if y>220 and y<300:
                        very=True
                        self.y=y
                if zona==9:
                    if x>400 and x<420:
                        verx=True
                        self.x=x
                    if y>240 and y<270:
                        very=True
                        self.y=y
                if zona==10:
                    if x>370 and x<440:
                        verx=True
                        self.x=x
                    if y>90 and y<140:
                        very=True
                        self.y=y
                if zona==11:
                    if x>320 and x<400:
                        verx=True
                        self.x=x
                    if y>170 and y<220:
                        very=True
                        self.y=y
                if zona==12:
                    if x>320 and x<360:
                        verx=True
                        self.x=x
                    if y>100 and y<160:
                        very=True
                        self.y=y
            # South America
            if continent==2:
                zona=random.randint(0, 1)
                if zona==0:
                    if x>350 and x<440:
                        verx=True
                        self.x=x
                    if y>420 and y<450:
                        very=True
                        self.y=y
                if zona==1:
                    if x>360 and x<490:
                        verx=True
                        self.x=x
                    if y>450 and y<630:
                        very=True
                        self.y=y
            # Europe
            if continent==3:
                zona=random.randint(0, 4)
                if zona==0:
                    if x>680 and x<740:
                        verx=True
                        self.x=x
                    if y>210 and y<280:
                        very=True
                        self.y=y
                if zona==1:
                    if x>600 and x<680:
                        verx=True
                        self.x=x
                    if y>250 and y<290:
                        very=True
                        self.y=y
                if zona==2:
                    if x>580 and x<720:
                        verx=True
                        self.x=x
                    if y>300 and y<320:
                        very=True
                        self.y=y
                if zona==3:
                    if x>640 and x<660:
                        verx=True
                        self.x=x
                    if y>190 and y<240:
                        very=True
                        self.y=y
                if zona==4:
                    if x>660 and x<700:
                        verx=True
                        self.x=x
                    if y>180 and y<200:
                        very=True
                        self.y=y
            # Asia
            if continent==4:
                zona=random.randint(0, 7)
                if zona==0:
                    if x>1120 and x<1150:
                        verx=True
                        self.x=x
                    if y>180 and y<220:
                        very=True
                        self.y=y
                if zona==1:
                    if x>1130 and x<1110:
                        verx=True
                        self.x=x
                    if y>180 and y<220:
                        very=True
                        self.y=y
                if zona==2:
                    if x>870 and x<1010:
                        verx=True
                        self.x=x
                    if y>160 and y<200:
                        very=True
                        self.y=y
                if zona==3:
                    if x>740 and x<1030:
                        verx=True
                        self.x=x
                    if y>200 and y<290:
                        very=True
                        self.y=y
                if zona==4:
                    if x>780 and x<970:
                        verx=True
                        self.x=x
                    if y>290 and y<360:
                        very=True
                        self.y=y
                if zona==5:
                    if x>840 and x<760:
                        verx=True
                        self.x=x
                    if y>300 and y<340:
                        very=True
                        self.y=y
                if zona==6:
                    if x>840 and x<860:
                        verx=True
                        self.x=x
                    if y>370 and y<400:
                        very=True
                        self.y=y
                if zona==7:
                    if x>910 and x<940:
                        verx=True
                        self.x=x
                    if y>370 and y<400:
                        very=True
                        self.y=y
            # Africa
            if continent==5:
                zona=random.randint(0, 2)
                if zona==0:
                    if x>580 and x<760:
                        verx=True
                        self.x=x
                    if y>340 and y<410:
                        very=True
                        self.y=y
                if zona==1:
                    if x>650 and x<700:
                        verx=True
                        self.x=x
                    if y>430 and y<530:
                        very=True
                        self.y=y
                if zona==2:
                    if x>740 and x<760:
                        verx=True
                        self.x=x
                    if y>490 and y<520:
                        very=True
                        self.y=y
            # Antartica
            if continent==6:
                if x>537 and x<956 or x>400 and x<430:
                    verx=True
                    self.x=x
                if y>680 and y<720:
                    very=True
                    self.y=y

            if verx==False:
                x=random.randint(0, 1280)
            if very==False:
                y=random.randint(0, 720)

window=pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fake PlagueInc")
window.fill((255, 255, 255))
screen=pygame.image.load("world.png")
window.blit(screen, (0, 0))
pygame.display.update()
focolai=200
semFocolai=threading.Lock()
lista=[]
for i in range(0, focolai):
    f=Focolaio(random.randint(0, 1280), random.randint(0, 720), random.randint(4, 20))
    f.start()
    lista.append(f)

for f in lista:
    f.join()

print("Terminato")
