#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import threading
import time
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
        print(focolai)
        r=self.raggio+1
        while self.raggio:
            semFocolai.acquire(1)
            pygame.draw.circle(window, (255, 0, 0), [self.x, self.y], r-self.raggio)
            self.raggio-=1
            time.sleep(0.2)
            print(self.raggio)
            pygame.display.update()
            semFocolai.release()

window=pygame.display.set_mode((640, 360))
window.fill((255, 255, 255))
pygame.display.update()
focolai=20
semFocolai=threading.Lock()
lista=[]
for i in range(0, 20):
    f=Focolaio(random.randint(0, 640), random.randint(0, 360), random.randint(0, 10))
    f.start()
    lista.append(f)

for e in lista:
    e.join()

print("Terminato")
