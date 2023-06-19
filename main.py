import pygame
import time
mw = pygame.display.set_mode((500, 500))
back = (200, 255, 255)
mw.fill(back)
WHITE = (255, 255, 255)
# переменные, отвечающие за координаты платформы
racket_x = 200
racket_y = 330


class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # прямоугольник
        self.fill_color = back

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):  # обводка существующего прямоугольника
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Picture(Area):
    def __init__(self, filename, x = 0, y = 0, width = 10, height = 10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

    def set_color(self):
        self.image.set_colorkey(WHITE)


ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platforma.png', racket_x, racket_y, 100, 30)
start_x = 5  # координаты создания первого монстра
start_y = 5
count = 9  # количество монстров в верхнем ряду
monsters = []
for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)
    for i in range(count):
        d = Picture('anonim kosta.png', x, y, 50, 50)
        monsters.append(d)
        x = x + 55
    count = count - 1
while True:
    ball.set_color()
    ball.fill()
    ball.draw()
    platform.set_color()
    platform.fill()
    platform.draw()
    for f in monsters:
        f.set_color()
        f.fill()
        f.draw()
    pygame.display.update()
