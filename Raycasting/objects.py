import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (163, 214, 245)
BROWN = (218, 160, 109)


class Line:
    def __init__(self, screen, color, start, end):
        self.screen = screen
        self.start = start
        self.end = end
        self.color = color

    def draw(self):
        self.this = pygame.draw.line(self.screen, self.color, self.start, self.end)


class Circle:
    def __init__(self, screen, color, x, y, radius):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.this = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class Square:
    def __init__(self, screen, color, x, y, size):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.ts = (self.x, self.y)
        self.te = (self.x + self.size, self.y)
        self.bs = (self.x, self.y + self.size)
        self.be = (self.x + self.size, self.y + self.size)
        self.ls = (self.x, self.y)
        self.le = (self.x, self.y + self.size)
        self.rs = (self.x + self.size, self.y)
        self.re = (self.x + self.size, self.y + self.size)
        self.sides = [(self.ts, self.te, "t"), (self.bs, self.be, "b"), (self.ls, self.le, "l"), (self.rs, self.re, "r")]

    def draw(self):
        self.top = pygame.draw.line(self.screen, self.color, self.ts, self.te)
        self.bottom = pygame.draw.line(self.screen, self.color, self.bs, self.be)
        self.left = pygame.draw.line(self.screen, self.color, self.ls, self.le)
        self.right = pygame.draw.line(self.screen, self.color, self.rs, self.re)


class ThreeDRect:
    def __init__(self, screen, x, w):
        self.screen = screen
        self.x = x
        self.w = w
    
    def draw(self, lol, cv, side):
        if side == "t":
            color = (cv, 0, 0)
        if side == "b":
            color = (cv, cv, 0)
        if side == "l":
            color = (0, cv, 0)
        if side == "r":
            color = (0, 0, cv)
        if side == "w":
            color = (0, 0, cv)

        self.y = 250 - lol
        self.h = 250 + lol*2

        self.this = pygame.draw.rect(self.screen, color, (self.x, self.y, self.w, self.h))