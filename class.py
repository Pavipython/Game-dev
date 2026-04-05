import pygame, pyautogui
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Object oriented programming using pygame")

class Box:
    def __init__(self, x, y, w, h, c):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.c=c
    def display(self):
        pygame.draw.rect(screen, self.c,(self.x, self.y, self.w, self.h))