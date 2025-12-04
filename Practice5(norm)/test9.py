import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Компас - Сбитнева Дарья")

# Цвета
bg = (20, 30, 50)
c1 = (40, 50, 70)
red = (255, 50, 50)
white = (220, 220, 220)

x, y = 250, 250
r = 150
angle = 0
speed = 0.5

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT: angle += 10
            if e.key == pygame.K_RIGHT: angle -= 10
            if e.key == pygame.K_UP: speed += 0.1
            if e.key == pygame.K_DOWN: speed = max(0.1, speed - 0.1)
            if e.key == pygame.K_r: angle, speed = 0, 0.5
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    angle += speed
    angle %= 360


    screen.fill(bg)


    pygame.draw.circle(screen, c1, (x, y), r)
    pygame.draw.circle(screen, (60, 80, 100), (x, y), r, 3)



    f = pygame.font.SysFont(None, 30)
    for i, s in enumerate(["N", "E", "S", "W"]):
        rad = math.radians(i * 90)
        tx = x + (r-30) * math.cos(rad)
        ty = y + (r-30) * math.sin(rad)
        screen.blit(f.render(s, 1, white), (tx-10, ty-10))



    rad = math.radians(angle)
    ax = x + (r-20) * math.cos(rad)
    ay = y + (r-20) * math.sin(rad)
    pygame.draw.line(screen, red, (x, y), (ax, ay), 6)


    rad2 = math.radians(angle + 180)
    ax2 = x + (r-30) * math.cos(rad2)
    ay2 = y + (r-30) * math.sin(rad2)
    pygame.draw.line(screen, white, (x, y), (ax2, ay2), 4)


    pygame.draw.circle(screen, (30, 40, 60), (x, y), 8)


    screen.blit(f.render(f"{angle:.0f}°", 1, white), (x-15, y-40))


    f2 = pygame.font.SysFont(None, 32)
    screen.blit(f2.render("Компас", 1, white), (200, 20))
    screen.blit(f.render("Сбитнева Дарья", 1, white), (180, 50))


    f3 = pygame.font.SysFont(None, 20)
    txt = ["← → - поворот", "↑ ↓ - скорость", "R - сброс"]
    for i, t in enumerate(txt):
        screen.blit(f3.render(t, 1, white), (20, 400+i*25))
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

