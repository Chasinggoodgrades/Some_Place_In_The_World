#########################
# Made By: Chase Poland #
# 02/10/2018            #
# Snowy Night           #
#########################

# Imports
import pygame
import random
import math

# Initialize game engine
pygame.init()
pygame.mixer.init()
from pygame.locals import*


# Window
SIZE = (800, 600)
TITLE = "Some place in the World"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

#Picture Imports
SKY = pygame.image.load('pictures/bingo.png')
NIGHT = pygame.image.load('pictures/night.png')
SANTA = pygame.image.load('pictures/santa.png')
GSKY = pygame.image.load('pictures/gsky.png')
GNIGHT = pygame.image.load('pictures/gnight.png')
PIKACHU = pygame.image.load('pictures/pokemon.png')
THANKS = pygame.image.load('pictures/thanks.png')

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
WHITE = (255, 255, 255)
ORANGE = (255, 125, 0)
BLUE = (0, 0, 255)
BROWN = (107, 69, 9)
GREY = (128, 128, 128)
BBROWN = (139,119,101)

#Sound Effects
pygame.mixer.init()
pygame.mixer.music.load("sounds/snow.mp3")
pygame.mixer.music.play(-1)

# Make Stars
stars = []
for i in range(100):
    x = random.randrange(400, 800)
    y = random.randrange(1, 180)
    r = random.randrange(2, 3)
    stars.append([x, y, r, r])
stars2 = []
for i in range(50):
    x = random.randrange(1, 400)
    y = random.randrange(1, 40)
    r = random.randrange(2, 3)
    stars2.append([x, y, r, r])
stars3 = []
for i in range(40):
    x = random.randrange(150, 200)
    y = random.randrange(1, 150)
    r = random.randrange(2, 3)
    stars3.append([x, y, r, r])
stars4 = []
for i in range(300):
    x = random.randrange(1, 800)
    y = random.randrange(1, 150)
    r = random.randrange(2, 3)
    stars4.append([x, y, r, r])
    
# Make Clouds
num_clouds = 5
clouds = []
for i in range (num_clouds):
    x = random.randrange(-800, 800)
    y = random.randrange(-50, 100)
    speed = random.randrange(-5, -1)
    loc = [x, y, speed]
    clouds.append(loc)

#Make santa / Pikachu
santa = []
for i in range(50):
    x = random.randint(-400, 800)
    y = random.randint(410, 500)
    santa.append([x, y])

def draw_thanks(x, y):
    screen.blit(THANKS, (x, y))

def draw_santa(x, y):
    screen.blit(SANTA,(x, y))

def draw_PIKACHU(x, y):
    screen.blit(PIKACHU, (x, y))

def day_night():
    if daytime == True and snowing == True:
        screen.blit(SKY, (0, 0))
    elif daytime == False and snowing == True:
        screen.blit(NIGHT, (0, 0))
    elif daytime == True and snowing == False:
        screen.blit(GSKY, (0, 0))
    else:
        screen.blit(GNIGHT, (0, 0))

def make_rain():
    num_droplets = 150
    global rain
    rain = []
    for i in range(num_droplets):
        x = random.randrange(0, 1000)
        y = random.randrange(-100, 400)
        r = random.randrange(1, 5)
        stoplet = random.randrange(400, 700)
        droplet = [x, y, r, r, stoplet]
        rain.append(droplet)

def make_snow():
    num_drops = 150
    global snow
    snow = []
    for i in range(num_drops):
        x = random.randrange(0, 1000)
        y = random.randrange(-100, 400)
        r = random.randrange(1, 10)
        stop = random.randrange(400, 700)
        drop = [x, y, r, r, stop]
        snow.append(drop)

def snow_rain():
    if snowing == True:
        make_snow()
    else:
        make_rain()

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]

    if daytime == True:
        C_COLOR = (255, 255, 255)
    else:
        C_COLOR = (128, 128, 128)

    pygame.draw.ellipse(screen, C_COLOR, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, C_COLOR, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, C_COLOR, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, C_COLOR, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, C_COLOR, [x + 20, y + 20, 60, 40])

def snowman(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 20, 20])
    pygame.draw.ellipse(screen, WHITE, [x - 5, y + 15, 30, 30])
    pygame.draw.ellipse(screen, WHITE
                        , [x - 10, y + 30, 40, 40])

def draw_snowdrop(drop):
    rect = drop[:4]
    if daytime == True:
        S_COLOR = (255, 255, 255)
    else:
        S_COLOR = (255,222,173)
    pygame.draw.ellipse(screen, S_COLOR, rect)

def draw_raindrop(droplet):
    rect = droplet[:4]
    pygame.draw.ellipse(screen, BLUE, rect)

def fence(x, y):
    y = 380
    for x in range(5, 800, 30):
        post = ([x+5, y], [x+10, y + 5], [x+10, y+40], [x, y+40], [x, y+5])
        pygame.draw.polygon(screen, BROWN, post)
        pygame.draw.rect(screen, BROWN, [0, y+10, 900, 5])
        pygame.draw.rect(screen,BROWN, [0, y+30, 800, 5])

daytime = True
snowing = True

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                snowing = not snowing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    daytime = not daytime
    # Game logic
    for c in clouds:
        c[0] -= c[2]

        if c[0] > 800:
            c[0] = random.randrange(-800, -100)
            c[1] = random.randrange(-50, 100)

    rain = []
    for n in rain:
        n[1] += 2

        if n[1] >400:
            n[0] = random.randrange(0, 800)
            n[1] = random.randrange(0, 10)
    snow = []
    for n in snow:
        n[1] += 0

        if n[1] >400:
            n[0] = random.randrange(0, 800)
            n[1] = random.randrange(0, 10)

# Move Rain
    for r in rain:
        r[0] -= 1
        r[1] += 4

        if r[1] > r[4]:
            r[0] = random.randrange(0, 1000)
            r[1] = random.randrange(-100, 0)

# Move Snow
    for r in snow:
        r[0] -= 0
        r[1] += 4
        if r[1] > r[4]:
            r[0] = random.randrange(0, 1000)
            r[1] = random.randrange(-100, 0)

# Move Santa/PIKACHU
    for r in santa:
        r[1] += random.randint(0, 1)
        if r[1] > 0:
            r[0] -= math.sqrt(r[1])
        ground_limit = random.randint(500, 700)
        if r[1] > ground_limit:
            r[1] = random.randint(400, 600)
            r[0] = random.randint(400, 800)

############# Drawing code #############

# Background
    day_night()

#Snow and Rain
    snow_rain()

# Stars
    if daytime == False:
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)
    if daytime == False:
        for s in stars2:
            pygame.draw.ellipse(screen, WHITE, s)
    if daytime == False:
        for s in stars3:
            pygame.draw.ellipse(screen, WHITE, s)
    if daytime == False and snowing == False:
        for s in stars4:
            pygame.draw.ellipse(screen, WHITE, s)

# Clouds
    for c in clouds:
        draw_cloud(c)

#Santas / PIKACHU
    if snowing == True:
        for r in santa:
            draw_santa(r[0], r[1])
    else:
        for r in santa:
            draw_PIKACHU(r[0], r[1])

#Thanks
    if snowing == False and daytime == False:
        draw_thanks(520, 210)
            
# Fence
    fence(0, 0)

# Snow and Rain
    if snowing == True:
        for r in snow:
            draw_snowdrop(r)
    else:
        for r in rain:
            draw_raindrop(r)

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
