import pygame
import time
mw = pygame.display.set_mode((500, 500))
back = (200, 255, 255)
mw.fill(back)
WHITE = (255, 255, 255)
WIN_COLOR = (0, 200, 0)
LOSE_COLOR = (255, 0, 0)
# переменные, отвечающие за координаты платформы
racket_x = 200
racket_y = 330
move_right = False
move_left = False
speed_x = 1
speed_y = 1
game_over = False




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

    def collidrect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x = 0, y = 0, width = 10, height = 10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

    def set_color(self):
        self.image.set_colorkey(WHITE)


class Label(Area):

    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))



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
        d = Picture('enemi.png', x, y, 50, 50)
        monsters.append(d)
        x = x + 55
    count = count - 1
while not game_over:
    ball.set_color()
    ball.fill()
    ball.draw()
    #platform.set_color()
    platform.draw()
    platform.fill()
    for f in monsters:
        f.set_color()
        f.fill()
        f.draw()
        if f.rect.colliderect(ball.rect):
            monsters.remove(f)
            f.fill()
            speed_y *= -1
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.colliderect(platform):
        speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if len(monsters) == 0:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('YOU WIN', 60, WIN_COLOR)
        time_text.draw(10, 10)
        game_over = True
    if ball.rect.y > (racket_y + 20):
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('YOU LOSE', 60, LOSE_COLOR)
        time_text.draw(10, 10)
        game_over = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
    if move_left:
        platform.rect.x -= 3
    if move_right:
        platform.rect.x += 3
    pygame.display.update()
